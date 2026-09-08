# Lab 01 — Attention Is All You Need

แล็บนี้พาไปตั้งแต่ **เข้าใจแนวคิด → เขียนโค้ดเอง → ทดลองพิสูจน์ → วิเคราะห์ผล** ของกลไก Attention
ซึ่งเป็นหัวใจของ Transformer และของ LLM แทบทุกตัวในปัจจุบัน

## Paper

| | |
|---|---|
| Title | Attention Is All You Need |
| Authors | Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin |
| Year | 2017 (NeurIPS 2017) |
| Link | https://arxiv.org/abs/1706.03762 |

---

## เริ่มตรงนี้ (Quick Start)

```bash
# ติดตั้ง environment (ครั้งแรกครั้งเดียว)
uv sync

# เปิด Jupyter แล้วเริ่มที่ notebooks/01_concept.ipynb
uv run jupyter lab
```

โน้ตบุ๊กทุกเล่มรันได้ตั้งแต่ต้นจนจบโดยไม่ต้องมี GPU (ทดสอบบน CPU แล้ว)

---

## ลำดับการเรียน

อ่าน/รันตามลำดับนี้ แต่ละเล่มต่อยอดจากเล่มก่อนหน้าโดยตรง (เล่มหลังใช้ตัวเลขจากเล่มหน้ามาตรวจสอบซ้ำ)

| ลำดับ | ไฟล์ | เรียนรู้อะไร | เวลาโดยประมาณ |
|---|---|---|---|
| 1 | [`notebooks/01_concept.ipynb`](notebooks/01_concept.ipynb) | **ทำไม**สมการ Attention ถึงหน้าตาแบบนี้ — soft lookup, ทำไมต้องมี Q/K/V แยกกัน, ทำไมใช้ dot product, ที่มาของ `1/√d_k`, softmax saturation, ทำไมต้อง multi-head + ตัวอย่างคำนวณด้วยมือทีละขั้น | 40–60 นาที |
| 2 | [`notebooks/02_from_scratch.ipynb`](notebooks/02_from_scratch.ipynb) | เขียนเองด้วย numpy: attention, multi-head, positional encoding, **position-wise FFN, Add & Norm, padding/causal mask** แล้ว**ตรวจสอบว่าตรงกับตัวเลขที่คำนวณด้วยมือในเล่มที่ 1** | 60–75 นาที |
| 3 | [`notebooks/03_experiment.ipynb`](notebooks/03_experiment.ipynb) | ทดลองเทียบโค้ดที่เขียนเองกับ `torch.nn.functional.scaled_dot_product_attention` และพิสูจน์ว่า `Var(q·k) = d_k` จริง | 30 นาที |
| 4 | [`notebooks/04_analysis.ipynb`](notebooks/04_analysis.ipynb) | สรุปผลทั้งหมด + วิเคราะห์ว่า self-attention คุ้มกว่า RNN ตอนไหน (crossover ที่ `n = d`) | 20–30 นาที |
| 5 | [`notebooks/05_training_concepts.ipynb`](notebooks/05_training_concepts.ipynb) | รายละเอียดฝั่ง training ที่ตัดสินว่าโมเดลจะเทรนสำเร็จหรือพัง: warmup schedule, label smoothing, embedding × `√d_model`, ตำแหน่ง dropout (อธิบาย+สาธิต โดยไม่ต้อง train) | 30–40 นาที |

**ถ้าอยากอ่านสรุป paper ก่อนลงมือ** เริ่มที่ [`docs/paper-notes.md`](docs/paper-notes.md) (มีรูปจาก paper ครบ)
แต่ถ้าอยากเข้าใจแบบลงมือทำ เริ่มที่ notebook 01 ได้เลย แล้วค่อยย้อนอ่าน docs ทีหลัง

---

## สิ่งที่จะได้จากแล็บนี้

หลังจบแล็บ ควรตอบคำถามเหล่านี้ได้ด้วยตัวเอง:

- Attention ต่างจากการค้นหาแบบ dictionary (hard lookup) อย่างไร และทำไมความต่างนั้นถึงสำคัญต่อการ train
- ทำไมต้องหารด้วย `√d_k` — ถ้าไม่หารจะเกิดอะไรขึ้นกับ gradient
- Multi-head ให้ประโยชน์อะไรที่ single head ขนาดใหญ่ให้ไม่ได้ (และไม่ใช่เพราะ "parameter เยอะกว่า")
- ทำไม self-attention ถึงขนานได้ดีกว่า RNN และแลกมาด้วยอะไร
- Positional encoding แก้ปัญหาอะไร และทำไมสมการถึงใช้ sin/cos หลายความถี่
- FFN ทำหน้าที่อะไรที่ attention ทำไม่ได้ (และทำไมมันกิน parameter มากกว่า attention)
- Residual + LayerNorm แก้ปัญหาคนละอย่างกันอย่างไร
- padding mask กับ causal mask ต่างกันตรงไหน และถ้าลืมใส่จะเกิดอะไรขึ้น
- ทำไมต้อง warmup learning rate และทำไม label smoothing ถึง "ทำให้ perplexity แย่ลงแต่ BLEU ดีขึ้น"

## สิ่งที่แล็บนี้ **ไม่ได้** ครอบคลุม

ตั้งความคาดหวังให้ถูกก่อนเริ่ม:

- ❌ ไม่ได้ประกอบเป็น `EncoderLayer`/`DecoderLayer`/`Transformer` เต็มรูปแบบ
  (มีครบทุกชิ้นส่วนแล้ว แต่ยังไม่ได้ประกอบเข้าด้วยกัน)
- ❌ ไม่มี training loop จริง — weight ทั้งหมดเป็น random projection ที่ไม่ได้เทรน
- ❌ ไม่ได้ reproduce ผล BLEU score ตามที่ paper รายงาน
- ❌ ไม่มี dataset/tokenizer จริง และไม่มี inference (greedy/beam search decoding)
- ❌ ไม่ได้ทดสอบบน GPU หรือ mixed precision (`float16`/`bfloat16`)

เหตุผลและรายละเอียดอยู่ใน [`notebooks/04_analysis.ipynb`](notebooks/04_analysis.ipynb) หัวข้อ 4 (Limitations)

---

## Prerequisites

- Linear Algebra: dot product, matrix multiplication
- Softmax และแนวคิดเรื่อง gradient — *ถ้ายังไม่ชัด อ่าน [`docs/softmax.md`](docs/softmax.md) ก่อน
  (อธิบายจากศูนย์ ใช้เวลา ~15 นาที)*
- พื้นฐาน Neural Network (Linear layer, non-linearity)
- Python + numpy พื้นฐาน

ไม่จำเป็นต้องรู้ PyTorch มาก่อน (ใช้แค่ในเล่มที่ 3 เพื่อเทียบผล และมีอธิบายกำกับไว้)

---

## เอกสารประกอบ (`docs/`)

| ไฟล์ | เนื้อหา |
|---|---|
| [`softmax.md`](docs/softmax.md) | **อ่านก่อนถ้ายังไม่ชัดเรื่อง softmax** — อธิบายจากศูนย์ พร้อมตัวอย่างตัวเลขและโค้ดให้ลองเล่น (เป็นพื้นฐานที่โน้ตบุ๊ก 01 สมมติว่ารู้แล้ว) |
| [`paper-notes.md`](docs/paper-notes.md) | สรุป paper ครบทุกหัวข้อ พร้อมรูป/ตารางจาก paper: architecture, สมการ, training setup, ผล BLEU, ablation study |
| [`engineering-notes.md`](docs/engineering-notes.md) | เชื่อมแนวคิดกับระบบจริง: training throughput, context window, KV cache, ที่มาของ FlashAttention/MQA/GQA/RoPE |
| [`limitations.md`](docs/limitations.md) | ข้อจำกัดที่ผู้เขียน paper ระบุเอง แยกจากข้อสังเกตของเรา |
| [`open-questions.md`](docs/open-questions.md) | คำถามที่ยังไม่มีคำตอบ + สถานะว่าข้อไหนตอบไปแล้วบางส่วน |

## โครงสร้างโฟลเดอร์

```text
01_attention_is_all_you_need/
├── README.md          ← อยู่ตรงนี้
├── notebooks/         ← เริ่มเรียนที่นี่ (01 → 04)
├── docs/              ← สรุป paper และบันทึกเชิงวิศวกรรม
├── media/             ← asset จากตัว paper (Figure 1-3, Table 1-4 ของต้นฉบับ)
├── figures/           ← asset ที่ Python สร้าง (กราฟ/heatmap ที่ export จาก notebook)
└── artifacts/         ← ผลลัพธ์อื่น ๆ ที่ export (ยังว่าง)
```

> **`media/` vs `figures/`** — แยกกันชัดเจน: `media/` คือรูปที่มาจาก paper ต้นฉบับ (ไม่ได้สร้างเอง)
> ส่วน `figures/` คือรูปที่โค้ดใน `notebooks/` สร้างขึ้นมาเอง

โค้ดที่ใช้ซ้ำได้ถูกย้ายออกไปที่ [`shared/src/attention/`](../../shared/src/attention/) แล้ว
(ดูเหตุผลใน `notebooks/02_from_scratch.ipynb` หัวข้อ 9) พร้อม test ที่ [`tests/shared/test_attention.py`](../../tests/shared/test_attention.py)
