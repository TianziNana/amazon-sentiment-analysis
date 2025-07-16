
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



# Amazon Sentiment Analysis: Large-Scale User Behavior Research

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Data Science](https://img.shields.io/badge/Data%20Science-Advanced-green.svg)
![Effect Size](https://img.shields.io/badge/Effect%20Size-R²%3D0.35-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Project Overview

This project conducts a comprehensive analysis of **Amazon beauty product reviews** to investigate the causal impact of user sentiment on rating behavior. Through advanced statistical modeling and machine learning techniques, we discovered significant **sentiment threshold effects** and identified distinct user behavioral patterns.

### Key Achievements
- **Large-scale Analysis**: 701,528 reviews from 631,986 users
- **Strong Effect Size**: R² = 0.35-0.378 (large effect in social sciences)
- **Novel Discovery**: Sentiment threshold effect at -0.483 with 10.7x impact difference
- **User Segmentation**: 5 distinct user behavioral clusters identified
- **Theoretical Innovation**: First application of Weber's Law to digital sentiment analysis

## 📊 Core Findings

### 1. Sentiment Threshold Effect
🎯 Optimal Threshold: -0.483
📈 Below Threshold: r = 0.163, R² = 0.027
📈 Above Threshold: r = 0.538, R² = 0.290
⚡ Effect Magnitude: 10.7x stronger above threshold
### 2. User Behavioral Clusters
| Cluster | Size | Type | Avg Sentiment | Volatility | Avg Rating |
|---------|------|------|---------------|------------|------------|
| 0 | 65 (8.1%) | Stable Moderate | 0.366 | 0.289 | 3.286 |
| 1 | 85 (10.6%) | Stable Negative | -0.167 | 0.134 | 1.716 |
| 2 | 135 (16.9%) | Volatile Positive | 0.346 | 0.430 | 3.548 |
| 3 | 64 (8.0%) | Highly Volatile | 0.206 | 0.592 | 3.837 |
| 4 | 451 (56.4%) | Consistently Positive | 0.695 | 0.073 | 4.704 |

### 3. Feature Importance Analysis
- **Sentiment Level**: 59.9% (Primary factor)
- **Sentiment Change**: 48.5% (Secondary factor)  
- **User Activity**: 2.9% (Moderate factor)
- **Volatility**: 0.1% (Minor factor)

## 🔧 Technical Stack

### Core Technologies
- **Python 3.8+** - Primary development language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib/Seaborn** - Data visualization
- **Scikit-learn** - Machine learning algorithms
- **VADER** - Sentiment analysis toolkit

### Statistical Methods
- **Correlation Analysis** - Cross-sectional and time-series
- **Regression Modeling** - Linear and piecewise regression
- **Clustering** - K-means with optimal cluster selection
- **Statistical Testing** - t-tests, Chow tests, effect size analysis
- **Threshold Detection** - Sliding window analysis

### Advanced Techniques
- **Rolling Window Analysis** - Temporal pattern detection
- **Piecewise Regression** - Threshold effect modeling
- **Feature Engineering** - Multi-dimensional user profiling
- **Memory Optimization** - Custom algorithms for large datasets

## 📁 Project Structure

## 🚀 Getting Started



### Prerequisites
```bash
Python 3.8+
pip or conda package manager
```

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/amazon-sentiment-analysis.git
cd amazon-sentiment-analysis

# Install dependencies
pip install -r requirements.txt

# Download sample data (if not included)
# Follow instructions in data/README.md
```

### Quick Start
```python
# Basic sentiment analysis
python code/01_data_preprocessing.py

# Run threshold analysis
python code/06_threshold_analysis.py

# Generate visualizations
python code/create_visualizations.py
```

## 📈 Key Results & Visualizations

### 1. Sentiment Distribution & Threshold Effect
- **Cross-sectional correlation**: r = 0.61
- **Time-series correlation**: r = 0.54
- **Threshold detection**: Optimal at -0.483
- **Statistical significance**: p < 0.001

### 2. User Trajectory Analysis
- **Rolling window patterns**: 2, 3, 5-period windows
- **Temporal stability**: 50% positive trends in 5-period windows
- **Volatility patterns**: Increasing with window size

### 3. Business Impact Quantification
- **ROI Coefficient**: 1.72 (direct business value)
- **User Segmentation**: 5 actionable clusters
- **Prediction Accuracy**: R² = 0.35-0.378

## 🔬 Research Methodology

### Phase 1: Foundation (Weeks 1-2)
- Large-scale data preprocessing (701K reviews)
- VADER sentiment analysis implementation
- Basic statistical analysis and correlation

### Phase 2: Multi-level Validation (Weeks 3-4)
- Time-series analysis across user timelines
- Statistical modeling with multiple validation
- User stratification and sampling strategies

### Phase 3: Advanced Analytics (Weeks 5-6)
- Professional-grade visualizations
- K-means clustering with optimal selection
- Comprehensive statistical testing

### Phase 4: Theoretical Innovation (Weeks 7-8)
- Weber's Law application to digital behavior
- Threshold effect analysis and validation
- Theoretical framework development

## 💡 Novel Contributions

### 1. Methodological Innovations
- **Memory-efficient algorithms** for large-scale analysis
- **Multi-validation framework** ensuring robustness
- **Sliding threshold detection** for non-linear effects

### 2. Theoretical Advances
- **First application** of Weber's Law to digital sentiment
- **Threshold effect discovery** in user behavior
- **Psychophysical principles** in e-commerce analytics

### 3. Practical Applications
- **User segmentation** for targeted marketing
- **Sentiment monitoring** systems
- **Predictive modeling** for customer behavior

## 📊 Performance Metrics

| Metric | Value | Interpretation |
|--------|-------|---------------|
| **Sample Size** | 631,986 users | Large-scale analysis |
| **Effect Size** | R² = 0.35 | Large effect (Cohen's standards) |
| **Correlation** | r = 0.61 | Strong relationship |
| **Threshold Impact** | 10.7x difference | Significant non-linearity |
| **Cluster Validity** | 5 distinct groups | Clear segmentation |

## 🔮 Future Work

### Immediate Extensions
- [ ] Deep learning sentiment models (BERT, RoBERTa)
- [ ] Real-time sentiment monitoring system
- [ ] Cross-platform validation (other e-commerce sites)

### Research Directions
- [ ] Causal inference with instrumental variables
- [ ] Temporal dynamics of threshold effects
- [ ] Cross-cultural sentiment analysis

### Business Applications
- [ ] Recommendation system integration
- [ ] A/B testing framework
- [ ] Customer lifetime value prediction

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Areas for Contribution
- Algorithm optimization
- Additional statistical tests
- Visualization enhancements
- Documentation improvements

## 📝 Citation

If you use this work in your research, please cite:

```bibtex
@software{amazon_sentiment_analysis,
  author = {[Your Name]},
  title = {Amazon Sentiment Analysis: Large-Scale User Behavior Research},
  year = {2024},
  url = {https://github.com/yourusername/amazon-sentiment-analysis}
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Amazon for providing the review dataset
- VADER sentiment analysis toolkit
- Scientific Python community
- Statistical methodology references

---

**⭐ If you find this project useful, please give it a star!**

**📧 Contact**: [your.email@example.com]
**🔗 LinkedIn**: [Your LinkedIn Profile]
**📱 Twitter**: [@yourusername]
