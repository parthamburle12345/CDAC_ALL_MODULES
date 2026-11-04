# Practice_EDA: End-to-End Enterprise Data Analytics & Causal Inference Roadmap

This directory contains a complete, unified implementation of all **6 Phases** described in [`readme_detail.md`](../readme_detail.md) consolidated into a single master Jupyter Notebook: [`Complete_Practice_EDA.ipynb`](Complete_Practice_EDA.ipynb).

---

## 1. Evaluation: Why The Stack v2 is Unsuitable for this Roadmap

* **The Stack v2** is a massive repository of raw source code (Git commits, file contents, code tokens, and programming language licenses) built by Hugging Face & ServiceNow for training Code LLMs (like StarCoder).
* **Why it does not fit `readme_detail.md`:**
  - **No Economic or Customer Foundation:** It lacks monetary transactions, order items, profit margins, shipping fees, CAC, LTV, ARR/MRR, and customer retention matrices required for Phase 1 & Phase 3.
  - **No Marketing or Product Funnels:** It lacks multi-stage web conversion funnels (Phase 3 Step 4).
  - **No Spatial Dimensions:** It has no customer latitude/longitude or state boundaries needed for geospatial maps and choropleths (Phase 4 Step 3).
  - **No Controlled Experiments or Policy Interventions:** It does not feature A/B testing variants, sample size power calculations, Difference-in-Differences (DiD) policy evaluations, or Propensity Score Matching (PSM) (Phase 6).

**The Solution:** We created a comprehensive, multi-table **Enterprise E-Commerce & Retail Analytics** dataset specifically architected to satisfy every single technique, formula, and visualization across all 6 phases.

---

## 2. Directory Structure

```text
Practice_EDA/
├── data/
│   ├── enterprise_retail_analytics.csv      # Master tabular dataset (15,000 orders, 32 features, 4.8 MB)
│   ├── enterprise_retail_analytics.parquet  # Optimized columnar Parquet storage (1.02 MB)
│   └── analytics_warehouse.db               # SQLite Relational Database (orders, items, customers, reviews, funnels, hierarchies)
├── Complete_Practice_EDA.ipynb              # Single Consolidated Master Notebook (All 6 Phases, 163 cells)
├── generate_data.py                         # Reproducible data generation script
├── README.md                                # Documentation and workflow guide
```

---

## 3. Dataset Architecture (`enterprise_retail_analytics`)

The dataset spans 3,500 customers, 15,000 transactions, 80 products, and 25,000 web sessions:

| Entity | Key Features | Analytical Role |
| :--- | :--- | :--- |
| **Customers** | `customer_id`, `state`, `city`, `latitude`, `longitude`, `segment`, `acquisition_channel`, `income_bracket` | Geographic mapping, CAC, LTV, MNAR missing data diagnosis |
| **Orders** | `order_id`, `purchase_timestamp`, `delivered_timestamp`, `order_status`, `payment_method`, `payment_installments` | Time series, rolling windows, MAR missing data, SQL window functions |
| **Items & Catalog** | `product_sku`, `base_price`, `freight_value`, `cost_of_goods_sold`, `discount_amount`, `net_profit_margin` | Outlier Winsorization, VIF collinearity, power transforms, Simpson's paradox |
| **Customer Feedback**| `review_score`, `review_comment_message` | MCAR missing data, regex SKU extraction, TF-IDF, NLP sentiment |
| **Web Sessions** | `session_id`, `furthest_funnel_step`, `device_type`, `ab_test_variant`, `converted` | Conversion funnels, drop-off analysis, A/B hypothesis testing |
| **Policy & Regions** | `treatment_region`, `policy_period` | Causal Inference: Difference-in-Differences (DiD) & Propensity Score Matching (PSM) |

---

## 4. Master Notebook Structure (`Complete_Practice_EDA.ipynb`)

The master notebook is organized sequentially into all 6 phases:

### Phase 1: Ingestion & Foundation
- **Step 1: Ingestion & Memory Management:** Chunked processing with `pd.read_csv(..., chunksize=2500)`, CSV vs Parquet benchmarks (speedup factor & file size), automatic downcasting reducing memory by >50%.
- **Step 2: Relational SQL:** Connects to `analytics_warehouse.db`, runs `CASE WHEN` conditional aggregations, window functions (`ROW_NUMBER()`, `LAG()`, `LEAD()`, running totals), recursive CTE for category hierarchies, and cohort retention grids.
- **Step 3: Advanced Wrangling:** Multi-Index slicing (`IndexSlice`), vectorized regex SKU parsing, custom `.transform()` mapping, pivot tables, and 7-day rolling sales averages.
- **Step 4: Missing Data Taxonomy & Cleanup:** Statistical diagnosis of MCAR, MAR, and MNAR patterns, `KNNImputer` vs median imputation, 1% outlier Winsorization, and fuzzy string deduplication.

### Phase 2: Auditing & Profiling (EDA)
- **Step 1: Automated Profiling & Schema Enforcement:** Programmatic data health reports (nulls, cardinality, memory) and programmatic schema assertions.
- **Step 2: Distribution Audits:** Continuous KDE, Boxen plots (letter-value for heavy tails), Violin plots, skewness/kurtosis calculations, and multivariate joint `PairGrid` plots.
- **Step 3: Correlation & Association:** Pearson (linear), Spearman (rank monotonic), Cramér's V (categorical pairs), Variance Inflation Factor (VIF) collinearity tests, and Mutual Information.
- **Step 4: Story Extraction & Business Hypotheses:** Empirical proof of **Simpson's Paradox** (aggregate discount vs margin reversal), state-level delivery delay deep dives, and prioritized operational hypotheses.

### Phase 3: Feature Engineering & Economic Alignment (KPIs)
- **Step 1: Categorical & Numerical Transformations:** One-Hot Encoding, Ordinal Encoding, Smoothed Target Encoding, StandardScaler vs RobustScaler, and Yeo-Johnson power transforms.
- **Step 2: Temporal, Cyclical & Text Features:** Purchase hour/day/month deltas, Sine/Cosine cyclical projection ($\sin(2\pi t/T)$), text character/word counts, and TF-IDF vectors.
- **Step 3: Economic Alignment (LTV & Churn):** Channel CAC attribution, historical customer LTV, LTV:CAC payback ratios, Logo Churn vs Revenue Churn, DAU/MAU stickiness, and longitudinal cohort revenue expansion heatmaps.
- **Step 4: Conversion Funnels & Dashboards:** 6-stage web conversion funnel drop-off analysis, GMV, Marketplace Take-Rate, Net Revenue, ARPU, and executive scorecard.

### Phase 4: Communication & Storytelling (Visualization)
- **Step 1: Accessible Static Layouts:** Seaborn `FacetGrid`, colorblind palettes, and publication-ready multi-panel dashboard built with Matplotlib `GridSpec`.
- **Step 2: Interactive Drill-Down Explorers:** Plotly Express interactive scatter with hover data, hierarchical Sunburst and Treemap visualizations, financial Waterfall chart (Gross Revenue $\rightarrow$ Net Profit), and 60-day price spread Candlestick charts.
- **Step 3: Geospatial Analytics:** US-wide latitude/longitude point clusters, state-level regional Choropleth maps, and 2D spatial hexbin density heatmaps.
- **Step 4: Executive Reporting:** Presentation architecture based on Barbara Minto's **Pyramid Principle** (Apex recommendation first, MECE supporting pillars).

### Phase 5: Advanced Intelligence (Unsupervised & Predictive Modeling)
- **Step 1: Unsupervised Learning & Segmentation:** RFM (Recency, Frequency, Monetary) feature extraction, Elbow method (Inertia) and Silhouette score analysis, K-Means customer persona profiling, DBSCAN noise detection, PCA 2D projection, and Isolation Forests for transaction anomaly detection.
- **Step 2: Predictive Modeling:** Customer churn classification (Random Forest & Logistic Regression), Confusion Matrices, ROC-AUC, Precision-Recall curves, customer spend forecasting via Ridge & Lasso regression, and leakage-free Scikit-Learn `Pipeline` with `StratifiedKFold`.
- **Step 3: Model Interpretability & Trust:** TreeSHAP global feature summary plots, dependence plots, and transparent waterfall breakdown of individual customer churn risk for executive stakeholders.

### Phase 6: Validation & Causal Impact (Experimentation)
- **Step 1: Experiment Design:** Primary & guardrail metrics, Statistical Power Analysis ($\alpha=0.05, 1-\beta=0.80$), MDE, and sample size / duration formulas.
- **Step 2: Statistical Inference:** Two-sample proportion Z-test for conversion rates, Welch's T-test for order value uplift, p-values, 95% confidence intervals, and Bonferroni & Benjamini-Hochberg FDR multiple testing corrections.
- **Step 3: Advanced Experimentation:** Sequential testing simulation (alpha-inflation under early peeking), and Multi-Armed Bandits (Thompson Sampling simulation allocating traffic dynamically to winning variants).
- **Step 4: Causal Inference & Quasi-Experiments:** Difference-in-Differences ($2 \times 2$ DiD regression with interaction term $\beta_3$), Parallel Trends test, and Propensity Score Matching (PSM) with Nearest Neighbor matching to estimate Average Treatment Effect on the Treated (ATT).

---

## 5. How to Run

1. Open your terminal in the workspace root and activate the environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
2. Open the single consolidated notebook in Jupyter or your IDE:
   ```powershell
   jupyter lab Practice_EDA/Complete_Practice_EDA.ipynb
   ```
3. Select the **Python (.venv)** kernel and execute cells sequentially.
