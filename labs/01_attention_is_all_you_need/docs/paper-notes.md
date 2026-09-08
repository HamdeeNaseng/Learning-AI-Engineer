# Paper Notes — Attention Is All You Need

## Paper Metadata

- Title: Attention Is All You Need
- Authors: Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin (Google Brain / Google Research / University of Toronto)
- Year: 2017 (NeurIPS 2017); v7 (arXiv) เพิ่มเติมภายหลัง
- Link: https://arxiv.org/html/1706.03762v7

---

## 1. ปัญหาที่ paper ต้องการแก้ (Motivation)

**Paper Finding:** สถาปัตยกรรม sequence-to-sequence เดิม (RNN, LSTM, GRU) ประมวลผลลำดับแบบ sequential
คือ hidden state ที่ตำแหน่ง `t` ต้องรอผลจากตำแหน่ง `t-1` ก่อนเสมอ ทำให้:

- ไม่สามารถขนาน (parallelize) การคำนวณภายใน training example เดียวกันได้
- เมื่อ sequence ยาวขึ้น ปัญหาเรื่อง memory และ path length ระหว่างตำแหน่งที่ห่างกันก็รุนแรงขึ้น

สำหรับ Convolutional approach (เช่น ConvS2S, ByteNet) ต้องซ้อนหลาย layer เพื่อเชื่อมตำแหน่งที่ห่างกัน
ทำให้ path length ระหว่างตำแหน่งไกล ๆ เพิ่มขึ้นแบบ linear (ConvS2S) หรือ logarithmic (ByteNet)

**Interpretation:** Transformer ถูกออกแบบมาเพื่อตัด recurrence และ convolution ออกทั้งหมด
แล้วใช้กลไก attention เป็นตัวเชื่อมทุกตำแหน่งเข้าด้วยกันโดยตรง — เป็นที่มาของชื่อ paper

---

## 2. สถาปัตยกรรม Transformer

![Figure 1: The Transformer model architecture](<../media/ModalNet-21.png>)

*Figure 1 — encoder (ซ้าย) และ decoder (ขวา) พร้อม sub-layer ทั้งหมดใน stack ขนาด N=6*

**Paper Finding (Encoder):** ซ้อน N=6 layer เหมือนกัน แต่ละ layer ประกอบด้วย 2 sub-layer:

1. Multi-Head Self-Attention
2. Position-wise Feed-Forward Network

แต่ละ sub-layer ห่อด้วย residual connection แล้วตามด้วย Layer Normalization:

```text
LayerNorm(x + Sublayer(x))
```

มิติของทุก output ในโมเดล (รวม embedding) คือ `d_model = 512`

**Paper Finding (Decoder):** ซ้อน N=6 layer เช่นกัน มี 3 sub-layer ต่อ layer:

1. Masked Multi-Head Self-Attention (กันไม่ให้เห็นตำแหน่งอนาคต เพื่อรักษาคุณสมบัติ auto-regressive)
2. Multi-Head Encoder-Decoder Attention (attend เข้าหา output ของ encoder)
3. Position-wise Feed-Forward Network

```text
Input
  ↓
Encoder (N=6 layer)
  ↓
Encoder Output  ──────┐
                       │
Target (shifted right) │
  ↓                    │
Decoder (N=6 layer, ดึง Encoder Output เข้ามาที่ sub-layer 2)
  ↓
Output Probabilities
```

---

## 3. Scaled Dot-Product Attention

![Figure 2 (left): Scaled Dot-Product Attention](<../media/ModalNet-19.png>)

**สมการ (Equation-to-Code):**

```text
Attention(Q, K, V) = softmax(QKᵀ / √d_k) V
```

Tensor shape:

```text
Q: [n_q, d_k]
K: [n_k, d_k]
V: [n_k, d_v]
      ↓
QKᵀ            → [n_q, n_k]
scale by 1/√d_k → [n_q, n_k]
softmax (แถวละ 1) → [n_q, n_k]
weighted sum ของ V → [n_q, d_v]
```

**เหตุผลของการ scale ด้วย 1/√d_k (Paper Finding):**
เมื่อ `d_k` มีค่ามาก ค่า dot product `q·k` จะมี variance สูงขึ้นตามสัดส่วนของ `d_k`
(ถ้า component ของ q, k เป็น random variable mean 0, variance 1 ที่ independent กัน
`q·k` จะมี mean 0 และ variance เท่ากับ `d_k`) ทำให้ผลลัพธ์ก่อนเข้า softmax มีขนาดใหญ่
ผลักให้ softmax ไปอยู่ในโซนที่ gradient เล็กมาก (saturated) — การหารด้วย `√d_k` ช่วยดึง scale กลับมาให้เหมาะสม

---

## 4. Multi-Head Attention

![Figure 2 (right): Multi-Head Attention](<../media/ModalNet-20.png>)

**สมการ:**

```text
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) Wᴼ
head_i = Attention(Q Wᵢ_Q, K Wᵢ_K, V Wᵢ_V)
```

**ค่าที่ paper ใช้ใน base model:** `h = 8`, `d_k = d_v = d_model / h = 64`

```text
[n, d_model=512]
      ↓ projection ต่อ head (Wᵢ_Q, Wᵢ_K, Wᵢ_V)
h=8 หัว × [n, d_k=64]
      ↓ scaled dot-product attention ต่อหัว
h=8 หัว × [n, d_v=64]
      ↓ concat
[n, h·d_v = 512]
      ↓ Wᴼ
[n, d_model=512]
```

**เหตุผลที่ใช้หลาย head (Paper Finding):** การมี attention head เดียวจะถูก "เฉลี่ย" (average)
กลบข้อมูลจาก representation subspace ที่ต่างกัน multi-head จึงเปิดให้แต่ละ head
เรียนรู้ที่จะ attend ไปยัง subspace / ตำแหน่งที่ต่างกันได้พร้อมกัน

---

## 5. รูปแบบการใช้ Attention ทั้ง 3 จุดในโมเดล

1. **Encoder self-attention** — Q, K, V มาจาก output ของ encoder layer ก่อนหน้า
   ทุกตำแหน่งมองเห็นทุกตำแหน่งในประโยคเดียวกันได้
2. **Decoder self-attention (masked)** — Q, K, V มาจาก decoder layer ก่อนหน้า
   แต่ถูก mask ไม่ให้มองเห็นตำแหน่งที่อยู่ทางขวา (อนาคต) เพื่อรักษา auto-regressive property
3. **Encoder-Decoder attention** — Q มาจาก decoder layer ก่อนหน้า, K/V มาจาก output ของ encoder
   ทำให้ decoder attend เข้าไปดูทุกตำแหน่งของ input sequence ได้

---

## 6. Position-wise Feed-Forward Network

```text
FFN(x) = max(0, x W1 + b1) W2 + b2
```

มิติ: input/output = `d_model = 512`, inner layer = `d_ff = 2048`
ใช้ parameter เดียวกันในทุกตำแหน่งของ layer นั้น (position-wise) แต่ parameter ต่างกันในแต่ละ layer

---

## 7. Positional Encoding

**สมการ (sinusoidal):**

```text
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

โดย `pos` คือตำแหน่งใน sequence และ `i` คือ index ของมิติใน embedding

**เหตุผลที่เลือก sinusoidal แทน learned embedding (Paper Finding):**
Learned positional embedding ให้ผลลัพธ์ "แทบจะเหมือนกัน" (nearly identical) กับ sinusoidal
แต่ผู้เขียนเลือก sinusoidal เพราะสมมติฐานว่าโมเดลจะเรียนรู้ที่จะ attend ตาม relative position ได้ง่ายกว่า
(เนื่องจาก `PE(pos+k)` เขียนเป็นฟังก์ชัน linear ของ `PE(pos)` ได้) และอาจ extrapolate ไปยัง sequence
ที่ยาวกว่าที่เคยเห็นตอน training ได้ดีกว่า

---

## 8. เหตุผลที่เลือก Self-Attention แทน Recurrent/Convolutional

**เกณฑ์เปรียบเทียบ 3 ข้อ (Paper Finding):**

1. Computational complexity ต่อ layer
2. จำนวน sequential operation ขั้นต่ำที่ต้องรอ (ผลต่อการ parallelize)
3. Path length สูงสุดระหว่างตำแหน่งที่ห่างกันมากที่สุดใน sequence

![Table 1: Maximum path lengths, per-layer complexity, and minimum number of sequential operations](<../media/Table 1 Maximum path lengths.png>)

| Layer Type | Complexity/Layer | Sequential Ops | Max Path Length |
|---|---|---|---|
| Self-Attention | O(n²·d) | O(1) | O(1) |
| Recurrent | O(n·d²) | O(n) | O(n) |
| Convolutional | O(k·n·d²) | O(1) | O(log_k(n)) |

**Interpretation:** self-attention แลก complexity ต่อ layer ที่สูงขึ้น (O(n²·d)) เพื่อให้ได้ sequential
operation คงที่ (O(1)) และ path length คงที่ (O(1)) — คุ้มค่าเมื่อ `n < d` ซึ่งเป็นกรณีทั่วไปของงานแปลภาษา
ที่ใช้ subword encoding (n ของ sentence มักสั้นกว่า d_model)

---

## 9. Training Setup

- **Dataset:** WMT 2014 En-De ~4.5M sentence pairs (BPE, shared vocab 37K),
  WMT 2014 En-Fr 36M sentences (word-piece vocab 32K)
- **Hardware:** เครื่องเดียว, 8× NVIDIA P100 GPU
- **เวลา training:** base model 100K steps (~12 ชั่วโมง, ~0.4 sec/step);
  big model 300K steps (3.5 วัน, ~1.0 sec/step)
- **Optimizer:** Adam, β1=0.9, β2=0.98, ε=1e-9
- **Learning rate schedule:**
  `lrate = d_model^-0.5 · min(step_num^-0.5, step_num · warmup_steps^-1.5)`, warmup_steps=4000
  (เพิ่มแบบ linear ใน 4000 step แรก แล้วลดแบบ inverse square root ของ step number)
- **Regularization:** dropout P_drop=0.1 (0.3 สำหรับ En-Fr big model), label smoothing ε_ls=0.1

---

## 10. ผลลัพธ์ (Results)

![Table 2: The Transformer achieves better BLEU scores than previous state-of-the-art models at a fraction of the training cost](<../media/Table 2 The Transformer achieves better BLEU scores.png>)

| Model | En-De BLEU | En-Fr BLEU |
|---|---|---|
| Transformer (base) | 27.3 | 38.1 |
| Transformer (big) | 28.4 | 41.8 |

Transformer (big) บน En-De ทำ BLEU ดีกว่า ensemble ที่ดีที่สุดก่อนหน้ากว่า 2.0 BLEU
และใช้ training cost (2.3×10^19 FLOPs) ต่ำกว่า GNMT+RL ensemble (1.8×10^20) และ ConvS2S ensemble (7.7×10^19)
อย่างมีนัยสำคัญ

![Table 4: The Transformer generalizes well to English constituency parsing](<../media/Table 4 The Transformer generalizes well to English constituency parsing.png>)

การทดลองเสริมด้าน English constituency parsing (4-layer Transformer):
91.3 F1 (WSJ-only), 92.7 F1 (semi-supervised — state-of-art ในเซ็ตติ้งนั้น ณ เวลานั้น)

---

## 11. Ablation Study — Variations on the Transformer Architecture

![Table 3: Variations on the Transformer architecture](<../media/Table 3 Variations on the Transformer architecture.png>)

**Paper Finding:** ผู้เขียนทดลองปรับ hyperparameter ของ base model ทีละตัว (เช่น จำนวน head `h`,
ขนาด `d_k`/`d_v`, ขนาดโมเดล, dropout, จำนวน positional encoding แบบ learned vs sinusoidal)
แล้ววัดผลกระทบต่อ BLEU และ perplexity บน development set (newstest2013) ประเด็นสำคัญที่รายงานไว้:

- ลดจำนวน head ลงเหลือ 1 (single-head) ทำให้ BLEU แย่ลงกว่า base model ที่ h=8 อย่างชัดเจน
  แต่การเพิ่ม head มากเกินไป (h=32) ก็ทำให้คุณภาพแย่ลงเช่นกัน — แสดงว่ามี "sweet spot" ของจำนวน head
- การลด `d_k` ลง (แม้จะรักษาจำนวน parameter รวมไว้เท่าเดิม) ทำให้คุณภาพโมเดลแย่ลง
  ผู้เขียนตั้งข้อสังเกตว่าการหาความเข้ากันได้ (compatibility) ระหว่าง Q/K ไม่ใช่เรื่องง่าย
  และฟังก์ชันที่ซับซ้อนกว่า dot product อาจช่วยได้
- โมเดลที่ใหญ่ขึ้น (`d_model`, `d_ff` มากขึ้น) ให้ผลลัพธ์ดีขึ้น และ dropout ช่วยลด overfitting ได้จริง
- แทนที่ sinusoidal positional encoding ด้วย learned positional embedding ให้ผล "แทบเหมือนกัน"
  กับ base model (สอดคล้องกับที่กล่าวไว้ใน [ส่วนที่ 7](#7-positional-encoding))

**Interpretation:** ผลจาก ablation นี้ชี้ว่าการออกแบบ multi-head attention ไม่ใช่แค่ "ยิ่งเยอะยิ่งดี"
แต่มีจุดสมดุลระหว่างจำนวน head กับขนาดของแต่ละ head ที่ต้องปรับให้เหมาะกับงาน — เป็นข้อมูลเชิงประจักษ์
ที่สนับสนุนเหตุผลของ multi-head attention ในส่วนที่ 4

---

## 12. Attention Visualization (Appendix)

![Figure 3: An example of the attention mechanism following long-distance dependencies in the encoder self-attention](<../media/An example of the attention mechanism.png>)

**Paper Finding:** ในภาคผนวก ผู้เขียนแสดงตัวอย่าง attention weight จริงจากโมเดลที่เทรนแล้ว
(layer 5 จาก 6) พบว่า head บางหัวเรียนรู้ที่จะ attend ตาม long-distance dependency ทางไวยากรณ์
(เช่น เชื่อมคำกริยากับ object ที่อยู่ไกลออกไปในประโยค) โดยไม่ได้ถูกบังคับให้ทำเช่นนั้นอย่างชัดเจนระหว่าง training

**Interpretation:** นี่เป็นหลักฐานเชิงคุณภาพ (qualitative) ไม่ใช่ metric เชิงปริมาณ — ใช้สนับสนุนว่า
attention weight ที่โมเดลเรียนรู้เองมีความหมายเชิงภาษาศาสตร์ (linguistically interpretable)
ในระดับหนึ่ง แต่ paper ไม่ได้วัดความสอดคล้องนี้อย่างเป็นระบบทั้งชุดข้อมูล

---

## 13. ข้อสรุปของผู้เขียน (Conclusion)

ผู้เขียนสรุปว่า Transformer เทรนได้เร็วกว่าสถาปัตยกรรมที่อิง recurrence/convolution อย่างมีนัยสำคัญ
ในขณะที่ได้คุณภาพการแปลภาษาที่ดีกว่า state-of-art เดิม และประกาศแผนจะขยายไปใช้กับ modality อื่นนอกเหนือจากข้อความ
(รูปภาพ, เสียง, วิดีโอ) รวมถึงการทดลอง restricted/local attention สำหรับ input/output ขนาดใหญ่

ดูรายละเอียดข้อจำกัดที่ผู้เขียนระบุไว้ใน [limitations.md](limitations.md)
และคำถามที่ยังเปิดอยู่ใน [open-questions.md](open-questions.md)
