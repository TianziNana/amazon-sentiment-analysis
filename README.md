
# 🛍️ Amazon 2023 Beauty Reviews: sentiment-analysis

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Data-Science](https://img.shields.io/badge/Project-Data--Science-brightgreen) ![Effect-Size](https://img.shields.io/badge/R²-0.35-important) ![License](https://img.shields.io/badge/License-MIT-informational)

---

## 📑 Project Overview

**Research Topic:** Investigating the causal impact of user sentiment on rating behavior in Amazon beauty reviews
**Dataset:** 701,528 reviews, 631,986 users (large-scale analysis)
**Duration:** 4-6 weeks (from data processing to theoretical modeling)
**Key Finding:** Discovered a sentiment threshold effect at -0.483, with sentiment above the threshold having 10.7x stronger impact on ratings

---

## 🚩 Project Structure

```
code/               # Data preprocessing and analysis scripts
data/               # Dataset description
results/            # Analysis results and visualizations
docs/               # Methodology and research findings
requirements.txt    # Python dependencies
.gitignore          # Git ignore rules
README.md           # Project overview
```

---

## 📈 Project Progression

### Phase 1️⃣ Data Analysis

* Data cleaning, VADER sentiment analysis, cross-sectional statistics
* **Findings:** Sentiment-rating correlation r=0.61
* **Technical highlight:** Batch processing to handle memory limits

### Phase 2️⃣ Multi-Level Validation

* Rolling window analysis, regression modeling, user stratification
* **Findings:** Regression R²=0.35, time-series correlation r=0.54
* **Methodology:** Robust multi-validation framework

### Phase 3️⃣ Visualization & Clustering

* User trajectory visualization, K-means clustering, radar plots
* **Findings:** Identified 5 user segments with distinct patterns

### Phase 4️⃣ Theoretical Advancement

* Incorporated Weber's Law, sliding threshold modeling
* **Contribution:** Applied psychophysics concepts to digital behavior for the first time

---

## 📊 Key Findings Summary

| Module               | Key Results                              |
| -------------------- | ---------------------------------------- |
| Sentiment vs. Rating | Correlation r=0.61, R²=0.35              |
| User Clustering      | 5 distinct user segments                 |
| Threshold Effect     | Threshold at -0.483, 10.7x impact        |
| Feature Importance   | Sentiment 60% > Change 48% > Activity 3% |

---

## 📂 Sample Visualizations

### 📉 Rolling Window Trend Analysis

![Rolling Window](results/visualizations/user_trajectory_analysis.png)

### 🎯 Cluster Feature Radar Plot

![Cluster Radar](results/visualizations/cluster_radar_analysis_fixed.png)

### 🔍 Sentiment Threshold Effect

![Threshold Effect](results/visualizations/sentiment_threshold_effect_analysis.png)

---

## 🛠️ Technical Highlights

* **Custom Algorithms:** Overcame pandas memory bottlenecks
* **Robust Validation:** Cross-sectional, time-series, stratified validation
* **Theory Integration:** Modeled non-linear threshold effects via psychophysics
* **Engineering Scale:** Processed 700K+ reviews efficiently
* **Business Relevance:** Clear user segmentation, quantifiable ROI

---

## 🏁 How to Use

```bash
# Clone the repository
git clone https://github.com/your-username/amazon-sentiment-analysis.git
cd amazon-sentiment-analysis

# Install dependencies
pip install -r requirements.txt

# Run analysis
python code/01_data_preprocessing.py
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 About Me

**Herbal**
[GitHub](https://github.com/your-username)
[LinkedIn](https://linkedin.com/in/your-username)

---

If you'd like, I can also provide you a **clean .md file version ready to upload** directly. Just say "yes".
