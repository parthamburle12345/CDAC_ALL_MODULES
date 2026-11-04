# ?? Statistics for Data Analytics — Complete Learning Guide
> **Based on CDAC Data Analytics: Day5–Day8 Notebooks & Readmes**
> Covers: Data Population, Probability Distributions, Descriptive Statistics, Bivariate Analysis

---

## ?? Table of Contents

1. [Data Population & Synthetic Generation](#1-data-population--synthetic-generation)
2. [Probability Distributions — Continuous](#2-probability-distributions--continuous)
3. [Probability Distributions — Discrete](#3-probability-distributions--discrete)
4. [Probability Theory & Bayesian Concepts](#4-probability-theory--bayesian-concepts)
5. [Measures of Central Tendency](#5-measures-of-central-tendency)
6. [Measures of Dispersion / Variability](#6-measures-of-dispersion--variability)
7. [Measures of Position / Relative Standing](#7-measures-of-position--relative-standing)
8. [Measures of Shape & Distribution Geometry](#8-measures-of-shape--distribution-geometry)
9. [Bivariate Relationships — Covariance & Pearson Correlation](#9-bivariate-relationships--covariance--pearson-correlation)
10. [Bivariate Relationships — Spearman & Kendall Rank Correlation](#10-bivariate-relationships--spearman--kendall-rank-correlation)
11. [SciPy & NumPy Statistical Function Reference](#11-scipy--numpy-statistical-function-reference)
12. [Quick Summary Matrix](#12-quick-summary-matrix)
13. [Key Concepts Q&A](#13-key-concepts-qa)
14. [Python Imports Cheat Sheet](#14-python-imports-cheat-sheet)

---

## 1. Data Population & Synthetic Generation

### What is it?
Synthetic data generation is the process of **creating controlled, reproducible datasets** from mathematical models. Essential for:
- Unit testing pipelines
- Monte Carlo simulation
- ML benchmark testing
- Stress-testing algorithms against known statistical properties

### Where is it used?
- Machine learning model validation
- Statistical simulation research
- Signal processing / sensor modeling
- Algorithm benchmarking

---

### 1.1 Deterministic Domain & Grid Generators

| Function | Formula | Purpose |
|---|---|---|
| `np.linspace(a, b, N)` | N evenly spaced points | Equally spaced domain axis |
| `np.logspace(a, b, N)` | Log-scale spacing | Log-scale grids (learning rates) |
| `np.geomspace(a, b, N)` | Geometric progression | Ratio-based spacing |
| `np.arange(a, b, step)` | Step-based range | Integer/float range |
| `np.meshgrid(x, y)` | 2D coordinate matrices | Loss surfaces, heatmaps |

**Visualization:** Line plots, surface plots, heatmaps

---

### 1.2 Functional & Noisy Signal Population

| Signal Type | Code Example | Use Case |
|---|---|---|
| Additive Noisy Sine | `y = sin(x) + N(0, 0.1)` | Sensor noise modeling |
| Polynomial + Error | `y = 3.5*x**2 - 2*x + 5 + N(0, 5)` | Regression benchmarks |
| Random Walk | `np.cumsum(N(0, 1, 1000))` | Time-series, stock simulation |

**Visualization:** Line plots, scatter plots with noise overlay

---

## 2. Probability Distributions — Continuous

### What is it?
Continuous probability distributions model **real-valued random variables** (measurements, times, financial returns, physical quantities).

### Where is it used?
- Modeling measurement errors (Normal)
- Reliability analysis (Weibull, Exponential)
- Financial modeling (Log-Normal)
- Bayesian priors (Beta)
- Hypothesis testing (t, chi-squared, F)

---

### 2.1 Normal (Gaussian) Distribution

```
f(x) = (1 / (sigma * sqrt(2*pi))) * exp(-0.5 * ((x - mu) / sigma)^2)
```

| Property | Value |
|---|---|
| Parameters | Mean mu, Std. Dev sigma |
| Shape | Bell-shaped, symmetric |
| Mean | mu |
| Variance | sigma^2 |

```python
rng.normal(loc=40.0, scale=10.0, size=1000)
```

**Visualization:** Histogram + KDE (bell curve overlay), Q-Q Plot

---

### 2.2 Uniform Distribution

```
f(x) = 1 / (b - a)  for x in [a, b]
```

| Property | Value |
|---|---|
| Mean | (a + b) / 2 |
| Variance | (b - a)^2 / 12 |

```python
rng.uniform(low=10.0, high=50.0, size=1000)
```

**Visualization:** Flat histogram, CDF staircase plot

---

### 2.3 Exponential Distribution

```
f(x) = lambda * exp(-lambda * x)  for x >= 0
```

| Property | Value |
|---|---|
| Mean | 1 / lambda |
| Key property | Memoryless |

```python
rng.exponential(scale=1.0, size=1000)
```

**Use case:** Time between events in a Poisson process (call center arrivals, radioactive decay)

---

### 2.4 Beta Distribution

```
f(x) = x^(alpha-1) * (1-x)^(beta-1) / B(alpha, beta)  for x in [0, 1]
```

```python
rng.beta(a=0.5, b=0.5, size=1000)
```

**Use case:** Bayesian prior modeling, probability/ratio estimation

---

### 2.5 Log-Normal Distribution

```
f(x) = (1 / (x * sigma * sqrt(2*pi))) * exp(-(ln(x) - mu)^2 / (2*sigma^2))
```

```python
rng.lognormal(mean=0.0, sigma=1.0, size=1000)
```

**Use case:** Income distributions, stock prices, biological measurements

---

### 2.6 Student's t-Distribution

```
f(t) = Gamma((nu+1)/2) / (sqrt(nu*pi) * Gamma(nu/2)) * (1 + t^2/nu)^(-(nu+1)/2)
```

| Property | Value |
|---|---|
| Parameter | Degrees of freedom nu |
| Shape | Bell-shaped, heavier tails than Normal |

```python
rng.standard_t(df=10, size=1000)
```

**Use case:** Small-sample inference, hypothesis testing (t-tests)

---

### 2.7 Chi-Square Distribution

```
chi2 = Z1^2 + Z2^2 + ... + Zk^2  where Zi ~ N(0,1)
```

```python
rng.chisquare(df=3, size=1000)
```

**Use case:** Goodness-of-fit tests, independence tests in contingency tables

---

### 2.8 F-Distribution

```
F = (chi2_d1 / d1) / (chi2_d2 / d2)
```

```python
rng.f(dfnum=5, dfden=20, size=1000)
```

**Use case:** ANOVA, comparing variance ratios between two populations

---

### 2.9 Gamma, Weibull, Pareto

| Distribution | Use Case | Visualization |
|---|---|---|
| Gamma | Queuing delays, lifetime data | Right-skewed histogram |
| Weibull | Reliability engineering, failure rates | Hazard function plot |
| Pareto | 80/20 power-law phenomena | Log-log scale plot |

---

## 3. Probability Distributions — Discrete

### What is it?
Discrete distributions model **countable outcomes** — successes, failures, event counts.

---

### 3.1 Bernoulli / Binary

```
P(X = k) = p^k * (1-p)^(1-k)  for k in {0, 1}
```

```python
rng.binomial(n=1, p=0.3, size=1000)
```

**Use case:** Single binary trial (pass/fail, click/no-click)

---

### 3.2 Binomial Distribution

```
P(X = k) = C(n,k) * p^k * (1-p)^(n-k)
```

| Property | Value |
|---|---|
| Mean | n * p |
| Variance | n * p * (1-p) |

```python
rng.binomial(n=10, p=0.5, size=1000)
```

**Use case:** Number of successes in n independent coin flips

---

### 3.3 Poisson Distribution

```
P(X = k) = (lambda^k * exp(-lambda)) / k!
```

| Property | Value |
|---|---|
| Mean | lambda |
| Variance | lambda |

```python
rng.poisson(lam=5.0, size=1000)
```

**Use case:** Event counts per fixed time/space interval

---

### 3.4 Geometric, Negative Binomial, Hypergeometric

| Distribution | Formula | Use Case |
|---|---|---|
| Geometric | P(k) = (1-p)^(k-1) * p | Trials until first success |
| Negative Binomial | Failures before n-th success | Overdispersed count data |
| Hypergeometric | C(K,k)*C(N-K,n-k)/C(N,n) | Sampling WITHOUT replacement |

---

## 4. Probability Theory & Bayesian Concepts

### 4.1 Classical Probability

```
P(E) = |E| / |Omega|
```

Where Omega = sample space, E = event.

```python
import itertools
omega = list(itertools.product(range(1, 7), repeat=2))  # Dice rolls
```

---

### 4.2 Joint, Marginal & Conditional Probability

| Concept | Formula |
|---|---|
| Joint Probability | P(A and B) = P(A | B) * P(B) |
| Marginal Probability | P(A) = Sum_B P(A, B) |
| Conditional Probability | P(A | B) = P(A and B) / P(B) |

```python
pd.crosstab(df['Category'], df['Tier'], normalize=True, margins=True)
```

**Visualization:** Contingency tables, heatmaps

---

### 4.3 Bayes' Theorem

```
P(State | Evidence) = P(Evidence | State) * P(State) / P(Evidence)
```

Or:

```
P(H | D) = P(D | H) * P(H) / P(D)
```

| Term | Meaning |
|---|---|
| P(H) | Prior probability of hypothesis |
| P(D | H) | Likelihood of data given hypothesis |
| P(H | D) | Posterior probability (updated belief) |
| P(D) | Evidence (normalizing constant) |

**Where used:**
- Spam classification (Naive Bayes)
- Medical diagnosis
- A/B testing posterior inference

**Visualization:** Prior vs Posterior distribution plots

---

### 4.4 Bootstrap Resampling

Generating empirical distributions by sampling **with replacement**:

```python
bootstrap_samples = rng.choice(data, size=(1000, len(data)), replace=True)
bootstrap_means = bootstrap_samples.mean(axis=1)
```

**Where used:** Confidence intervals without distributional assumptions

**Visualization:** Histogram of bootstrap statistic with confidence bounds

---

## 5. Measures of Central Tendency

### What is it?
These measures quantify the **central or typical value** around which the data clusters.

### Where is it used?
- Summarizing datasets
- Comparing populations
- Feature engineering in ML

---

### 5.1 Arithmetic Mean

```
x_bar = (1/n) * sum(xi)
```

| Property | Detail |
|---|---|
| Robust to outliers? | NO — 0% breakdown point |
| When NOT to use | Skewed data, outlier-heavy datasets |

```python
np.mean(x)
```

---

### 5.2 Median

```
Median = x_((n+1)/2)  for odd n
       = (x_(n/2) + x_(n/2+1)) / 2  for even n
```

| Property | Detail |
|---|---|
| Robust to outliers? | YES — 50% breakdown point |
| Best for | Skewed distributions (income, house prices) |

```python
np.median(x)
```

---

### 5.3 Mode

```
Mode = argmax_x Frequency(x)
```

| Property | Detail |
|---|---|
| Robust? | YES |
| Note | Can be multimodal or non-existent |

**Visualization:** Histogram (peak = mode)

---

### 5.4 Geometric Mean

```
G = (x1 * x2 * ... * xn)^(1/n) = exp((1/n) * sum(ln(xi)))
```

| Property | Detail |
|---|---|
| Constraint | xi > 0 always required |
| Best for | Growth rates, ratios, compounding returns |

```python
from scipy.stats import gmean
gmean(x)
```

---

### 5.5 Harmonic Mean

```
H = n / sum(1/xi)
```

| Property | Detail |
|---|---|
| Constraint | xi > 0, undefined if xi = 0 |
| Best for | Rates & ratios (average speed, F1 score) |

```python
from scipy.stats import hmean
hmean(x)
```

---

### 5.6 Trimmed Mean

```
x_alpha = (1/(n-2k)) * sum_{i=k+1}^{n-k} x_(i)  where k = floor(n*alpha)
```

Discards proportion alpha from each tail before computing the mean.

```python
from scipy.stats import trim_mean
trim_mean(x, proportiontocut=0.1)
```

---

### 5.7 Winsorized Mean

Replaces extreme values instead of removing them — preserves sample size n.

```python
from scipy.stats import mstats
mstats.winsorize(x, limits=[0.05, 0.05]).mean()
```

---

### Visualization for Central Tendency
- Histogram with vertical lines marking mean, median, mode
- Box plot showing median and quartiles
- Strip plot / rug plot alongside central markers

---

## 6. Measures of Dispersion / Variability

### What is it?
Measures how **spread out** or **scattered** the data is around the center.

### Where is it used?
- Risk assessment (finance, quality control)
- Feature scaling in ML
- Comparing dataset variability

---

### 6.1 Range

```
R = max(X) - min(X)
```

| Property | Detail |
|---|---|
| Robust? | NO — 0% breakdown |
| Problem | Sensitive to one outlier |

---

### 6.2 Interquartile Range (IQR)

```
IQR = Q3 - Q1
```

| Property | Detail |
|---|---|
| Robust? | YES — 25% breakdown |
| Covers | Middle 50% of data |

```python
from scipy.stats import iqr
iqr(x)
```

**Visualization:** Box plot (the box IS the IQR)

---

### 6.3 Variance

```
s^2 = (1/(n-1)) * sum((xi - x_bar)^2)   [sample]
sigma^2 = (1/N) * sum((xi - mu)^2)       [population]
```

> **Note:** Use ddof=1 for sample variance (Bessel's correction)

```python
np.var(x, ddof=1)   # sample variance
np.var(x, ddof=0)   # population variance
```

---

### 6.4 Standard Deviation

```
s = sqrt((1/(n-1)) * sum((xi - x_bar)^2))
```

Same unit as the data — most interpretable spread measure.

```python
np.std(x, ddof=1)
```

**Visualization:** Error bars, shaded bands on line plots

---

### 6.5 Mean Absolute Deviation (MAD_mean)

```
MAD_mean = (1/n) * sum(|xi - x_bar|)
```

Less sensitive to outliers than variance (no squaring).

---

### 6.6 Median Absolute Deviation (MAD_median)

```
MAD_median = median(|xi - x_tilde|)
```

| Property | Detail |
|---|---|
| Robust? | YES — 50% breakdown |
| To estimate sigma | Multiply by approximately 1.4826 |

```python
from scipy.stats import median_abs_deviation
median_abs_deviation(x)
```

---

### 6.7 Coefficient of Variation (CV)

```
CV = (s / x_bar) * 100%
```

| Property | Detail |
|---|---|
| Dimensionless? | YES |
| Use | Compare spread across datasets with different units/scales |
| Caution | Undefined when x_bar approaches 0 |

---

### Visualizations for Dispersion
- Box plot — shows IQR, range, outliers
- Violin plot — shows full distribution shape
- Error bar plots — shows standard deviation
- Histogram with std bands — visual spread around mean

---

## 7. Measures of Position / Relative Standing

### What is it?
Measures that quantify **where a value sits** within a distribution relative to others.

### Where is it used?
- Academic grading (percentile ranks)
- Standardization for ML (Z-score / StandardScaler)
- Outlier detection

---

### 7.1 Quantiles & Percentiles

For p in (0,1), the p-th quantile q_p satisfies:

```
P(X <= q_p) >= p  AND  P(X >= q_p) >= 1 - p
```

| Division | Notation |
|---|---|
| Quartiles | Q1 = 25th, Q2 = 50th (Median), Q3 = 75th percentile |
| Deciles | Dk = k*10th percentile |

```python
np.percentile(x, [25, 50, 75])   # Q1, Q2, Q3
np.quantile(x, 0.9)               # 90th percentile
```

**Visualization:** Box plot, Q-Q plot

---

### 7.2 Z-Score (Standardized Score)

```
zi = (xi - x_bar) / s
```

| Value | Interpretation |
|---|---|
| z = 0 | At the mean |
| z = +2 | 2 standard deviations above mean |
| z > 3 or z < -3 | Potential outlier |

```python
from scipy.stats import zscore
zscore(x)
```

**Visualization:** Standardized histogram with +/-1, +/-2, +/-3 sigma bands

---

### 7.3 Percentile Rank

```
PR_x = ((count(xi < x) + 0.5 * count(xi = x)) / n) * 100%
```

**Example:** "This student scored in the 82nd percentile" = scored higher than 82% of students

---

## 8. Measures of Shape & Distribution Geometry

### What is it?
These measures quantify **asymmetry** and **tail behavior** relative to a Normal distribution.

### Where is it used?
- Testing normality assumptions for statistical tests
- Financial return distribution analysis (fat tails = Black Swan events)
- Distribution fitting

---

### 8.1 Statistical Moments

| Moment | Formula | Meaning |
|---|---|---|
| 1st Raw Moment | mu'_1 = (1/n)*sum(xi) | = Mean |
| 1st Central Moment | m1 = 0 | Always zero |
| 2nd Central Moment | m2 = (1/n)*sum((xi-x_bar)^2) | = Population Variance |
| 3rd Central Moment | m3 = (1/n)*sum((xi-x_bar)^3) | Unstandardized Skewness |
| 4th Central Moment | m4 = (1/n)*sum((xi-x_bar)^4) | Unstandardized Kurtosis |

Standardized Moment: alpha_r = m_r / s^r

---

### 8.2 Skewness

The 3rd standardized moment — measures directional asymmetry around the mean.

```
g1 = m3 / m2^(3/2)
```

Adjusted Fisher-Pearson Skewness (used by Python/pandas):

```
G1 = (sqrt(n*(n-1)) / (n-2)) * g1
```

| Value | Shape |
|---|---|
| G1 = 0 | Symmetric (Normal) |
| G1 > 0 | Right-skewed (tail to the right, mean > median) |
| G1 < 0 | Left-skewed (tail to the left, mean < median) |

```python
from scipy.stats import skew
skew(x)
```

**Visualization:**
- Histogram overlay showing tail direction
- Comparison of mean vs. median position

---

### 8.3 Kurtosis

The 4th standardized moment — measures tail heaviness relative to Normal.

Excess Kurtosis (Normal = 0):

```
g2 = m4 / m2^2 - 3
```

Sample Unbiased Excess Kurtosis:

```
G2 = ((n-1) / ((n-2)*(n-3))) * ((n+1)*g2 + 6)
```

| Value | Shape | Name |
|---|---|---|
| G2 = 0 | Normal tail weight | Mesokurtic |
| G2 > 0 | Heavy tails, sharp peak | Leptokurtic |
| G2 < 0 | Light tails, flat peak | Platykurtic |

```python
from scipy.stats import kurtosis
kurtosis(x)              # excess kurtosis
kurtosis(x, fisher=False)  # raw kurtosis (Normal = 3)
```

**Visualization:**
- Overlaid density plots comparing distributions with different kurtosis
- Q-Q plot (deviation from straight line indicates kurtosis)

---

### 8.4 Pearson's Median Skewness (Non-parametric)

```
Pearson Skew = 3 * (x_bar - median) / s
```

A quick, robust approximation bounded roughly in [-3, +3].

---

## 9. Bivariate Relationships — Covariance & Pearson Correlation

### What is it?
Measures the **linear relationship** between two variables.

### Where is it used?
- Feature selection in ML (remove highly correlated redundant features)
- Portfolio risk matrix (finance)
- Principal Component Analysis (PCA) preprocessing
- A/B test analysis

---

### 9.1 Sample Covariance

```
Cov(X, Y) = s_xy = (1/(n-1)) * sum((xi - x_bar)(yi - y_bar))
```

| Value | Meaning |
|---|---|
| s_xy > 0 | X and Y move together (positive relationship) |
| s_xy < 0 | X and Y move opposite (negative relationship) |
| s_xy = 0 | No linear relationship |

> **Problem:** Covariance is unit-dependent — hard to compare across datasets!

**Step-by-Step Example:**

| Student | Hours (X) | Score (Y) | (x-x_bar) | (y-y_bar) | Product |
|---|---|---|---|---|---|
| 1 | 2 | 50 | -2 | -20 | 40 |
| 2 | 4 | 70 | 0 | 0 | 0 |
| 3 | 6 | 90 | 2 | 20 | 40 |

```
Cov(X, Y) = 80 / (3-1) = 40.0
```

```python
np.cov(x, y, ddof=1)   # returns covariance matrix
np.cov(x, y)[0, 1]     # off-diagonal = Cov(X,Y)
```

**Visualization:** Scatter plot with regression line, Covariance matrix heatmap

---

### 9.2 Pearson Correlation Coefficient (r)

Standardizes covariance to a unit-free range [-1, +1]:

```
r = Cov(X,Y) / (s_X * s_Y)
  = sum((xi-x_bar)(yi-y_bar)) / sqrt(sum((xi-x_bar)^2) * sum((yi-y_bar)^2))
```

| Value | Interpretation |
|---|---|
| r = +1.0 | Perfect positive linear correlation |
| r = +0.7 | Strong positive |
| r = +0.3 | Weak positive |
| r = 0.0 | No linear correlation |
| r = -0.3 | Weak negative |
| r = -0.7 | Strong negative |
| r = -1.0 | Perfect negative linear correlation |

> **Linearity Assumption:** Pearson only captures linear relationships. Strong nonlinear relationships may show r near 0.

```python
from scipy.stats import pearsonr
r, p_value = pearsonr(x, y)
```

**Visualization:**
- Scatter plot grid for multiple variables
- Correlation heatmap (Seaborn heatmap)
- Annotated correlation matrix

---

## 10. Bivariate Relationships — Spearman & Kendall Rank Correlation

### What is it?
**Rank-based correlation** measures that capture **monotonic** (not just linear) relationships and are robust to outliers.

### Where is it used?
- Ordinal data (survey ratings, rankings)
- Data with outliers that would distort Pearson's r
- Non-linear monotonic relationships
- Small samples

---

### 10.1 Spearman Rank Correlation (rho)

How it works: Convert raw values to ranks, then apply Pearson on ranks.

```
r_s = rho = 1 - (6 * sum(di^2)) / (n * (n^2 - 1))
```

Where di = Rank(xi) - Rank(yi) is the rank difference.

**Step-by-Step Example:**

| Customer | Tenure (X) | Spend (Y) | Rank(X) | Rank(Y) | di | di^2 |
|---|---|---|---|---|---|---|
| 1 | 5 | 100 | 1 | 1 | 0 | 0 |
| 2 | 50 | 5000 | 3 | 3 | 0 | 0 |
| 3 | 12 | 250 | 2 | 2 | 0 | 0 |
| 4 | 100 | 15000 | 4 | 4 | 0 | 0 |

```
r_s = 1 - (6 * 0) / (4 * (16 - 1)) = 1.0  (perfect monotonic)
```

```python
from scipy.stats import spearmanr
rho, p_value = spearmanr(x, y)

# With pandas:
df.corr(method='spearman')
```

---

### 10.2 Kendall's Tau

Measures **pairwise concordance** (agreement in ordering of pairs).

```
tau = (n_c - n_d) / (0.5 * n * (n-1))
```

Where:
- n_c = number of concordant pairs (both variables agree in order)
- n_d = number of discordant pairs (variables disagree in order)

| Range | Interpretation |
|---|---|
| tau = +1 | All pairs concordant (perfect monotonic) |
| tau = -1 | All pairs discordant |
| tau = 0 | No monotonic relationship |

```python
from scipy.stats import kendalltau
tau, p_value = kendalltau(x, y)
```

---

### Comparison: Pearson vs Spearman vs Kendall

| Feature | Pearson (r) | Spearman (rho) | Kendall (tau) |
|---|---|---|---|
| Measures | Linear relationship | Monotonic relationship | Pairwise concordance |
| Robust to outliers | NO | YES | YES |
| Data type | Continuous | Ordinal/Continuous | Ordinal/Continuous |
| Best for | Linear, normal data | Non-linear monotonic | Small samples, tied ranks |
| Range | [-1, +1] | [-1, +1] | [-1, +1] |

---

### Visualizations for Correlation
- Scatter plot with regression line — shows linear trend
- Scatter plot matrix (Seaborn pairplot) — all pairwise relationships
- Correlation heatmap — color-coded correlation matrix
- Residual plot — checks linearity assumption

---

## 11. SciPy & NumPy Statistical Function Reference

### SciPy Distribution Methods

| Method | Meaning | Formula |
|---|---|---|
| `pdf(x)` | Probability Density Function | f(x) for continuous |
| `pmf(k)` | Probability Mass Function | P(X=k) for discrete |
| `cdf(x)` | Cumulative Distribution | F(x) = P(X <= x) |
| `sf(x)` | Survival Function | 1 - F(x) = P(X > x) |
| `ppf(q)` | Percentile Point Function | F^-1(q) (Inverse CDF) |
| `isf(q)` | Inverse Survival Function | S^-1(q) |
| `rvs(size)` | Random Variates Sampling | Generates samples |

### NumPy Descriptive Functions

```python
np.mean(x)                     # arithmetic mean
np.median(x)                   # median
np.std(x, ddof=1)              # sample standard deviation
np.var(x, ddof=1)              # sample variance
np.percentile(x, q)            # empirical quantiles
np.cov(m)                      # covariance matrix

# SciPy extras
from scipy.stats import pearsonr, spearmanr, kendalltau
from scipy.stats import skew, kurtosis
from scipy.stats import iqr, median_abs_deviation
```

---

## 12. Quick Summary Matrix

| Measure | Formula (simplified) | Robust? | Breakdown | Best For |
|---|---|---|---|---|
| **Mean** | (1/n)*sum(xi) | NO | 0% | Symmetric, normal data |
| **Median** | Middle value | YES | 50% | Skewed data |
| **Mode** | Most frequent value | YES | Variable | Categorical, multimodal |
| **Geometric Mean** | (prod xi)^(1/n) | NO | 0% | Growth rates (xi > 0) |
| **Harmonic Mean** | n / sum(1/xi) | NO | 0% | Rates, ratios |
| **Trimmed Mean** | Mean after removing alpha tails | YES | alpha*100% | Moderate outlier resistance |
| **Winsorized Mean** | Replace extremes | YES | alpha*100% | Same n, outlier control |
| **Range** | max - min | NO | 0% | Quick spread estimate |
| **IQR** | Q3 - Q1 | YES | 25% | Skewed distributions |
| **Variance / Std Dev** | (1/(n-1))*sum((xi-x_bar)^2) | NO | 0% | Normally distributed data |
| **MAD (mean)** | (1/n)*sum(|xi - x_bar|) | NO | 0% | L1 norm spread |
| **MAD (median)** | median(|xi - x_tilde|) | YES | 50% | Robust spread estimate |
| **CV** | (s / x_bar) * 100% | NO | 0% | Comparing across scales |
| **Z-Score** | (xi - x_bar) / s | NO | 0% | Standardization, outlier detection |
| **Skewness (G1)** | 3rd standardized moment | NO | 0% | Asymmetry measurement |
| **Kurtosis (G2)** | 4th standardized moment - 3 | NO | 0% | Tail weight vs. Normal |
| **Covariance** | (1/(n-1))*sum((x-x_bar)(y-y_bar)) | NO | 0% | Joint variability (unit-dependent) |
| **Pearson r** | Cov / (s_X * s_Y) | NO | 0% | Linear relationships |
| **Spearman rho** | Pearson on ranks | YES | Variable | Monotonic, ordinal data |
| **Kendall tau** | Concordant vs discordant pairs | YES | Variable | Small samples, tied data |

---

## 13. Key Concepts Q&A

### Q: When should I use Median instead of Mean?
**A:** Use Median when the data is **skewed** or has **outliers** (e.g., income distributions, house prices). The median is robust — a single extreme outlier won't shift it.

### Q: What does a positive skewness mean?
**A:** The distribution has a **longer right tail**. Most data clusters on the left. Mean > Median. Example: Income data.

### Q: What does high kurtosis (Leptokurtic) mean?
**A:** The distribution has **heavier tails** than Normal — extreme values are more likely. Important in finance (tail risk, Black Swan events).

### Q: What's the difference between Covariance and Pearson Correlation?
**A:** Covariance measures the direction of linear relationship but is **scale-dependent**. Pearson correlation **standardizes** covariance to [-1, +1], making it interpretable regardless of units.

### Q: When to use Spearman instead of Pearson?
**A:** Use Spearman when:
1. Data is ordinal (ranks, survey responses)
2. Relationship is monotonic but **not necessarily linear**
3. Data has significant **outliers**

### Q: What is the Normal distribution's role in statistics?
**A:** It's the **Central Limit Theorem** distribution — the average of any sufficiently large random sample approximates a Normal distribution. This is why many statistical tests assume normality.

### Q: What is Bootstrap Resampling?
**A:** A technique for estimating uncertainty (confidence intervals) by repeatedly sampling your own dataset **with replacement** — no distributional assumptions needed.

### Q: What's the difference between sample and population variance?
**A:** Sample variance uses (n-1) as denominator (Bessel's correction) to give an unbiased estimate when you only have a sample. Population variance uses N (the total population size).

### Q: Why is IQR preferred over Range for outlier detection?
**A:** Range uses only the min and max (both extreme values), so a single outlier completely distorts it. IQR uses the 25th and 75th percentiles, which are robust — up to 25% of extreme values can be outliers without affecting IQR.

### Q: What does Kendall's tau measure compared to Spearman?
**A:** Spearman measures the correlation of rank differences (similar to Pearson on ranks). Kendall counts concordant vs discordant pairs, making it more suitable for **small samples** and data with **many tied ranks**.

---

## 14. Python Imports Cheat Sheet

```python
# Core
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

# Data Generation — Modern NumPy API
rng = np.random.default_rng(seed=42)

# Continuous Distributions (scipy.stats)
from scipy.stats import norm, uniform, expon, gamma, beta
from scipy.stats import t, chi2, f, weibull_min, lognorm

# Descriptive Statistics
from scipy.stats import gmean, hmean, trim_mean
from scipy.stats import skew, kurtosis
from scipy.stats import iqr, median_abs_deviation
from scipy.stats import zscore

# Correlation
from scipy.stats import pearsonr, spearmanr, kendalltau

# Advanced Sampling
from scipy.stats import gaussian_kde, truncnorm

# Sklearn synthetic data
from sklearn.datasets import make_classification, make_regression, make_blobs
```

---

> **Source Files:**
> - `Day5/data_population/` — Deterministic grids, noisy signals, distributions
> - `Day6/01_data_population/` — Bayesian & conditional sampling
> - `Day6/02_statistical_measure/` — Measures of central tendency
> - `Day7/02_statistical_measure/` — Dispersion, position, shape measures
> - `Day8/03_bivariate_relationships/` — Covariance, Pearson, Spearman, Kendall
