# Statistical Functions Reference: SciPy & NumPy

A comprehensive reference of essential statistical functions across **SciPy** (`scipy.stats`) and **NumPy** (`numpy.random` / `np.random.default_rng`).

---

## 1. SciPy Statistical Functions (`scipy.stats`)

In SciPy, every probability distribution object (e.g., `stats.norm`, `stats.binom`, `stats.poisson`) exposes a unified set of methods.

### Core Distribution Methods

| Function | Full Name | Mathematical Meaning | Key Use Case |
| :--- | :--- | :--- | :--- |
| **`pdf(x)`** | Probability Density Function | $f(x) = P(X = x)$ for **continuous** variables | Plotting continuous distribution curves (e.g., Gaussian curve). |
| **`pmf(k)`** | Probability Mass Function | $P(X = k)$ for **discrete** integer variables | Calculating exact point probabilities (e.g., getting *exactly* 3 heads in 10 flips). |
| **`cdf(x)`** | Cumulative Distribution Function | $F(x) = P(X \le x)$ | Finding tail probabilities or "less than or equal to" thresholds (e.g., probability score $\le 80$). |
| **`sf(x)`** | Survival Function | $1 - F(x) = P(X > x)$ | Complement of CDF; calculates "greater than" probabilities without precision loss (e.g., p-values). |
| **`ppf(q)`** | Percentile Point Function | $F^{-1}(q)$ (Inverse CDF) | Finding critical values/quantiles given a cumulative probability $q$ (e.g., $z$-score for top 5%). |
| **`isf(q)`** | Inverse Survival Function | $S^{-1}(q)$ (Inverse SF) | Upper-tail critical values (e.g., finding the upper 2.5% cutoff for hypothesis testing). |
| **`rvs(size)`** | Random Variates Sampling | Generates random draws from the distribution | Creating synthetic benchmark samples. |
| **`logpdf(x)` / `logpmf(k)`** | Log Probability Density/Mass | $\ln(f(x))$ or $\ln(P(X = k))$ | Numerical stability in Maximum Likelihood Estimation (MLE) to avoid underflow. |
| **`logcdf(x)` / `logsf(x)`** | Log Cumulative / Log Survival | $\ln(F(x))$ or $\ln(S(x))$ | High-precision tail computations in Bayesian modeling and inference. |

### Summary Statistics & Fitting Methods

| Function | Description & Example Output |
| :--- | :--- |
| **`stats.fit(data)`** | Fits distribution parameters ($\mu, \sigma$, shape parameters) to an empirical dataset via Maximum Likelihood. |
| **`dist.stats(moments='mvsk')`** | Computes the four primary distribution moments: **Mean** ($m$), **Variance** ($v$), **Skewness** ($s$), and **Kurtosis** ($k$). |
| **`dist.mean()`** | Returns the exact analytical mean $\mathbb{E}[X]$ of the distribution. |
| **`dist.var()`** | Returns the exact analytical variance $\text{Var}(X)$ of the distribution. |
| **`dist.std()`** | Returns the analytical standard deviation $\sigma = \sqrt{\text{Var}(X)}$. |
| **`dist.interval(confidence)`** | Calculates symmetric confidence bounds containing the specified proportion (e.g., `interval(0.95)`) of probability mass. |

---

## 2. Modern NumPy Random Generator Methods (`np.random.default_rng`)

NumPy’s `Generator` API (`rng = np.random.default_rng()`) provides high-performance stochastic generation routines.

### Continuous Distribution Generators

| Function Call | Mathematical Formula | Primary Domain / Usage |
| :--- | :--- | :--- |
| **`rng.normal(loc, scale, size)`** | $\mathcal{N}(\mu, \sigma^2)$ | Gaussian continuous noise, linear regression errors. |
| **`rng.uniform(low, high, size)`** | $\mathcal{U}(a, b)$ | Uniform domain sampling, randomized hyperparameters. |
| **`rng.exponential(scale, size)`** | $\text{Exp}(\lambda = 1/\text{scale})$ | Waiting times between events, survival analysis. |
| **`rng.gamma(shape, scale, size)`** | $\text{Gamma}(k, \theta)$ | Aggregated queuing delays, positive continuous skew. |
| **`rng.beta(a, b, size)`** | $\text{Beta}(\alpha, \beta)$ | Probabilities, proportions, Bayesian prior modeling. |
| **`rng.lognormal(mean, sigma, size)`** | $\text{Lognormal}(\mu, \sigma)$ | Stock prices, income distributions, biological metrics. |
| **`rng.pareto(a, size)`** | $\text{Pareto}(\alpha)$ | Heavy-tailed power-law phenomena (80/20 rule). |
| **`rng.multivariate_normal(mean, cov, size)`** | $\mathcal{N}_d(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ | Correlated multi-feature matrices, vector sampling. |

### Discrete Distribution Generators

| Function Call | Mathematical Formula | Primary Domain / Usage |
| :--- | :--- | :--- |
| **`rng.binomial(n, p, size)`** | $\text{Binomial}(n, p)$ | Number of successes in $n$ independent Bernoulli trials. |
| **`rng.poisson(lam, size)`** | $\text{Poisson}(\lambda)$ | Event count arrivals per fixed unit of time/space. |
| **`rng.geometric(p, size)`** | $\text{Geometric}(p)$ | Number of trials required before the first success occurs. |
| **`rng.hypergeometric(ngood, nbad, nsample)`** | $\text{Hypergeometric}(M, n, N)$ | Sampling without replacement from a finite population. |
| **`rng.integers(low, high, size)`** | Discrete $\mathcal{U}\{a, b-1\}$ | Uniform discrete integer draws. |

### Combinatorics & Categorical Methods

| Function Call | Operation Type | Primary Domain / Usage |
| :--- | :--- | :--- |
| **`rng.choice(a, size, p=weights)`** | Categorical Draw | Uniform or weighted sampling across categorical elements. |
| **`rng.permutation(x)`** | Combinatorial | Returns a **new shuffled copy** of array $x$. |
| **`rng.shuffle(x)`** | Combinatorial | Reorders target array $x$ **in-place**. |

---

## 3. Empirical & Sample Descriptive Functions (`numpy` & `scipy.stats`)

Functions used to evaluate observed sample data directly:

* **`np.mean(x)`** / **`np.std(x, ddof=1)`** / **`np.var(x, ddof=1)`**: Sample summary metrics ($ddof=1$ applies Bessel's correction for unbiased estimation).
* **`np.percentile(x, q)`** / **`np.quantile(x, q)`**: Empirical sample quantiles (e.g., `q=0.5` for median).
* **`np.cov(m)`**: Sample covariance matrix calculation across feature vectors.
* **`stats.pearsonr(x, y)`**: Pearson linear correlation coefficient $r \in [-1, 1]$.
* **`stats.skew(x)`** / **`stats.kurtosis(x)`**: Sample asymmetry (skewness) and tail-heaviness (excess kurtosis).