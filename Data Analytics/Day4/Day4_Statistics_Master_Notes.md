# Data Analytics Day 4: Advanced Descriptive Statistics, Sampling, Percentiles & Skewness
> **Module:** Data Analytics - Statistics (Day 4)  
> **Topic Focus:** Bessel's Correction, Monte Carlo Sampling, Welford's Algorithm, Percentiles & Percentile of Score, Hyndman-Fan Quantile Methods, Interquartile Range (IQR), and Skewness (3rd Central Moment)  
> **Author:** Antigravity Coding Assistant  
> **Date:** September 2026

---

## Table of Contents
1. [Pedagogical Learning Sequence](#1-pedagogical-learning-sequence)
2. [Module 1: Robust Measures Recap & Sampling Theory](#2-module-1-robust-measures-recap--sampling-theory)
   - 1.1 Outlier Resistance: Mean vs. Median vs. Trimmed Mean
   - 1.2 Sampling Strategies: With vs. Without Replacement
   - 1.3 Empirical Proof of Bessel's Correction ($ddof=1$) via Monte Carlo Simulation
   - 1.4 **[Bonus Topic]** Welford's Algorithm: Numerically Stable Streaming Variance
3. [Module 2: Percentiles, Quantiles & Percentile Ranks](#3-module-2-percentiles-quantiles--percentile-ranks)
   - 2.1 What is a Percentile? (Score vs. Value)
   - 2.2 Finding the Percentile of a Score: `strict`, `weak`, `rank`, and `mean`
   - 2.3 Hand-Calculation Step-by-Step Walkthrough
4. [Module 3: Interquartile Range (IQR) & Outlier Detection](#4-module-3-interquartile-range-iqr--outlier-detection)
   - 3.1 Quartiles ($Q_1, Q_2, Q_3$) and the IQR Metric
   - 3.2 Manual Calculation (Tukey's / Moore-McCabe Median Split)
   - 3.3 Tukey’s $1.5 \times \text{IQR}$ Boxplot Outlier Fences
   - 3.4 Visualizing Outliers with Boxplots
5. [Module 4: The 9 Hyndman-Fan Quantile Interpolation Methods](#5-module-4-the-9-hyndman-fan-quantile-interpolation-methods)
   - 4.1 Why Do Excel, R, and Python Give Different Quartiles?
   - 4.2 The 9 Hyndman & Fan (1996) Formulations
   - 4.3 NumPy `method` Parameter Deep Dive (`linear`, `weibull`, `midpoint`, etc.)
6. [Module 5: Skewness & The 3rd Statistical Moment](#6-module-5-skewness--the-3rd-statistical-moment)
   - 5.1 Intuition: Symmetry, Right-Skewed (Positive), and Left-Skewed (Negative)
   - 5.2 Mathematical Formulation: 3rd Central Moment ($m_3$) and Standardized Skewness ($\gamma_1$)
   - 5.3 Complete Step-by-Step Derivation 1: Startup Salaries ($[40, 45, 50, 55, 310]$)
   - 5.4 Complete Step-by-Step Derivation 2: Retirement Ages ($[35, 62, 65, 67, 71]$)
   - 5.5 **[Bonus Concepts]** Pearson's & Bowley's Skewness
7. [Module 6: Industry Best Practices & Data Transformations](#7-module-6-industry-best-practices--data-transformations)
   - 6.1 Correcting Skewness in ML: Log, Square Root, and Box-Cox Transforms
   - 6.2 Tooling Overview (DuckDB, Polars, PySpark, Statsmodels)
8. [Module 7: Complete Code Reference Cheat-Sheet](#8-module-7-complete-code-reference-cheat-sheet)

---

## 1. Pedagogical Learning Sequence

To master Day 4 concepts, progress through these stages:

```
[ Day 3 Recap & Outlier Sensitivity ]
               │
               ▼
[ Sampling: With vs. Without Replacement ]
               │
               ▼
[ Monte Carlo Verification of Bessel's Correction (ddof=1) ]
               │
               ▼
[ Welford's Streaming Algorithm (Online Mean & Variance) ]
               │
               ▼
[ Percentiles vs. Percentile Ranks (Strict, Weak, Rank, Mean) ]
               │
               ▼
[ Quartiles, IQR & Tukey's 1.5*IQR Boxplot Outlier Fences ]
               │
               ▼
[ Quantile Estimation: The 9 Hyndman & Fan Methods ]
               │
               ▼
[ Skewness (3rd Moment): Mean vs. Median Shift & Hand Calculations ]
               │
               ▼
[ Skewness Transformations (Log, Sqrt, Box-Cox) ]
```

---

## 2. Module 1: Robust Measures Recap & Sampling Theory

### 1.1 Outlier Resistance: Mean vs. Median vs. Trimmed Mean
As explored in [`O01_recap.ipynb`](file:///d:/Engineering/CDAC_ALL_MODULES/Data%20Analytics/Day4/O01_recap.ipynb):
* **Pristine Data:** $N=100$, drawn from $\mathcal{N}(\mu=50, \sigma=10)$.
  * $\text{Mean} \approx 50.0$, $\text{Median} \approx 50.0$, $\text{Trimmed Mean}(10\%) \approx 50.0$.
* **Corrupted Data:** Introduce a single outlier $x_0 = 1,000,000$.
  * **Mean:** Skyrockets to $\approx 10,000$ (0% Breakdown point - destroyed by 1 outlier).
  * **Median:** Remains $\approx 50.0$ (50% Breakdown point - unaffected).
  * **Trimmed Mean ($10\%$):** Discards the top 10% and bottom 10% before averaging. The $1,000,000$ is trimmed away, preserving the true center $\approx 50.0$.

```python
import numpy as np
import scipy.stats as stats

np.random.seed(42)
data = np.random.normal(loc=50.0, scale=10.0, size=100)
corrupted = data.copy()
corrupted[0] = 1_000_000

print(f"Pristine Mean: {np.mean(data):.2f} | Corrupted Mean: {np.mean(corrupted):.2f}")
print(f"Pristine Median: {np.median(data):.2f} | Corrupted Median: {np.median(corrupted):.2f}")
print(f"Pristine Trimmed (10%): {stats.trim_mean(data, 0.1):.2f} | Corrupted Trimmed (10%): {stats.trim_mean(corrupted, 0.1):.2f}")
```

---

### 1.2 Sampling Strategies: With vs. Without Replacement
* **Sampling with Replacement (`replace=True`):** After an item is picked, it is returned to the pool. It can be selected multiple times.
  * Probabilities remain independent across draws: $P(A \cap B) = P(A) \cdot P(B)$.
  * Used in **Bootstrapping**, Random Forests, and Bagging.
* **Sampling without Replacement (`replace=False`):** Once selected, the item is removed.
  * Probabilities change on each draw (Hypergeometric process).
  * Standard in survey sampling, train/test splitting, and cross-validation.

```python
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_with = np.random.choice(lst, size=5, replace=True)    # May contain duplicates
sample_without = np.random.choice(lst, size=5, replace=False) # All unique
```

---

### 1.3 Empirical Proof of Bessel's Correction ($ddof=1$) via Monte Carlo Simulation

#### The Theoretical Question
Why do we divide by $n-1$ instead of $n$ for sample variance?

#### Mathematical Expectation
When estimating population variance $\sigma^2$ using sample variance with divisor $n$:
$$\mathbb{E}\left[s_{\text{biased}}^2\right] = \mathbb{E}\left[\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2\right] = \frac{n-1}{n}\sigma^2$$
Notice that for sample size $n=10$:
$$\frac{n-1}{n} = \frac{9}{10} = 0.90 \implies \text{Biased formula captures only } 90\% \text{ of true variance!}$$
To eliminate this bias, Bessel's correction divides by $n-1$:
$$\mathbb{E}\left[s_{\text{unbiased}}^2\right] = \mathbb{E}\left[\frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2\right] = \sigma^2$$

#### Monte Carlo Simulation (from `O01_recap.ipynb`)
```python
import numpy as np

np.random.seed(42)
# Population of 100,000 semiconductor chips
chips = np.random.normal(loc=100.0, scale=15.0, size=100_000)
true_var = np.var(chips)  # True population variance = 15^2 = 225

sample_size = 10
num_trials = 10_000
biased_vars = []
unbiased_vars = []

for _ in range(num_trials):
    sample = np.random.choice(chips, size=sample_size, replace=False)
    biased_vars.append(np.var(sample, ddof=0))    # Divisor: n = 10
    unbiased_vars.append(np.var(sample, ddof=1))  # Divisor: n - 1 = 9

print(f"True Population Variance:        {true_var:.4f}")
print(f"Average Unbiased Estimate (n-1): {np.mean(unbiased_vars):.4f} (~ 100% of True)")
print(f"Average Biased Estimate (n):     {np.mean(biased_vars):.4f} (~ 90% of True)")
print(f"Ratio (Biased / Unbiased):       {np.mean(biased_vars) / np.mean(unbiased_vars):.4f} (Exact theory: 9/10 = 0.9)")
```

---

### 1.4 [Bonus Topic] Welford's Algorithm: Numerically Stable Streaming Variance

#### Why is it Needed?
The classic textbook formula for variance is:
$$\text{Var}(X) = \frac{\sum x_i^2 - \frac{(\sum x_i)^2}{n}}{n-1}$$
In computational finance, telemetry streams, and Big Data (PySpark, Kafka), calculating $\sum x_i^2$ for large numbers leads to **Catastrophic Floating-Point Cancellation** (subtracting two massive, nearly identical floating-point numbers leaves garbage precision in Python/C++). Furthermore, it requires two passes over the data.

#### The Algorithm (Welford, 1962)
Updates the mean $M_k$ and the sum of squared differences $S_k$ in a **single pass (streaming)**:
1. Initialize: $M_0 = 0, S_0 = 0$
2. For each new data point $x_k$ at step $k$:
   $$M_k = M_{k-1} + \frac{x_k - M_{k-1}}{k}$$
   $$S_k = S_{k-1} + (x_k - M_{k-1})(x_k - M_k)$$
3. Current sample variance:
   $$s^2 = \frac{S_n}{n-1}, \quad \sigma^2 = \frac{S_n}{n}$$

#### Python Implementation
```python
class WelfordAccumulator:
    """Computes running mean and variance in a single pass with O(1) memory."""
    def __init__(self):
        self.k = 0
        self.M = 0.0
        self.S = 0.0

    def update(self, x):
        self.k += 1
        old_M = self.M
        self.M += (x - old_M) / self.k
        self.S += (x - old_M) * (x - self.M)

    @property
    def mean(self):
        return self.M

    @property
    def sample_variance(self):
        return self.S / (self.k - 1) if self.k > 1 else 0.0

    @property
    def sample_std(self):
        return np.sqrt(self.sample_variance)

# Verification against NumPy
stream_data = [10.5, 12.3, 11.8, 14.2, 13.1, 15.0]
acc = WelfordAccumulator()
for x in stream_data:
    acc.update(x)

print(f"Welford Mean: {acc.mean:.4f} | NumPy Mean: {np.mean(stream_data):.4f}")
print(f"Welford Sample Var: {acc.sample_variance:.4f} | NumPy Sample Var (ddof=1): {np.var(stream_data, ddof=1):.4f}")
```

---

## 3. Module 2: Percentiles, Quantiles & Percentile Ranks

### 3.1 What is a Percentile? (Score vs. Value)
* **Percentile Value ($P_k$):** The data value below which $k\%$ of observations fall.
  * Question: *"What score corresponds to the 75th percentile?"*
  * Function: `np.percentile(data, 75)`
* **Percentile Rank of a Score:** The percentage of scores in a distribution that are less than or equal to a given score.
  * Question: *"I scored 85 on the exam. What percentile am I?"*
  * Function: `scipy.stats.percentileofscore(data, 85, kind=...)`

---

### 3.2 Finding Percentile of Score: The 4 Calculation Kinds

When multiple identical values (ties) exist in the data, how should the percentile be computed? SciPy provides 4 distinct definitions:

Given dataset: `score = [50, 60, 70, 75, 75, 75, 75, 85, 90, 95]` ($N=10$)  
Target: $75$

```
Index:    0    1    2    3    4    5    6    7    8    9
Value:   50   60   70   75   75   75   75   85   90   95
Ranks:    1    2    3    4    5    6    7    8    9   10
                       ▲───────────────▲
                        Tied at 75
```

1. **`kind='strict'` (Strictly Less Than):**
   * Only counts observations strictly below the target ($x_i < \text{target}$).
   * Values $< 75$: $\{50, 60, 70\}$ (count = 3).
   $$\text{Percentile} = \frac{3}{10} \times 100 = 30.0\%$$

2. **`kind='weak'` (Less Than or Equal To):**
   * Counts observations less than or equal to the target ($x_i \le \text{target}$).
   * Values $\le 75$: $\{50, 60, 70, 75, 75, 75, 75\}$ (count = 7).
   $$\text{Percentile} = \frac{7}{10} \times 100 = 70.0\%$$

3. **`kind='rank'` (Average Relative Rank):**
   * Averages the 1-based ranks occupied by tied values.
   * Ranks for 75: $4, 5, 6, 7 \implies \text{Mean Rank} = \frac{4 + 5 + 6 + 7}{4} = 5.5$.
   $$\text{Percentile} = \frac{5.5}{10} \times 100 = 55.0\%$$

4. **`kind='mean'` (Midpoint of Strict and Weak):**
   $$\text{Percentile} = \frac{\text{strict} + \text{weak}}{2} = \frac{30.0 + 70.0}{2} = 50.0\%$$

```python
from scipy import stats

score = [50, 60, 70, 75, 75, 75, 75, 85, 90, 95]
target = 75

print("Strict Percentile: ", stats.percentileofscore(score, target, kind='strict')) # 30.0%
print("Weak Percentile:   ", stats.percentileofscore(score, target, kind='weak'))   # 70.0%
print("Rank Percentile:   ", stats.percentileofscore(score, target, kind='rank'))   # 55.0%
print("Mean Percentile:   ", stats.percentileofscore(score, target, kind='mean'))   # 50.0%
```

---

## 4. Module 3: Interquartile Range (IQR) & Outlier Detection

### 4.1 Quartiles ($Q_1, Q_2, Q_3$)
* **Quartiles** divide ordered data into 4 equal quarters (each containing 25% of observations):
  * **$Q_1$ (First Quartile):** $25^{\text{th}}$ percentile.
  * **$Q_2$ (Second Quartile):** $50^{\text{th}}$ percentile (The Median).
  * **$Q_3$ (Third Quartile):** $75^{\text{th}}$ percentile.
* **Interquartile Range (IQR):**
  $$\text{IQR} = Q_3 - Q_1$$
  * Measures the spread of the middle 50% of the data.
  * Completely immune to extreme outliers in the top or bottom 25%.

---

### 4.2 Manual Calculation (Tukey's / Moore & McCabe Method)
From [`O04_problem.py`](file:///d:/Engineering/CDAC_ALL_MODULES/Data%20Analytics/Day4/O04_problem.py):
Given: `prices = [2, 3, 4, 5, 6, 7, 8]` ($n=7$)

1. **Sort Data:** $[2, 3, 4, 5, 6, 7, 8]$
2. **Find Median ($Q_2$):** Middle element at index $3 \implies Q_2 = 5$.
3. **Split into Lower and Upper Halves (excluding median when $n$ is odd):**
   * Lower half: $[2, 3, 4]$
   * Upper half: $[6, 7, 8]$
4. **Compute $Q_1$ and $Q_3$ as the medians of their respective halves:**
   * $Q_1 = \text{median}([2, 3, 4]) = 3$
   * $Q_3 = \text{median}([6, 7, 8]) = 7$
5. **Calculate IQR:**
   $$\text{IQR} = Q_3 - Q_1 = 7 - 3 = 4$$

---

### 4.3 Tukey’s $1.5 \times \text{IQR}$ Boxplot Outlier Fences

```
          Inner Fence (Outlier boundary)
                │
                ▼
      ┌─────────┬──────────────┬───────────────┬─────────┐
    ──┤         │              │               │         ├──  o (Outlier)
      └─────────┴──────────────┴───────────────┴─────────┘
      ▲         ▲              ▲               ▲         ▲
      │         │              │               │         │
  Whisker Min   Q1           Median (Q2)       Q3    Whisker Max
  (Q1 - 1.5*IQR)                                     (Q3 + 1.5*IQR)
```

#### The Rules
1. **Lower Fence:** $Q_1 - 1.5 \times \text{IQR}$
2. **Upper Fence:** $Q_3 + 1.5 \times \text{IQR}$
3. **Outlier Criterion:** Any observation $x < \text{Lower Fence}$ or $x > \text{Upper Fence}$ is flagged as an outlier (drawn as individual dots/fliers in `plt.boxplot`).
4. **Extreme Outliers:** Any observation beyond $Q_3 + 3 \times \text{IQR}$ or $Q_1 - 3 \times \text{IQR}$.

---

## 5. Module 4: The 9 Hyndman-Fan Quantile Interpolation Methods

### 5.1 Why Do Excel, R, and Python Give Different Quartiles?
When running [`O04_problem.py`](file:///d:/Engineering/CDAC_ALL_MODULES/Data%20Analytics/Day4/O04_problem.py) on `prices = [2, 3, 4, 5, 6, 7, 8]`:
* **Manual split gave:** $Q_1 = 3, Q_3 = 7, \text{IQR} = 4$
* **NumPy (`method='linear'`) gave:** $Q_1 = 3.5, Q_3 = 6.5, \text{IQR} = 3.0$
* **SciPy `iqr()` gave:** $\text{IQR} = 3.0$

**Why?** Because with continuous interpolation, the virtual index for 25% is:
$$i = (n - 1) \times 0.25 = 6 \times 0.25 = 1.5$$
Index 1 is $3$, Index 2 is $4$.  
Linear interpolation at $1.5$ yields $3 + 0.5 \times (4 - 3) = 3.5$!

In 1996, statisticians **Rob J. Hyndman and Yanan Fan** published a landmark paper categorizing all sample quantile estimators across commercial software into **9 distinct methods**:

### 5.2 The 9 Hyndman & Fan Methods Matrix

| Method # | NumPy Name | Description | Used As Default By |
| :---: | :--- | :--- | :--- |
| **1** | `inverted_cdf` | Step function, no interpolation | Discontinuous |
| **2** | `averaged_inverted_cdf` | Step function with averaging at discontinuities | SAS, Discontinuous |
| **3** | `closest_observation` | Nearest integer order statistic | Nearest data point |
| **4** | `interpolated_inverted_cdf` | Linear interpolation of empirical CDF | Classical linear |
| **5** | `hazen` | Piecewise linear ($p_k = \frac{k - 0.5}{n}$) | Hydrology, Hazen |
| **6** | `weibull` | Divides by $n + 1$ ($p_k = \frac{k}{n+1}$) | **SPSS, Minitab, Excel `PERCENTILE.EXC`** |
| **7** | `linear` | Standard linear interpolation ($p_k = \frac{k - 1}{n - 1}$) | **R (default), S-Plus, Excel `PERCENTILE.INC`, NumPy (default)** |
| **8** | `median_unbiased` | Approximately median-unbiased | Recommended by Hyndman & Fan for unknown distributions |
| **9** | `normal_unbiased` | Approximately unbiased if data is Normal | Standard for normal theory |

```python
import numpy as np

prices = [2, 3, 4, 5, 6, 7, 8]
methods = ['linear', 'lower', 'higher', 'midpoint', 'nearest', 'weibull']

for m in methods:
    q1 = np.percentile(prices, 25, method=m)
    q3 = np.percentile(prices, 75, method=m)
    print(f"Method '{m:8s}': Q1={q1:.1f}, Q3={q3:.1f}, IQR={q3-q1:.1f}")
```
*Output:*
* `linear`: $Q_1=3.5, Q_3=6.5, \text{IQR}=3.0$
* `weibull`: $Q_1=3.0, Q_3=7.0, \text{IQR}=4.0$ *(Matches manual median split!)*

---

## 6. Module 5: Skewness & The 3rd Statistical Moment

### 6.1 Intuition: Asymmetry and Tail Direction
Skewness measures the lack of symmetry in a distribution:

```
        Negative Skew (Left-Skewed)           Normal (Symmetric)           Positive Skew (Right-Skewed)
              Mean < Median                      Mean = Median                    Median < Mean
                ┌─────┐                             ┌─────┐                          ┌─────┐
              ┌─┘     └─┐                         ┌─┘     └─┐                      ┌─┘     └─┐
        ─────/          \                        /           \                    /           \─────
        Long tail on LEFT                        Symmetric tails                  Long tail on RIGHT
```

* **Zero-Skewed (Symmetric):** $\text{Mean} \approx \text{Median} \approx \text{Mode}$.
* **Positive (Right-Skewed):** Extreme large values drag the mean upward:
  $$\text{Mean} > \text{Median} > \text{Mode}$$
  *(Examples: Startup salaries, wealth, housing prices, website traffic).*
* **Negative (Left-Skewed):** Extreme small values drag the mean downward:
  $$\text{Mean} < \text{Median} < \text{Mode}$$
  *(Examples: Retirement age, human lifespan, university graduation rates).*

---

### 6.2 Mathematical Formulation of Skewness

1. **$k^{\text{th}}$ Central Moment ($m_k$):**
   $$m_k = \frac{1}{n}\sum_{i=1}^n (x_i - \mu)^k$$
   * $m_1 = 0$ (Always zero around the mean)
   * $m_2 = \sigma^2$ (Variance)
   * $m_3 = \frac{1}{n}\sum (x_i - \mu)^3$ ($3^{\text{rd}}$ Central Moment)

2. **Fisher-Pearson Standardized Skewness Coefficient ($\gamma_1$):**
   $$\gamma_1 = \frac{m_3}{m_2^{3/2}} = \frac{m_3}{\sigma^3} = \frac{\frac{1}{n}\sum_{i=1}^n (x_i - \mu)^3}{\left(\frac{1}{n}\sum_{i=1}^n (x_i - \mu)^2\right)^{3/2}}$$

3. **Sample-Adjusted Unbiased Skewness ($G_1$):**
   $$G_1 = \frac{\sqrt{n(n-1)}}{n-2} \gamma_1$$

---

### 6.3 Complete Step-by-Step Derivation 1: Startup Salaries
Dataset: `salaries = [40, 45, 50, 55, 310]` ($n=5$)

#### Step 1: Compute Mean ($\mu$)
$$\mu = \frac{40 + 45 + 50 + 55 + 310}{5} = \frac{500}{5} = 100$$

#### Step 2: Compute Median
Sorted values: $[40, 45, 50, 55, 310] \implies \text{Median} = 50$.  
$\mu (100) > \text{Median} (50) \implies$ **Right-Skewed / Positively Skewed!**

#### Step 3: Compute Deviations, Squared, and Cubed Differences
| $x_i$ | Deviation $(x_i - \mu)$ | Squared $(x_i - \mu)^2$ | Cubed $(x_i - \mu)^3$ |
| :---: | :---: | :---: | :---: |
| 40 | $40 - 100 = -60$ | $(-60)^2 = 3,600$ | $(-60)^3 = -216,000$ |
| 45 | $45 - 100 = -55$ | $(-55)^2 = 3,025$ | $(-55)^3 = -166,375$ |
| 50 | $50 - 100 = -50$ | $(-50)^2 = 2,500$ | $(-50)^3 = -125,000$ |
| 55 | $55 - 100 = -45$ | $(-45)^2 = 2,025$ | $(-45)^3 = -91,125$ |
| 310 | $310 - 100 = +210$ | $(+210)^2 = 44,100$ | $(+210)^3 = +9,261,000$ |
| **Total** | $\sum = 0$ | $\sum = 55,250$ | $\sum = 8,662,500$ |

#### Step 4: Compute Moments and Skewness
* **Variance ($m_2$):** $m_2 = \frac{55,250}{5} = 11,050 \implies \sigma = \sqrt{11,050} \approx 105.11898$
* **3rd Moment ($m_3$):** $m_3 = \frac{8,662,500}{5} = 1,732,500$
* **Standardized Skewness ($\gamma_1$):**
  $$\gamma_1 = \frac{m_3}{\sigma^3} = \frac{1,732,500}{(11,050)^{1.5}} = \frac{1,732,500}{1,161,564.75} \approx \mathbf{+1.4915}$$
*SciPy verification (`stats.skew`):* $\approx +1.49$ to $+1.50$ (Heavily right-skewed).

---

### 6.4 Complete Step-by-Step Derivation 2: Retirement Ages Problem
Problem posed at the end of [`O06_skewness.py`](file:///d:/Engineering/CDAC_ALL_MODULES/Data%20Analytics/Day4/O06_skewness.py):  
`retirement_age = [35, 62, 65, 67, 71]` ($n=5$)

#### Step 1: Compute Mean
$$\mu = \frac{35 + 62 + 65 + 67 + 71}{5} = \frac{300}{5} = \mathbf{60.0}$$

#### Step 2: Compute Median
Sorted array: $[35, 62, 65, 67, 71] \implies \text{Median} = \mathbf{65.0}$.  
Since $\mu (60.0) < \text{Median} (65.0)$, this is **Left-Skewed / Negatively Skewed**!

#### Step 3: Compute Deviations, Squared, and Cubed Differences
| $x_i$ | $(x_i - \mu)$ | $(x_i - \mu)^2$ | $(x_i - \mu)^3$ |
| :---: | :---: | :---: | :---: |
| 35 | $35 - 60 = -25$ | $(-25)^2 = 625$ | $(-25)^3 = -15,625$ |
| 62 | $62 - 60 = +2$ | $2^2 = 4$ | $2^3 = +8$ |
| 65 | $65 - 60 = +5$ | $5^2 = 25$ | $5^3 = +125$ |
| 67 | $67 - 60 = +7$ | $7^2 = 49$ | $7^3 = +343$ |
| 71 | $71 - 60 = +11$ | $11^2 = 121$ | $11^3 = +1,331$ |
| **Total** | $\sum = 0$ | $\sum = 824$ | $\sum = -13,818$ |

#### Step 4: Compute Moments and Skewness
* **Variance ($m_2$):** $m_2 = \frac{824}{5} = 164.8 \implies \sigma = \sqrt{164.8} \approx 12.8374$
* **3rd Moment ($m_3$):** $m_3 = \frac{-13,818}{5} = -2,763.6$
* **Standardized Skewness ($\gamma_1$):**
  $$\gamma_1 = \frac{m_3}{\sigma^3} = \frac{-2,763.6}{(164.8)^{1.5}} = \frac{-2,763.6}{2,115.61} = \mathbf{-1.3063}$$

```python
from scipy import stats
import numpy as np

ret = np.array([35, 62, 65, 67, 71])
print(f"Mean:     {np.mean(ret):.2f}")     # 60.00
print(f"Median:   {np.median(ret):.2f}")   # 65.00
print(f"Skewness: {stats.skew(ret):.4f}")  # -1.3063
```

---

### 6.5 [Bonus Concepts] Pearson's & Bowley's Skewness

1. **Pearson's First Skewness Coefficient (Mode-based):**
   $$\text{Sk}_1 = \frac{\text{Mean} - \text{Mode}}{\sigma}$$
2. **Pearson's Second Skewness Coefficient (Median-based):**
   $$\text{Sk}_2 = \frac{3 \times (\text{Mean} - \text{Median})}{\sigma}$$
   * For the retirement age data: $\text{Sk}_2 = \frac{3 \times (60 - 65)}{12.837} = \frac{-15}{12.837} \approx -1.168$.
3. **Bowley's Quartile Skewness (Galton's Skewness):**
   * Based entirely on percentiles/quartiles; resistant to extreme outliers:
   $$\text{Sk}_{\text{Bowley}} = \frac{(Q_3 - Q_2) - (Q_2 - Q_1)}{Q_3 - Q_1} = \frac{Q_3 + Q_1 - 2 Q_2}{Q_3 - Q_1}$$
   * Ranges from $-1$ to $+1$.

---

## 7. Module 6: Industry Best Practices & Data Transformations

### 7.1 Correcting Skewness in Machine Learning Pipelines
Many predictive algorithms (Linear Regression, Logistic Regression, Neural Networks, PCA) assume normally distributed residuals or symmetric predictors. When features are heavily right-skewed, we apply non-linear transformations:

1. **Log Transformation ($x > 0$):**
   $$y = \ln(x) \quad \text{or} \quad y = \log_{10}(x) \quad \text{or} \quad y = \ln(x + 1) \; (\text{via } \texttt{np.log1p})$$
   * Compresses large values, pulling the long right tail inward.
2. **Square Root Transformation ($x \ge 0$):**
   $$y = \sqrt{x}$$
   * Milder than log transform; works well for count data (Poisson-like).
3. **Box-Cox Transformation (Strictly positive $x > 0$):**
   $$y^{(\lambda)} = \begin{cases} \frac{x^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0 \\ \ln(x) & \text{if } \lambda = 0 \end{cases}$$
   * `scipy.stats.boxcox` automatically finds the optimal $\lambda$ via maximum likelihood estimation!
4. **Yeo-Johnson Transformation:**
   * Works on zero and negative numbers.

```python
import numpy as np
from scipy import stats

right_skewed = np.array([40, 45, 50, 55, 310])
log_transformed = np.log(right_skewed)
boxcox_transformed, optimal_lambda = stats.boxcox(right_skewed)

print("Original Skewness:   ", stats.skew(right_skewed))       # ~ 1.50
print("Log Skewness:        ", stats.skew(log_transformed))    # Significantly reduced!
print("Box-Cox Skewness:    ", stats.skew(boxcox_transformed)) # Optimal symmetry!
```

---

### 7.2 Tooling Overview (from Day 4 `requirements.txt`)
In your Day 4 environment, industry-standard data analytics packages are specified:
* **`duckdb`**: Fast in-memory columnar OLAP SQL engine for sub-second analytical queries on millions of rows.
* **`polars`**: High-performance Rust-backed DataFrame library with multi-threaded lazy execution (10-100x faster than Pandas).
* **`pyspark` & `dask`**: Distributed cluster computation for massive datasets exceeding RAM.
* **`statsmodels`**: Rigorous statistical modeling (OLS regression, hypothesis tests, ANOVA, time series).
* **`scipy`**: Comprehensive numerical routines (`stats.percentileofscore`, `stats.skew`, `stats.kurtosis`, `stats.iqr`).

---

## 8. Module 7: Complete Code Reference Cheat-Sheet

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 1. Percentiles & Quantiles
data = np.array([50, 60, 70, 75, 75, 75, 75, 85, 90, 95])
q25 = np.percentile(data, 25)
q50 = np.percentile(data, 50)  # Median
q75 = np.percentile(data, 75)
iqr_val = stats.iqr(data)

# 2. Percentile Rank of a Target
strict_p = stats.percentileofscore(data, 75, kind='strict')
rank_p   = stats.percentileofscore(data, 75, kind='rank')

# 3. Skewness
skew_val = stats.skew(data)

# 4. Outlier Bounds (Tukey's Fences)
lower_fence = q25 - 1.5 * iqr_val
upper_fence = q75 + 1.5 * iqr_val
outliers = data[(data < lower_fence) | (data > upper_fence)]

# 5. Boxplot Plotting
plt.figure(figsize=(8, 3))
plt.boxplot(data, vert=False, patch_artist=True)
plt.title(f"Boxplot (IQR = {iqr_val})")
plt.xlabel("Values")
plt.grid(axis='x', alpha=0.3)
plt.show()
```

---
*Created as part of CDAC Data Analytics Day 4 Statistics Module.*
