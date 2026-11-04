# Data Population & Synthetic Generation Techniques

This directory serves as the foundational module for generating, sampling, and populating datasets across deterministic grids, parametric continuous, discrete, empirical distributions, and noisy synthetic signals using **NumPy**, **SciPy**, and **Scikit-Learn**.

Populating controlled synthetic data is essential for unit testing, algorithmic benchmark verification, statistical simulation (e.g., Monte Carlo methods), and stress-testing machine learning pipelines against known statistical properties (e.g., variance, skewness, covariance).

---
#### High Level
1. Deterministic Domain & Grid Generators
   * 1.1. **Linear Spacing (`np.linspace`)**
   * 1.2. **Logarithmic Spacing (`np.logspace`)**
   * 1.3. **Geometric Spacing (`np.geomspace`)**
   * 1.4. **Step-Based Range (`np.arange`)**
   * 1.5. **Coordinate Grids (`np.meshgrid`)**

2. Functional & Noisy Signal Population
   * 2.1. **Additive Noisy Signals (Sine Wave)**
   * 2.2. **Polynomial & Trend Curves**
   * 2.3. **Autoregressive / Time-Series Synthetic Signals**

3. Continuous Probability Distributions (NumPy API) **(Univariate Sampling)**
   * 3.1. **Normal (Gaussian)** **(Univariate Sampling)**
   * 3.2. **Uniform** **(Univariate Sampling)**
   * 3.3. **Gamma** **(Univariate Sampling)**
   * 3.4. **Exponential** **(Univariate Sampling)**
   * 3.5. **Beta** **(Univariate Sampling)**
   * 3.6. **Log-Normal** **(Univariate Sampling)**
   * 3.7. **Triangular** **(Univariate Sampling)**
   * 3.8. **Student's t** **(Univariate Sampling)**
   * 3.9. **Chi-Square ($\chi^2$)** **(Univariate Sampling)**
   * 3.10. **F-Distribution** **(Univariate Sampling)**
   * 3.11. **Weibull** **(Univariate Sampling)**
   * 3.12. **Pareto** **(Univariate Sampling)**

4. Discrete Probability Distributions (NumPy API) **(Univariate Sampling)**
   * 4.1. **Bernoulli / Binary** **(Univariate Sampling)**
   * 4.2. **Binomial** **(Univariate Sampling)**
   * 4.3. **Poisson** **(Univariate Sampling)**
   * 4.4. **Discrete Uniform (Integers)** **(Univariate Sampling)**
   * 4.5. **Geometric** **(Univariate Sampling)**
   * 4.6. **Negative Binomial** **(Univariate Sampling)**
   * 4.7. **Hypergeometric** **(Univariate Sampling)**

5. Categorical Sampling & Combinatorics
   * 5.1. **Sample Space ($\Omega$) Enumeration & Event Set Sampling** **(Sample Spaces and Events)**
   * 5.2. **Uniform Categorical Sampling** **(Sample & Population / Univariate Sampling)**
   * 5.3. **Weighted Categorical Sampling** **(Sample & Population / Univariate Sampling)**
   * 5.4. **Permutation / Shuffling** **(Sample Spaces and Events)**
   * 5.5. **Bootstrap Re-sampling (Sampling with Replacement)** **(Re-sampling)**

6. Multivariate Datasets & Structural Generators **(Bivariate Sampling)**
   * 6.1. **Multivariate Normal Distribution** **(Bivariate Sampling)**
   * 6.2. **Dirichlet Distribution** **(Bivariate & Multivariate Sampling)**
   * 6.3. **Classification Clusters (`sklearn.datasets`)** **(Bivariate & Multivariate Sampling)**
   * 6.4. **Regression Datasets (`sklearn.datasets`)** **(Bivariate & Multivariate Sampling)**
   * 6.5. **Blob Clusters (`sklearn.datasets`)** **(Bivariate & Multivariate Sampling)**

7. Advanced & Bounded Sampling (`scipy.stats`)
   * 7.1. **Truncated Normal Distribution** **(Univariate Sampling)**
   * 7.2. **Kernel Density Estimation Sampling (KDE)** **(Re-sampling / Empirical Sampling)**

8. Conditional, Marginal & Bayesian Data Population
   * 8.1. **Joint & Marginal Probability Table Generation** **(Joint and Marginal Probability)**
   * 8.2. **Conditional Sampling ($P(Y \mid X)$ Dependent Data Population)** **(Conditional Probability)**
   * 8.3. **Bayesian Posterior Data Population (Prior $\times$ Likelihood Sampling)** **(Bayes' Theorem)**

---

## Technical Index: Data Population Paradigms

### 1. Deterministic Domain & Grid Generators
Essential for establishing evaluation domains, feature axes, loss landscapes, and signal baseline arrays.

* **Linear Spacing (`np.linspace`):** Generates $N$ evenly spaced values over a closed interval $[a, b]$. Ideal for independent variable axes ($x$-axis) and continuous function evaluations.
  `x = np.linspace(start=0.0, stop=10.0, num=100)`
* **Logarithmic Spacing (`np.logspace`):** Generates values spaced evenly on a logarithmic scale (base 10 by default). Essential for hyperparameter search grids (e.g., learning rates, regularization parameters $\alpha \in [10^{-5}, 10^{1}]$).
  `lrs = np.logspace(start=-5, stop=1, num=7)`
* **Geometric Spacing (`np.geomspace`):** Generates values spaced evenly on a geometric progression.
  `geom_grid = np.geomspace(start=1.0, stop=1000.0, num=4)`
* **Step-Based Range (`np.arange`):** Populates values spaced by a fixed step size $h$ over $[a, b)$.
  `time_steps = np.arange(start=0.0, stop=60.0, step=0.5)`
* **Coordinate Grids (`np.meshgrid`):** Constructs 2D or $N$-D coordinate matrices from 1D domain vectors for spatial population, loss surface rendering, and multi-variable evaluations.
  `X, Y = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))`

---

### 2. Functional & Noisy Signal Population
Combines deterministic ground-truth functions with stochastic error terms to model real-world noisy sensors, time series, and regression targets.

* **Additive Noisy Signals (Sine Wave):** Superimposes Gaussian noise onto periodic deterministic functions.
  `x = np.linspace(0, 2 * np.pi, 500); y = np.sin(x) + rng.normal(loc=0.0, scale=0.1, size=500)`
* **Polynomial & Trend Curves:** Generates linear and non-linear ground truth curves with additive error for regression benchmark testing.
  `x = np.linspace(-10, 10, 200); y = 3.5 * x**2 - 2.0 * x + 5.0 + rng.normal(0, 5.0, size=200)`
* **Autoregressive / Time-Series Synthetic Signals:** Simulates sequential data with persistent temporal autocorrelation and drift.
  `steps = rng.normal(loc=0.0, scale=1.0, size=1000); random_walk = np.cumsum(steps)`

---

### 3. Continuous Probability Distributions (NumPy API)
Used for modeling continuous variables such as measurements, times, financial returns, and physical quantities.

* **Normal (Gaussian):** Bell-shaped distribution parameterized by mean ($\mu$) and standard deviation ($\sigma$).
  `rng.normal(loc=40.0, scale=10.0, size=1000)`
* **Uniform:** Even probability density across a closed interval $[a, b]$.
  `rng.uniform(low=10.0, high=50.0, size=1000)`
* **Gamma:** Continuous, positively-skewed distribution modeling wait times and lifetime data.
  `rng.gamma(shape=2.0, scale=2.0, size=1000)`
* **Exponential:** Memoryless process modeling arrival time intervals between independent Poisson events.
  `rng.exponential(scale=1.0, size=1000)`
* **Beta:** Bounded on $[0, 1]$, ideal for modeling probabilities, ratios, and Bayesian priors.
  `rng.beta(a=0.5, b=0.5, size=1000)`
* **Log-Normal:** Distribution of a random variable whose logarithm is normally distributed (e.g., incomes, asset prices).
  `rng.lognormal(mean=0.0, sigma=1.0, size=1000)`
* **Triangular:** Continuous distribution defined by lower bound, upper bound, and peak mode.
  `rng.triangular(left=10.0, mode=25.0, right=50.0, size=1000)`
* **Student's t:** Heavy-tailed distribution used in small-sample statistical inference and robust modeling.
  `rng.standard_t(df=10, size=1000)`
* **Chi-Square ($\chi^2$):** Sum of squared independent standard normal variables, crucial for goodness-of-fit testing.
  `rng.chisquare(df=3, size=1000)`
* **F-Distribution:** Ratio of two independent chi-square variables, central to ANOVA and variance ratios.
  `rng.f(dfnum=5, dfden=20, size=1000)`
* **Weibull:** Used extensively in reliability analysis, survival modeling, and industrial failure rates.
  `rng.weibull(a=1.5, size=1000)`
* **Pareto:** Power-law distribution modeling 80/20 power-law phenomena (wealth distribution, word counts).
  `rng.pareto(a=3.0, size=1000)`

---

### 4. Discrete Probability Distributions (NumPy API)
Used for count data, success/failure experiments, and integer-bounded processes.

* **Bernoulli / Binary:** Single binary trial with success probability $p$.
  `rng.binomial(n=1, p=0.3, size=1000)`
* **Binomial:** Number of successes across $n$ independent trials with success probability $p$.
  `rng.binomial(n=10, p=0.5, size=1000)`
* **Poisson:** Count of events occurring within a fixed time/space interval under constant rate $\lambda$.
  `rng.poisson(lam=5.0, size=1000)`
* **Discrete Uniform (Integers):** Equiprobable random integers drawn from an interval $[a, b)$.
  `rng.integers(low=1, high=100, size=1000)`
* **Geometric:** Number of failure trials preceding the first success.
  `rng.geometric(p=0.3, size=1000)`
* **Negative Binomial:** Number of failures encountered before reaching $n$ target successes.
  `rng.negative_binomial(n=5, p=0.5, size=1000)`
* **Hypergeometric:** Sampling without replacement from a finite population containing two distinct classes.
  `rng.hypergeometric(ngood=20, nbad=80, nsample=10, size=1000)`

---

### 5. Categorical Sampling & Combinatorics
Used for generating labels, survey responses, and structured categorical attributes.

* **Sample Space ($\Omega$) Enumeration & Event Sampling:** Generating the set of all possible outcomes and calculating event probabilities $P(E) = \frac{\vert{}E\vert{}}{\vert{}\Omega\vert{}}$.
  `omega = list(itertools.product(range(1, 7), repeat=2))`
* **Uniform Categorical Sampling:** Equal selection probability across discrete elements.
  `rng.choice(['Control', 'Treatment_A', 'Treatment_B'], size=1000)`
* **Weighted Categorical Sampling:** Selection guided by custom probability weight vectors ($p$).
  `rng.choice(['Pass', 'Fail', 'Inconclusive'], size=1000, p=[0.70, 0.20, 0.10])`
* **Permutation / Shuffling:** Random reordering of existing arrays without replacement.
  `rng.permutation(array)` or `rng.shuffle(array)`
* **Bootstrap Re-sampling:** Generating empirical distributions by sampling with replacement.
  `rng.choice(empirical_data, size=(1000, len(empirical_data)), replace=True)`

---

### 6. Multivariate Datasets & Structural Generators
Used for high-dimensional feature matrices, regression/classification benchmarks, and spatial clusters.

* **Multivariate Normal Distribution:** Continuous vectors parameterized by a mean vector $\boldsymbol{\mu}$ and Covariance Matrix $\boldsymbol{\Sigma}$.
  `rng.multivariate_normal(mean=[0, 0], cov=[[1, 0.6], [0.6, 1]], size=1000)`
* **Dirichlet Distribution:** Multivariate probability vector generation where values sum to 1 (used for topic modeling and priors).
  `rng.dirichlet(alpha=[1, 2, 5], size=1000)`
* **Classification Clusters (`sklearn.datasets`):** Generates synthetic multi-class datasets with controlled noise and feature redundancy.
  `make_classification(n_samples=1000, n_features=5, n_classes=2, random_state=42)`
* **Regression Datasets (`sklearn.datasets`):** Generates linear and non-linear targets with additive Gaussian noise.
  `make_regression(n_samples=1000, n_features=4, noise=0.1, random_state=42)`
* **Blob Clusters (`sklearn.datasets`):** Isotropic Gaussian blobs for benchmarking unsupervised clustering algorithms (e.g., K-Means).
  `make_blobs(n_samples=1000, centers=3, n_features=2, random_state=42)`

---

### 7. Advanced & Bounded Sampling (`scipy.stats`)
Provides probability density function (PDF) evaluation, empirical fit generation, and truncated boundaries.

* **Truncated Normal Distribution:** Restricts Gaussian sampling strictly between lower and upper bounds $[a, b]$.
  `scipy.stats.truncnorm.rvs(a=-2, b=2, loc=40, scale=10, size=1000)`
* **Kernel Density Estimation Sampling (KDE):** Non-parametric population drawn directly from an estimated empirical data distribution.
  `scipy.stats.gaussian_kde(empirical_data).resample(1000)`

---

### 8. Conditional, Marginal & Bayesian Data Population
Models joint probability tables, dependent variables $P(Y \mid X)$, and Bayesian posterior distributions.

* **Joint & Marginal Probability Table Generation:** Sampling multi-variable discrete observations and computing contingency matrices.
  `pd.crosstab(df['Category'], df['Tier'], normalize=True, margins=True)`
* **Conditional Sampling ($P(Y \mid X)$):** Populating target outcomes conditioned on predictor states.
  `y = rng.binomial(n=1, p=np.where(x == 0, 0.05, 0.25))`
* **Bayesian Posterior Data Population:** Populating datasets by combining prior probabilities with likelihood functions using Bayes' Theorem.
  `P(State | Evidence) = (P(Evidence | State) * P(State)) / P(Evidence)`

---

## Best Practices & Systems Architecture Notes

1. **Modern NumPy Generator API:** Avoid using legacy `np.random.seed()` or `np.random.normal()`. Always instantiate a local Generator instance via `rng = np.random.default_rng(seed=42)` for optimal random number generation performance, reproducibility, and thread safety.
2. **Reproducibility:** Always pass an explicit seed (`seed=42` or `random_state=42`) when generating synthetic populations to ensure deterministic re-execution of research notebooks.
3. **Array Memory Layout:** For large-scale data population ($N > 10^7$), pre-allocate NumPy buffers or specify `dtype` explicitly (e.g., `np.float32` vs `np.float64`) to optimize memory bandwidth.