# Comprehensive Statistics Master Study Guide & Code Analysis
> **Module:** Data Analytics - Statistics (Day 3 / `O3Statistics`)  
> **Target Audience:** Data Analyst / Data Scientist / Machine Learning Engineer  
> **Author:** Antigravity Coding Assistant  
> **Date:** September 2026

---

## Table of Contents
1. [Learning Sequence Roadmap](#1-learning-sequence-roadmap)
2. [Phase 1: Measures of Central Tendency](#2-phase-1-measures-of-central-tendency)
   - 2.1 Arithmetic Mean ($\mu, \bar{x}$)
   - 2.2 Median ($Q_2$)
   - 2.3 Mode
   - 2.4 Trimmed Mean ($\bar{x}_{\alpha}$)
   - 2.5 Supplementary Means: Weighted, Geometric, and Harmonic Means
3. [Phase 2: Measures of Dispersion (Variability & Spread)](#3-phase-2-measures-of-dispersion-variability--spread)
   - 3.1 Range
   - 3.2 Population Variance vs. Sample Variance & Bessel's Correction ($ddof$)
   - 3.3 Standard Deviation ($\sigma, s$) - First-Principles Derivation
   - 3.4 Percentiles, Quartiles & Interquartile Range (IQR) with Boxplot Outlier Rules
   - 3.5 Coefficient of Variation (CV) & MAD
4. [Phase 3: Measures of Shape & Statistical Moments](#4-phase-3-measures-of-shape--statistical-moments)
   - 4.1 The 4 Moments of a Distribution
   - 4.2 Skewness (Symmetry)
   - 4.3 Kurtosis (Tail Fatness & Peakedness)
5. [Phase 4: Probability Theory Foundations](#5-phase-4-probability-theory-foundations)
   - 5.1 Sample Space, Events, and Classical Probability
   - 5.2 Discrete vs. Continuous Random Variables
   - 5.3 PMF vs. PDF vs. CDF
6. [Phase 5: Probability Distributions (Formulas, Visuals & Code)](#6-phase-5-probability-distributions-formulas-visuals--code)
   - 6.1 Discrete Uniform Distribution (Rolling 1 Die)
   - 6.2 Triangular Distribution (Sum of 2 Dice)
   - 6.3 Continuous Uniform Distribution
   - 6.4 Normal / Gaussian Distribution & The 68-95-99.7 Empirical Rule
   - 6.5 Binomial Distribution (Coin Flips, Defect Counting)
   - 6.6 Exponential Distribution (Time-to-Event Modeling)
   - 6.7 Poisson Distribution (Count of Occurrences over Fixed Interval)
7. [Phase 6: Bridging to Inferential Statistics](#7-phase-6-bridging-to-inferential-statistics)
   - 7.1 The Central Limit Theorem (CLT)
   - 7.2 Standard Error of the Mean (SEM)
   - 7.3 Covariance vs. Correlation (Pearson vs. Spearman)
8. [Phase 7: Python Library Comparison & Critical Gotchas](#8-phase-7-python-library-comparison--critical-gotchas)
   - 8.1 NumPy vs. SciPy vs. Python `statistics` vs. Pandas
   - 8.2 The $ddof$ Default Trap
   - 8.3 Pseudorandom Number Generation & Reproducibility (`seed`)

---

## 1. Learning Sequence Roadmap

To master data analytics, concepts must be approached in a systematic order:

```
[ Raw Data / Observations ]
         │
         ▼
[ 1. Central Tendency ] ──► (Where is the center? Mean, Median, Mode, Trimmed Mean)
         │
         ▼
[ 2. Dispersion & Spread ] ──► (How spread out is it? Range, Variance, Std Dev, IQR)
         │
         ▼
[ 3. Shape & Moments ] ──► (Is it lopsided or fat-tailed? Skewness, Kurtosis)
         │
         ▼
[ 4. Probability Foundations ] ──► (How do random events behave? Random Variables, PMF, PDF, CDF)
         │
         ▼
[ 5. Theoretical Distributions ] ──► (Uniform, Normal, Binomial, Exponential, Poisson)
         │
         ▼
[ 6. Inferential Bridge ] ──► (CLT, Standard Error, Covariance, Correlation)
```

---

## 2. Phase 1: Measures of Central Tendency

Central tendency identifies a single summary score that serves as the representative midpoint of an entire distribution.

### 2.1 Arithmetic Mean ($\mu, \bar{x}$)

#### Mathematical Formulation
For a population of size $N$:
$$\mu = \frac{1}{N} \sum_{i=1}^{N} x_i$$

For a sample of size $n$:
$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

#### Mathematical Optimization Property
The arithmetic mean is the **unique scalar $c$ that minimizes the sum of squared deviations (L2 Norm)**:
$$\arg\min_{c} \sum_{i=1}^{n} (x_i - c)^2 = \bar{x}$$

#### Breakdown Point & Vulnerability
* **Breakdown Point:** **$0\%$**. 
* A single arbitrary outlier ($x_i \to \infty$) causes $\bar{x} \to \infty$. It has zero robustness against extreme values.

---

### 2.2 Median ($Q_2$)

#### Mathematical Formulation
Sort the sample in ascending order: $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$.

$$\text{Median}(X) = \begin{cases} 
X_{\left(\frac{n+1}{2}\right)} & \text{if } n \text{ is odd} \\ 
\frac{X_{\left(\frac{n}{2}\right)} + X_{\left(\frac{n}{2} + 1\right)}}{2} & \text{if } n \text{ is even} 
\end{cases}$$

#### Mathematical Optimization Property
The median is the **scalar $c$ that minimizes the sum of absolute deviations (L1 Norm)**:
$$\arg\min_{c} \sum_{i=1}^{n} |x_i - c| = \text{Median}(X)$$

#### Breakdown Point & Vulnerability
* **Breakdown Point:** **$50\%$**.
* Up to half the sample can be corrupted with extreme noise before the median becomes unbounded. It is **robust** to outliers (ideal for income distributions, house prices, etc.).

---

### 2.3 Mode

#### Definition
The value(s) appearing with the highest frequency in a discrete dataset or the peak of the probability density function for a continuous dataset.
* **Unimodal:** Exactly 1 peak.
* **Bimodal:** 2 distinct peaks.
* **Multimodal:** More than 2 peaks.

---

### 2.4 Trimmed Mean ($\bar{x}_{\alpha}$)

#### Definition & Formula
Removes a proportion $\alpha$ (e.g., $10\% = 0.10$) from both the lower and upper tails of sorted data before computing the arithmetic mean:

$$\bar{x}_{\alpha} = \frac{1}{n - 2k} \sum_{i=k+1}^{n-k} X_{(i)} \quad \text{where } k = \lfloor n\alpha \rfloor$$

It strikes a compromise: keeps the efficiency of the mean while inheriting the robustness of the median.

---

### 2.5 Supplementary Means (Added Concepts)

1. **Weighted Mean:** Used when data points have unequal significance or weights $w_i$:
   $$\bar{x}_w = \frac{\sum_{i=1}^n w_i x_i}{\sum_{i=1}^n w_i}$$
2. **Geometric Mean:** Used for multiplicative processes, compounding growth rates, and financial returns:
   $$GM = \left( \prod_{i=1}^n x_i \right)^{\frac{1}{n}} = \exp\left( \frac{1}{n} \sum_{i=1}^n \ln(x_i) \right)$$
3. **Harmonic Mean:** Used for rates, speed, and ratios (e.g., F1-Score in machine learning):
   $$HM = \frac{n}{\sum_{i=1}^n \frac{1}{x_i}}$$
   * **Inequality relationship:** $HM \le GM \le \bar{x}$ (for positive numbers).

---

### Code Implementation: Central Tendency & Breakdown Point Simulation

```python
import numpy as np
import scipy.stats as stats
from collections import Counter

# 1. Reproducibility
np.random.seed(42)

# Generate baseline normal data (e.g., transaction amounts or salaries)
clean_data = np.random.normal(loc=50.0, scale=10.0, size=1000)

# 2. Corrupt one single observation with an extreme outlier
corrupted_data = clean_data.copy()
corrupted_data[0] = 1e8  # 100,000,000

# 3. Mean vs Median Comparison
print(f"Clean Mean:     {np.mean(clean_data):.4f} | Clean Median:     {np.median(clean_data):.4f}")
print(f"Corrupted Mean: {np.mean(corrupted_data):.4f} | Corrupted Median: {np.median(corrupted_data):.4f}")

# 4. Trimmed Mean (discarding 10% from bottom and 10% from top)
trimmed_clean = stats.trim_mean(clean_data, proportiontocut=0.1)
trimmed_corrupt = stats.trim_mean(corrupted_data, proportiontocut=0.1)
print(f"Trimmed Clean Mean: {trimmed_clean:.4f} | Trimmed Corrupted Mean: {trimmed_corrupt:.4f}")

# 5. Mode calculation via scipy and Counter
ages = np.random.randint(low=18, high=90, size=500)
scipy_mode = stats.mode(ages, keepdims=True)
print(f"Mode (scipy): value = {scipy_mode.mode[0]}, count = {scipy_mode.count[0]}")

age_counter = Counter(ages)
most_common_age, highest_freq = age_counter.most_common(1)[0]
print(f"Mode (Counter): value = {most_common_age}, count = {highest_freq}")
```

---

## 3. Phase 2: Measures of Dispersion (Variability & Spread)

Dispersion quantifies how much the data points stretch, squeeze, or deviate from the center.

### 3.1 Range
$$\text{Range} = X_{\max} - X_{\min}$$
Extremely sensitive to outliers; only considers two extreme values.

---

### 3.2 Population Variance ($\sigma^2$) vs. Sample Variance ($s^2$)

#### Formulas
* **Population Variance ($\sigma^2$):** Used when measuring every individual in the entire population ($N$):
  $$\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2$$

* **Sample Variance ($s^2$):** Used when inferring population variance from a subset ($n$):
  $$s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

#### Why $n-1$? (Bessel's Correction & Degrees of Freedom)
* In a sample, observations $x_i$ cluster closer to their sample mean $\bar{x}$ than to the unknown true population mean $\mu$.
* If we divide by $n$, the expected sample variance is systematically lower than the true population variance:
  $$\mathbb{E}\left[ \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2 \right] = \frac{n-1}{n} \sigma^2 < \sigma^2$$
* Dividing by $n - 1$ removes this downward bias, producing an **unbiased estimator**:
  $$\mathbb{E}[s^2] = \sigma^2$$
* In Python: `ddof` stands for **Delta Degrees of Freedom**. Divisor is $N - \text{ddof}$.
  * `ddof=0` $\implies$ divide by $N$ (Population)
  * `ddof=1` $\implies$ divide by $n-1$ (Sample)

---

### 3.3 Standard Deviation ($\sigma, s$)

#### Definition
Standard deviation is the square root of variance. It restores the dispersion metric back to the original units of the data (dollars, meters, etc.):
$$\sigma = \sqrt{\sigma^2}, \quad s = \sqrt{s^2}$$

#### First-Principles Step-by-Step Algorithm
1. Compute the mean: $\bar{x} = \frac{1}{n}\sum x_i$
2. Calculate deviation for every observation: $d_i = x_i - \bar{x}$
3. Square each deviation: $d_i^2 = (x_i - \bar{x})^2$
4. Sum all squared deviations and divide by degrees of freedom ($n$ or $n-1$).
5. Take the positive square root: $\sqrt{\text{Variance}}$.

---

### 3.4 Percentiles, Quartiles & Interquartile Range (IQR)

* **$Q_1$ (25th percentile):** $25\%$ of data lies below this value.
* **$Q_2$ (50th percentile):** The Median.
* **$Q_3$ (75th percentile):** $75\%$ of data lies below this value.
* **Interquartile Range (IQR):**
  $$\text{IQR} = Q_3 - Q_1$$
* **Tukey's Fences (Boxplot Outlier Detection):**
  * $\text{Lower Bound} = Q_1 - 1.5 \times \text{IQR}$
  * $\text{Upper Bound} = Q_3 + 1.5 \times \text{IQR}$
  * Any point outside $[\text{Lower Bound}, \text{Upper Bound}]$ is flagged as an outlier.

---

### 3.5 Coefficient of Variation (CV) & MAD

* **Coefficient of Variation (CV):** Relative measure of dispersion (dimensionless):
  $$CV = \frac{\sigma}{\mu} \times 100\%$$
  Enables comparing volatility between two stocks or datasets with completely different price scales.
* **Median Absolute Deviation (MAD):** Highly robust dispersion metric:
  $$\text{MAD} = \text{median}(|x_i - \text{median}(X)|)$$

---

### Code Implementation: Dispersion from Scratch vs. Libraries

```python
import numpy as np
import scipy.stats as stats
import statistics

data = [1, 4, 5, 4, 8]
n = len(data)

# Step 1: Mean
mean = sum(data) / n

# Step 2: Deviations
deviations = [x - mean for x in data]

# Step 3: Squared deviations
sq_deviations = [d**2 for d in deviations]

# Step 4: Population Variance (ddof=0) and Sample Variance (ddof=1)
pop_var_manual = sum(sq_deviations) / n
sample_var_manual = sum(sq_deviations) / (n - 1)

print(f"Original Data: {data}")
print(f"Mean: {mean}")
print(f"Deviations: {deviations}")
print(f"Squared Deviations: {sq_deviations}")
print(f"Population Variance (manual): {pop_var_manual:.4f}")
print(f"Sample Variance (manual):     {sample_var_manual:.4f}")

# Validating across Python packages
print("\n--- Package Verification ---")
print("NumPy pop var (ddof=0):      ", np.var(data, ddof=0))
print("NumPy sample var (ddof=1):   ", np.var(data, ddof=1))
print("statistics.variance (ddof=1):", statistics.variance(data))
print("scipy.stats.tvar (ddof=1):   ", stats.tvar(data))

# Standard Deviations
print("NumPy pop std (ddof=0):      ", np.std(data, ddof=0))
print("NumPy sample std (ddof=1):   ", np.std(data, ddof=1))
print("statistics.stdev (ddof=1):   ", statistics.stdev(data))
print("scipy.stats.tstd (ddof=1):   ", stats.tstd(data))

# IQR and Outlier Detection
q75, q25 = np.percentile(data, [75, 25])
iqr = q75 - q25
lower_bound = q25 - 1.5 * iqr
upper_bound = q75 + 1.5 * iqr
print(f"\nQ1: {q25}, Q3: {q75}, IQR: {iqr}")
print(f"Acceptable range without outliers: [{lower_bound}, {upper_bound}]")
```

---

## 4. Phase 3: Measures of Shape & Statistical Moments

Moments are quantitative measures describing the shape of a probability distribution function.

### 4.1 The 4 Statistical Moments

| Moment | Name | Mathematical Formula | What It Measures |
| :--- | :--- | :--- | :--- |
| **1st Moment** | **Mean** ($\mu$) | $\mathbb{E}[X] = \mu$ | **Location** (Central position) |
| **2nd Central Moment** | **Variance** ($\sigma^2$) | $\mu_2 = \mathbb{E}[(X - \mu)^2]$ | **Scale / Spread** (Dispersion) |
| **3rd Standardized Moment** | **Skewness** ($\tilde{\mu}_3$) | $\tilde{\mu}_3 = \mathbb{E}\left[\left(\frac{X - \mu}{\sigma}\right)^3\right]$ | **Symmetry / Direction of Tail** |
| **4th Standardized Moment** | **Kurtosis** ($\tilde{\mu}_4$) | $\tilde{\mu}_4 = \mathbb{E}\left[\left(\frac{X - \mu}{\sigma}\right)^4\right]$ | **Tailedness / Outlier Propensity** |

---

### 4.2 Skewness

* **Zero Skewness ($\approx 0$):** Symmetric distribution (e.g., standard Normal distribution). $\text{Mean} \approx \text{Median} \approx \text{Mode}$.
* **Positive (Right-Skewed) ($> 0$):** The right tail is longer/fatter. Pulls the mean to the right:
  $$\text{Mean} > \text{Median} > \text{Mode}$$
  *(Examples: Income distribution, household wealth, insurance claims).*
* **Negative (Left-Skewed) ($< 0$):** The left tail is longer/fatter. Pulls the mean to the left:
  $$\text{Mean} < \text{Median} < \text{Mode}$$
  *(Examples: Age at death, retirement age, human lifespan).*

---

### 4.3 Kurtosis

Kurtosis measures extreme tail events (financial black swans, heavy outliers):
* **Mesokurtic:** Kurtosis $= 3$ (Excess Kurtosis $= 0$). Perfect Normal Distribution.
* **Leptokurtic:** Kurtosis $> 3$ (Excess Kurtosis $> 0$). Fat tails, high peak, higher probability of extreme outliers (e.g., Bitcoin returns, financial markets).
* **Platykurtic:** Kurtosis $< 3$ (Excess Kurtosis $< 0$). Thin tails, flat peak (e.g., Uniform distribution).

```python
from scipy.stats import skew, kurtosis
import numpy as np

np.random.seed(42)
sample = np.random.normal(loc=0, scale=1, size=5000)

print(f"Sample Skewness:        {skew(sample):.4f} (Expect ~ 0)")
print(f"Fisher Excess Kurtosis: {kurtosis(sample, fisher=True):.4f} (Expect ~ 0)")
```

---

## 5. Phase 4: Probability Theory Foundations

### 5.1 Sample Space, Events, and Classical Probability

* **Sample Space ($S$):** The set of all possible outcomes of a random experiment.
  * For 1 fair die: $S = \{1, 2, 3, 4, 5, 6\} \implies n(S) = 6$.
  * For 2 dice: $S = \{(1,1), (1,2), \dots, (6,6)\} \implies n(S) = 36$.
* **Event ($A$):** Any subset of $S$.
* **Classical Probability:**
  $$P(A) = \frac{n(A)}{n(S)} = \frac{\text{Number of Favorable Outcomes}}{\text{Total Number of Possible Outcomes}}$$

---

### 5.2 Discrete vs. Continuous Random Variables

* **Discrete Random Variable:** Takes countably distinct values (integers: count of heads, number of defect items, dice rolls).
* **Continuous Random Variable:** Takes any value within an interval (real numbers: salary, height, time, temperature).

---

### 5.3 PMF vs. PDF vs. CDF

* **Probability Mass Function (PMF) — For Discrete Variables:**
  * Returns the exact probability of $X = x$:
    $$P(X = x) = f(x), \quad \sum_{x} f(x) = 1, \quad 0 \le f(x) \le 1$$
* **Probability Density Function (PDF) — For Continuous Variables:**
  * For continuous variables, the probability of hitting an exact exact number is 0 ($P(X = 5.00000\dots) = 0$).
  * The PDF gives the **density**. Probability is the **area under the curve**:
    $$P(a \le X \le b) = \int_{a}^{b} f(x) \, dx, \quad \int_{-\infty}^{\infty} f(x) \, dx = 1$$
* **Cumulative Distribution Function (CDF) — For Both:**
  * The probability that $X$ is less than or equal to $x$:
    $$F(x) = P(X \le x)$$

---

## 6. Phase 5: Probability Distributions (Formulas, Visuals & Code)

### 6.1 Discrete Uniform Distribution (Rolling 1 Die)

Every outcome has identical probability:
$$P(X = k) = \frac{1}{k_{\max} - k_{\min} + 1}$$
For a 6-sided die: $P(X = 1) = P(X = 2) = \dots = P(X = 6) = \frac{1}{6} \approx 0.1667$.

```python
import numpy as np

np.random.seed(100)
roll_1_die = np.random.randint(low=1, high=7, size=10)
print("10 rolls of a single die:", roll_1_die)
```

---

### 6.2 Discrete Triangular Distribution (Sum of 2 Dice)

When rolling 2 dice and taking their sum:
* Smallest sum: $2$ (only $(1,1) \implies 1/36$).
* Peak sum: $7$ (combos $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1) \implies 6/36 = 1/6$).
* Largest sum: $12$ (only $(6,6) \implies 1/36$).
* The distribution is triangular. As the number of dice rolled grows ($n \to \infty$), the distribution converges to a Gaussian/Normal bell curve due to the **Central Limit Theorem**.

```python
dice_1 = np.random.randint(low=1, high=7, size=10000)
dice_2 = np.random.randint(low=1, high=7, size=10000)
totals = dice_1 + dice_2
# Plotting totals will show a symmetric triangle peaking at 7
```

---

### 6.3 Continuous Uniform Distribution

A variable is equally likely to land anywhere inside interval $[a, b]$:
$$f(x) = \begin{cases} \frac{1}{b - a} & \text{for } a \le x \le b \\ 0 & \text{otherwise} \end{cases}$$
* Mean: $\mu = \frac{a + b}{2}$
* Variance: $\sigma^2 = \frac{(b - a)^2}{12}$

```python
values = np.random.uniform(low=-10.0, high=10.0, size=100000)
# A histogram with bins=50 will show a rectangular flat distribution
```

---

### 6.4 Normal (Gaussian) Distribution $\mathcal{N}(\mu, \sigma^2)$

#### Formula
$$f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{1}{2}\left(\frac{x - \mu}{\sigma}\right)^2 \right)$$

#### Key Characteristics
* **Symmetry:** Perfectly bell-shaped around mean $\mu$.
* **Standard Normal ($Z$):** When $\mu = 0$ and $\sigma = 1$:
  $$Z = \frac{X - \mu}{\sigma}$$
* **Empirical (68-95-99.7) Rule:**
  * $\approx 68.27\%$ of values fall within $[\mu - 1\sigma, \mu + 1\sigma]$
  * $\approx 95.45\%$ of values fall within $[\mu - 2\sigma, \mu + 2\sigma]$
  * $\approx 99.73\%$ of values fall within $[\mu - 3\sigma, \mu + 3\sigma]$

```python
from scipy.stats import norm
import numpy as np

# Evaluating probability density at specific x coordinates
x = np.linspace(-3, 3, 100)
y = norm.pdf(x, loc=0, scale=1)  # standard normal density
```

---

### 6.5 Binomial Distribution $\mathcal{B}(n, p)$

#### Description & Conditions
Models the number of "successes" $k$ in $n$ independent trials, where each trial has probability $p$ of success (Bernoulli trial).
1. Fixed number of trials $n$.
2. Only two outcomes per trial (Success / Failure).
3. Probability of success $p$ is constant.
4. Trials are mutually independent.

#### Mathematical Formulation
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} = \frac{n!}{k!(n-k)!} p^k (1-p)^{n-k}$$
* Mean: $\mu = n \cdot p$
* Variance: $\sigma^2 = n \cdot p \cdot (1 - p)$

```python
from scipy.stats import binom
import numpy as np

# Example: 10 coin flips with fair coin (p=0.5)
n = 10
p = 0.5
x = np.arange(0, n + 1)
probabilities = binom.pmf(x, n, p)

for k, prob in zip(x, probabilities):
    print(f"P({k} Heads) = {prob:.4f}")
```

---

### 6.6 Exponential Distribution $\text{Exp}(\lambda)$

#### Description & Applications
Models the **amount of time or distance until the next event occurs** (e.g., time until next customer enters a store, time until machine component failure, call center inter-arrival times).

#### Mathematical Formulation
$$f(x; \lambda) = \lambda e^{-\lambda x} \quad \text{for } x \ge 0$$
* Cumulative Distribution Function: $F(x) = 1 - e^{-\lambda x}$
* Mean: $\mu = \frac{1}{\lambda}$
* Variance: $\sigma^2 = \frac{1}{\lambda^2}$
* **Memoryless Property:** $P(X > t + s \mid X > t) = P(X > s)$. The probability of an event happening in the next 5 minutes is independent of how long you've already waited.

```python
from scipy.stats import expon
import numpy as np

# Scale parameter in scipy is 1 / lambda (the mean waiting time)
scale = 2.0  # mean wait of 2 units of time
x = np.linspace(0, 10, 100)
pdf_values = expon.pdf(x, scale=scale)
```

---

### 6.7 Poisson Distribution $\text{Pois}(\lambda)$ *(Added Full Implementation)*

#### Description & Applications
Models the **number of events occurring within a fixed interval of time or space**, given that events occur with a known constant mean rate $\lambda$ and independently of the time since the last event.
*(Examples: number of website requests per second, number of emergency room arrivals per hour, number of typographical errors per page).*

#### Mathematical Formulation
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!} \quad \text{for } k = 0, 1, 2, \dots$$
* Mean: $\mu = \lambda$
* Variance: $\sigma^2 = \lambda$  *(Crucial hallmark: Mean equals Variance)*

```python
from scipy.stats import poisson
import numpy as np

# Example: A website receives an average of 4 requests per minute (lambda = 4)
lam = 4
k_values = np.arange(0, 15)
poisson_probs = poisson.pmf(k_values, mu=lam)

for k, prob in zip(k_values, poisson_probs):
    print(f"P({k} requests) = {prob:.4f}")
```

---

## 7. Phase 6: Bridging to Inferential Statistics

### 7.1 Central Limit Theorem (CLT)

#### Core Theorem
No matter the underlying distribution of the population (skewed, uniform, bimodal), the distribution of the **sample means** ($\bar{X}_n$) approaches a **Normal Distribution** as the sample size $n$ becomes sufficiently large (typically $n \ge 30$):
$$\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$$

#### Practical Demonstration (Dice Summation)
As demonstrated in `O01_4_basics.py`, rolling 1 die gives a flat uniform distribution. Rolling 2 dice creates a triangular distribution. Rolling 10 or 30 dice produces a nearly perfect Gaussian bell curve.

---

### 7.2 Standard Error of the Mean (SEM)

The standard deviation of the sampling distribution of the mean:
$$\text{SEM} = \frac{s}{\sqrt{n}}$$
As sample size $n$ increases, uncertainty shrinks by a factor of $\frac{1}{\sqrt{n}}$.

```python
from scipy.stats import sem
sample_data = [50, 52, 48, 55, 49, 53, 51]
print("SEM:", sem(sample_data))
```

---

### 7.3 Covariance & Correlation (Pearson vs. Spearman)

* **Covariance:** Measures the joint variability of two random variables:
  $$\text{Cov}(X, Y) = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})$$
  *(Scale-dependent: Hard to interpret magnitude).*
* **Pearson Correlation ($r$):** Standardized covariance measuring linear relationship:
  $$r = \frac{\text{Cov}(X, Y)}{s_X s_Y} \quad (-1 \le r \le 1)$$
* **Spearman Rank Correlation ($\rho$):** Computes Pearson correlation on ranked data. Detects **monotonic non-linear** relationships and is robust against outliers.

---

## 8. Phase 7: Python Library Comparison & Critical Gotchas

### 8.1 The $ddof$ Default Trap

| Library / Method | Function | Default `ddof` | Target |
| :--- | :--- | :--- | :--- |
| **NumPy** | `np.var(x)`, `np.std(x)` | **`ddof=0`** | **Population** ($/ N$) |
| **Python Standard** | `statistics.variance(x)`, `statistics.stdev(x)` | **`ddof=1`** | **Sample** ($/ n-1$) |
| **SciPy** | `scipy.stats.tvar(x)`, `scipy.stats.tstd(x)` | **`ddof=1`** | **Sample** ($/ n-1$) |
| **Pandas** | `df['col'].var()`, `df['col'].std()` | **`ddof=1`** | **Sample** ($/ n-1$) |

> [!WARNING]
> If you compare `np.var(data)` with `pd.Series(data).var()`, their results will **differ** because NumPy defaults to `ddof=0` while Pandas defaults to `ddof=1`. Always specify `ddof=1` explicitly in NumPy when calculating sample statistics!

---

### 8.2 Summary Cheat-Sheet: Python Commands

```python
# --- Central Tendency ---
np.mean(x)
np.median(x)
stats.mode(x)
stats.trim_mean(x, proportiontocut=0.1)

# --- Dispersion ---
np.var(x, ddof=1)               # Sample variance
np.std(x, ddof=1)               # Sample standard deviation
iqr = stats.iqr(x)              # Interquartile range

# --- Shape ---
stats.skew(x)                   # Skewness
stats.kurtosis(x, fisher=True)  # Excess Kurtosis (Normal = 0)

# --- Discrete Distributions ---
stats.binom.pmf(k, n, p)        # Binomial PMF
stats.poisson.pmf(k, mu)        # Poisson PMF

# --- Continuous Distributions ---
stats.norm.pdf(x, loc, scale)   # Normal PDF
stats.norm.cdf(x, loc, scale)   # Normal CDF
stats.expon.pdf(x, scale)       # Exponential PDF
```

---
*Created as part of CDAC Data Analytics Day 3 Statistics Module.*
