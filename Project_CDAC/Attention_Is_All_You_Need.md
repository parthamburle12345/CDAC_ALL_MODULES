# Attention Is All You Need

- **Authors**: Ashish Vaswani\*, Noam Shazeer\*, Niki Parmar\*, Jakob Uszkoreit\*, Llion Jones\*, Aidan N. Gomez\*†, Łukasz Kaiser\*, Illia Polosukhin\*‡
- **Affiliations**: Google Brain, Google Research, University of Toronto
- **Venue**: 31st Conference on Neural Information Processing Systems (NeurIPS 2017), Long Beach, CA, USA
- **arXiv ID**: [1706.03762](https://arxiv.org/abs/1706.03762)
- **Local PDF File**: `Attention_Is_All_You_Need.pdf`

---

## 1. Abstract

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the **Transformer**, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. 

Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves **28.4 BLEU** on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of **41.8** after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

---

## 2. Background and Motivation

- **Limitations of Recurrent Networks (RNNs, LSTMs, GRUs)**:
  - Factor computation along symbol positions, aligning sequential time steps $t$.
  - Generating hidden state $h_t$ inherently requires previous hidden state $h_{t-1}$ and current token $x_t$.
  - **Sequential bottleneck**: Precludes intra-batch parallelization across sequence length during training.
  - Memory constraints limit batch sizes for long sequences.
- **Limitations of Convolutional Sequence Models (ConvS2S, ByteNet)**:
  - Operations required to relate signals between arbitrary distant positions grow linearly ($O(n)$) or logarithmically ($O(\log_k n)$).
  - Difficult to learn long-range context dependencies across distant tokens.
- **The Transformer Solution**:
  - Eliminates recurrent layers and sequential convolutions entirely.
  - Constant $O(1)$ operations to connect any two input/output positions via self-attention.
  - Counteracts loss of resolution via **Multi-Head Attention**.

---

## 3. Model Architecture

The Transformer follows the standard encoder-decoder paradigm using stacked self-attention and point-wise fully connected layers.

### 3.1 Encoder Stack
- Consists of a stack of $N = 6$ identical layers.
- Each layer contains two sub-layers:
  1. **Multi-Head Self-Attention mechanism**
  2. **Position-wise Feed-Forward Network**
- Residual connection around each sub-layer followed by Layer Normalization:
  $$\text{Output} = \text{LayerNorm}(x + \text{SubLayer}(x))$$
- Uniform dimensionality across all sub-layers: $d_{\text{model}} = 512$.

### 3.2 Decoder Stack
- Consists of a stack of $N = 6$ identical layers.
- In addition to the two encoder sub-layers, decoder introduces a third sub-layer:
  - **Cross-Attention (Encoder-Decoder Attention)** over the output of the encoder stack.
- **Masked Self-Attention**: Prevents positions from attending to subsequent future positions (preserves auto-regressive causality during generation).

---

## 4. Attention Mechanisms

An attention function maps queries ($Q$), keys ($K$), and values ($V$) to an output vector.

### 4.1 Scaled Dot-Product Attention
Given queries $Q \in \mathbb{R}^{n \times d_k}$, keys $K \in \mathbb{R}^{m \times d_k}$, and values $V \in \mathbb{R}^{m \times d_v}$:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$$

- Scaling by $\frac{1}{\sqrt{d_k}}$ prevents large dot products from pushing the softmax function into regions with vanishingly small gradients.

### 4.2 Multi-Head Attention
Instead of performing a single attention function with dimension $d_{\text{model}}$, Multi-Head Attention projects queries, keys, and values $h$ times with learned linear projections:

$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O$$

$$\text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$$

- Projection parameters:
  - $W_i^Q \in \mathbb{R}^{d_{\text{model}} \times d_k}$
  - $W_i^K \in \mathbb{R}^{d_{\text{model}} \times d_k}$
  - $W_i^V \in \mathbb{R}^{d_{\text{model}} \times d_v}$
  - $W^O \in \mathbb{R}^{h d_v \times d_{\text{model}}}$
- Hyperparameters:
  - Heads: $h = 8$
  - Dimensions: $d_k = d_v = d_{\text{model}} / h = 64$

---

## 5. Other Architectural Components

### 5.1 Position-wise Feed-Forward Networks (FFN)
Applied identically and independently to each position:
$$\text{FFN}(x) = \max(0, x W_1 + b_1) W_2 + b_2$$
- Input/output dimension: $d_{\text{model}} = 512$
- Inner hidden dimension: $d_{ff} = 2048$

### 5.2 Positional Encoding (Sinusoidal)
Because the Transformer does not contain recurrent or convolutional loops, positional information is injected into token embeddings:

$$\text{PE}_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)$$

$$\text{PE}_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)$$

- Allows model to generalize to sequence lengths longer than seen during training.

---

## 6. Computational Complexity Comparison

| Layer Type | Complexity per Layer | Sequential Operations | Maximum Path Length |
| :--- | :--- | :--- | :--- |
| **Self-Attention** | $O(n^2 \cdot d)$ | $O(1)$ | $O(1)$ |
| **Recurrent (RNN)** | $O(n \cdot d^2)$ | $O(n)$ | $O(n)$ |
| **Convolutional** | $O(k \cdot n \cdot d^2)$ | $O(1)$ | $O(\log_k(n))$ |
| **Self-Attention (Restricted)** | $O(r \cdot n \cdot d)$ | $O(1)$ | $O(n/r)$ |

*Where $n$ = sequence length, $d$ = representation dimensionality, $k$ = kernel width, $r$ = neighborhood size.*

---

## 7. Training & Empirical Results

### 7.1 Setup
- **Hardware**: 8 $\times$ NVIDIA P100 GPUs.
- **Base model**: 100,000 steps (~12 hours).
- **Big model**: 300,000 steps (~3.5 days).
- **Optimizer**: Adam with $\beta_1 = 0.9$, $\beta_2 = 0.98$, $\epsilon = 10^{-9}$, with linear warmup (4000 steps) and inverse square root decay.
- **Regularization**: Residual dropout ($P_{drop} = 0.1$), label smoothing ($\epsilon_{ls} = 0.1$).

### 7.2 Results Summary
- **WMT 2014 English-to-German**: **28.4 BLEU** (Outperformed all previous state-of-the-art models and ensembles by $> 2.0$ BLEU).
- **WMT 2014 English-to-French**: **41.8 BLEU** (New single-model state-of-the-art at $< 1/4$ the training cost).
- **English Constituency Parsing**: Achieved 91.3 $F_1$ score on WSJ test set, establishing strong transferability beyond machine translation.
