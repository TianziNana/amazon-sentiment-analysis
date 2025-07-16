import pandas as pd
from tqdm import tqdm  # 进度条工具，可选

# 加载评论数据（主要数据集）
chunks = []
chunk_size = 50000  # 分批读取避免内存不足

# 使用分块读取
for chunk in tqdm(pd.read_json('All_Beauty.jsonl', lines=True, chunksize=chunk_size)):
    chunks.append(chunk)

reviews_df = pd.concat(chunks)

print("评论数据加载完成！")
print(f"共加载 {len(reviews_df)} 条评论")
print(reviews_df.head())

# 加载元数据（产品信息）
meta_chunks = []
for chunk in tqdm(pd.read_json('meta_All_Beauty.jsonl', lines=True, chunksize=chunk_size)):
    meta_chunks.append(chunk)

meta_df = pd.concat(meta_chunks)

print("\n元数据加载完成！")
print(f"共加载 {len(meta_df)} 条产品信息")
print(meta_df.head())


import pandas as pd
import json
import matplotlib.pyplot as plt

# 1. 加载评论数据（已确认成功）
reviews_df = pd.read_json('All_Beauty.jsonl', lines=True)
print(f"成功加载评论数据: {len(reviews_df)} 条记录")

# 2. 加载元数据（使用更稳健的方法）
meta_data = []
with open('meta_All_Beauty.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        try:
            # 尝试解析每一行
            data = json.loads(line)
            meta_data.append(data)
        except json.JSONDecodeError:
            # 跳过格式错误的行
            continue

# 转换为 DataFrame
meta_df = pd.DataFrame(meta_data)
print(f"成功加载元数据: {len(meta_df)} 条记录")

# 3. 基本数据分析
print("\n评论数据结构:")
print(reviews_df.info())

print("\n元数据结构:")
print(meta_df.info())
# 查看列名及其计数
from collections import Counter
Counter(reviews_df.columns)
Counter(meta_df.columns)

# 如果发现重复列，例如两个 parent_asin
reviews_df = reviews_df.loc[:, ~reviews_df.columns.duplicated()]
meta_df = meta_df.loc[:, ~meta_df.columns.duplicated()]

# 在评论表里重命名 asin→parent_asin
reviews_df = reviews_df.rename(columns={'asin': 'parent_asin'})

# 然后再 merge
df_merged = pd.merge(reviews_df, meta_df, on='parent_asin', how='left')

# 优化数据类型
# 数值列优化
df_merged['rating'] = pd.to_numeric(df_merged['rating'], downcast='integer')
df_merged['helpful_vote'] = pd.to_numeric(df_merged['helpful_vote'], downcast='integer')

# 分类列优化（高基数列）
df_merged['parent_asin'] = df_merged['parent_asin'].astype('category')
df_merged['user_id'] = df_merged['user_id'].astype('category')

# 布尔列优化
if 'verified_purchase' in df_merged.columns:
    df_merged['verified_purchase'] = df_merged['verified_purchase'].astype('bool')

# 时间列优化
if 'timestamp' in df_merged.columns:
    df_merged['timestamp'] = pd.to_datetime(df_merged['timestamp'])
    
# 文本列优化（仅当文本特别长时）
# df_merged['text'] = df_merged['text'].astype('string')
# 为常用查询列设置索引
df_merged = df_merged.set_index('parent_asin')  # 商品ID作为主索引
df_merged = df_merged.sort_index()  # 排序索引提高查询速度

# 添加多级索引（如果需要）
# df_merged = df_merged.set_index(['parent_asin', 'user_id'])
# 检查缺失值
missing_data = df_merged.isnull().sum()
print("缺失值统计:\n", missing_data[missing_data > 0])
