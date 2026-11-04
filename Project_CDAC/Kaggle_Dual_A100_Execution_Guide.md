# 📓 Kaggle Dual A100 Execution Guide: Qwen2.5-Coder C++ Fine-Tuning
### Step-by-Step Workflow for Running `qwen2_5_coder_cpp_review_kaggle.ipynb`

---

## 1. Prerequisites & Dataset Upload

1. Go to [kaggle.com](https://www.kaggle.com) and sign in.
2. Click **+ Create** ➔ **New Dataset**.
3. Title it: `the-stack-v2-cpp`.
4. Upload your C++ parquet shards from your local folder:
   ```text
   D:\Engineering\CDAC_ALL_MODULES\Project_CDAC\dataset\Cpp\
   (train-00000-of-00007.parquet, train-00001-of-00007.parquet, etc.)
   ```
5. Click **Create** (Keep it **Private**).

---

## 2. Importing the Notebook to Kaggle

1. In Kaggle, click **+ Create** ➔ **New Notebook**.
2. Go to **File** (top left menu) ➔ **Import Notebook**.
3. Select and upload:
   [`qwen2_5_coder_cpp_review_kaggle.ipynb`](file:///d:/Engineering/CDAC_ALL_MODULES/Project_CDAC/qwen2_5_coder_cpp_review_kaggle.ipynb)
4. On the right-side **Notebook Options** panel:
   * **Accelerator**: Select **GPU** ➔ Choose **A100 (or 2x A100 / Dual GPU)**.
   * **Internet**: Toggle to **ON** (required to download model weights from Hugging Face).
   * **Persistence**: Set to **Variables and Files**.
5. Click **+ Add Input** (top right) ➔ Select your uploaded dataset `the-stack-v2-cpp`.

---

## 3. Running the Pipeline Step-by-Step

### Step 1: Environment & Dependency Setup (Cell 1 & 2)
* Installs `transformers`, `peft`, `trl`, `accelerate`, `bitsandbytes`.
* Validates that your 2x A100 GPUs are detected and verifies native `bfloat16` precision support.

### Step 2: Exploratory Data Analysis (EDA) (Cell 3 & 4)
* Reads the parquet shard directly using PyArrow.
* Visualizes:
  - Distribution of C++ file extensions (`.cpp`, `.hpp`, `.cc`, `.h`).
  - File byte length distribution and outlier boundaries.
  - Summary metrics (quantiles, missing values, license distribution).

### Step 3: ML Data Preprocessing & Quality Filtering (Cell 5)
* Filters files within strict bounds ($200 \le \text{bytes} \le 12,000$) to fit context windows without truncating functions.
* Formats pairs into **Qwen2.5 ChatML** standard (`system`, `user`, `assistant`).
* Creates stratified splits: **80% Train, 10% Validation, 10% Test**.

### Step 4: LoRA Model Initialization (Cell 6)
* Loads `Qwen/Qwen2.5-Coder-7B-Instruct` in `bfloat16`.
* Configures LoRA adapter with rank $r=16$, $\alpha=32$, targeting all linear attention and MLP layers (`q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`).
* Enables **Gradient Checkpointing** to prevent out-of-memory errors.

### Step 5: SFT Training with Feedback Constraints (Cell 7)
* Uses Hugging Face `SFTTrainer`.
* Effective batch size = **32** (Per-device batch size = 4, Gradient accumulation steps = 4, across 2 GPUs).
* Cosine learning rate schedule with $2\times 10^{-4}$ and warmup ratio 0.03.
* Evaluates every 50 steps on validation split.

### Step 6: Academic Evaluation (Cell 8)
* Tests inference on holdout test set.
* Validates strict **JSON Schema compliance**.
* Calculates CodeBLEU and Severity classification accuracy.

### Step 7: Exporting Artifacts (Cell 9)
* Compresses the trained LoRA adapter into `qwen2_5_coder_7b_cpp_review_adapter.zip`.
* You can download this file from Kaggle's **Output** tab and plug it directly into your local FastAPI microservice!

---

## 4. Hardware Sizing & Training Time Estimates

| GPU Setup | Training Time (3 Epochs, ~5,000 samples) | VRAM Utilization | Recommended Batch Size |
| :--- | :---: | :---: | :---: |
| **2x A100 (80GB)** | **~18 to 25 minutes** | ~24 GB / 80 GB | `per_device_batch_size = 4`, `accum = 4` |
| **1x A100 (40GB)** | **~35 to 45 minutes** | ~26 GB / 40 GB | `per_device_batch_size = 4`, `accum = 8` |
| **2x T4 (Fallback)** | **~2.5 to 3.5 hours** | ~14 GB / 16 GB | `per_device_batch_size = 2`, `accum = 16` |

---

## 5. Troubleshooting Matrix
If you encounter any warning, loss anomaly, or memory issue while running on Kaggle, refer to your local diagnostic guide:
➔ [`Fine_Tuning_Troubleshooting_and_Decision_Guide.md`](file:///d:/Engineering/CDAC_ALL_MODULES/Project_CDAC/Fine_Tuning_Troubleshooting_and_Decision_Guide.md)
