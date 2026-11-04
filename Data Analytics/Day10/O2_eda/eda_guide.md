# Exploratory Data Analysis (EDA) Guide

Exploratory Data Analysis (EDA) is the foundational process of analyzing datasets to summarize their main characteristics, often using visual methods and statistical summaries. Before building predictive models or deriving final insights, EDA helps identify patterns, detect anomalies, test hypotheses, and verify assumptions.

---

### The 4 Core Steps of EDA

#### 1. Inspecting the Structure
First, examine the dimensions and schema of your dataset.
* **Dimensions:** Determine the total number of rows ($N$) and columns ($P$).
* **Data Types:** Categorize variables as categorical, numerical (discrete or continuous), or temporal.
* **Memory & Completeness:** Check overall memory usage and the non-null count for each feature $X_j$.

#### 2. Cleaning and Finding the Messy Bits
Identify data quality issues that could skew analysis or model performance.
* **Missing Data:** Quantify missing values per column:
  $$\text{Missing Percentage} = \left( \frac{\sum_{i=1}^{N} \mathbb{I}(x_i = \text{null})}{N} \right) \times 100\%$$
* **Outlier Detection:** Locate extreme values using the Interquartile Range ($IQR$):
  $$IQR = Q_3 - Q_1$$
  where points lying outside the range $[Q_1 - 1.5 \times IQR, \; Q_3 + 1.5 \times IQR]$ are flagged as potential outliers.

#### 3. Summarizing with Numbers
Calculate key descriptive statistics to understand the central tendency and spread of each variable.
* **Central Tendency:**
  * **Mean ($\mu$):**
    $$\mu = \frac{1}{N} \sum_{i=1}^{N} x_i$$
  * **Median:** The middle value of the sorted data sequence.
* **Spread & Variability:**
  * **Variance ($\sigma^2$):**
    $$\sigma^2 = \frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})^2$$
  * **Standard Deviation ($\sigma$):**
    $$\sigma = \sqrt{\sigma^2}$$

#### 4. Visualizing the Story
Transform raw numbers into graphical representations to uncover relationships and distributions.
* **Univariate Distributions:** Use **Histograms** and **KDE plots** to inspect feature distributions and evaluate skewness:
  $$\text{Skewness} = \frac{\frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{x})^3}{\sigma^3}$$
* **Bivariate & Multivariate Relationships:**
  * **Scatter Plots:** Examine non-linear trends or linear association.
  * **Correlation Matrix:** Compute Pearson's correlation coefficient ($r$) between continuous variables $X$ and $Y$:
    $$r_{XY} = \frac{\sum_{i=1}^{N} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{N} (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^{N} (y_i - \bar{y})^2}}$$
* **Box Plots:** Visualize five-number summaries ($\text{Min}$, $Q_1$, $\text{Median}$, $Q_3$, $\text{Max}$) and highlight outliers.