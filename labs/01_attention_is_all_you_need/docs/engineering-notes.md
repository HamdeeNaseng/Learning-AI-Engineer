# Engineering Notes — Attention Is All You Need

เอกสารนี้เชื่อมโยงแนวคิดใน paper เข้ากับผลกระทบเชิงวิศวกรรมต่อระบบจริง
(ดู paper facts ทั้งหมดใน [paper-notes.md](paper-notes.md))

---

## 1. Parallelization → Training Throughput

**Engineering Implication:** เพราะ self-attention มี sequential operation ที่ O(1) (ไม่ต้องรอ
ตำแหน่งก่อนหน้าเหมือน RNN) ทุกตำแหน่งใน sequence จึงคำนวณพร้อมกันได้บน GPU/TPU เต็มรูปแบบ
นี่คือเหตุผลที่ base model เทรนจบใน ~12 ชั่วโมงบน 8× P100 เทียบกับ RNN/LSTM ที่ต้อง unroll ทีละ timestep
ผลคือ **training throughput** (samples/sec, tokens/sec) สูงขึ้นมากในสเกลเดียวกันของ compute

## 2. O(n²·d) Complexity → Context Window เป็นข้อจำกัดเชิงวิศวกรรม

**Engineering Implication:** การแลก sequential op คงที่มาด้วย complexity ต่อ layer ที่เป็น O(n²·d)
หมายความว่าเมื่อ sequence length (`n`) ยาวขึ้น ต้นทุนการคำนวณและหน่วยความจำของ attention matrix
(`n × n`) โตแบบ quadratic — นี่คือรากของปัญหาที่งานยุคหลัง (FlashAttention, sparse/local attention,
sliding window attention) พยายามแก้ไข เพื่อให้ context window ยาวขึ้นได้โดยไม่ระเบิด VRAM

## 3. Q/K/V Projection และ KV Cache ตอน Inference

**Engineering Implication:** ในช่วง autoregressive decoding ค่า K และ V ของตำแหน่งที่ผ่านมาแล้ว
ไม่เปลี่ยนแปลง ระบบ serving จริงจึงแคชค่าเหล่านี้ไว้ (**KV Cache**) เพื่อไม่ต้องคำนวณ K/V ซ้ำทุก token
สิ่งนี้เป็นรากฐานของงานด้าน inference optimization รุ่นหลัง เช่น PagedAttention (vLLM),
Multi-Query Attention (MQA), Grouped-Query Attention (GQA) ที่ลดขนาด KV cache ลง
เพื่อเพิ่ม batching efficiency และ throughput ตอน serving

## 4. Multi-Head Attention → Representation Diversity บน Hardware เดียวกัน

**Engineering Implication:** การแบ่งเป็น h=8 head ที่มี d_k=d_v=64 แทนที่จะใช้ 1 head ขนาด d_model=512
ไม่ได้เพิ่ม parameter count หรือ FLOPs โดยรวมมากนัก (เพราะ compute ต่อ head เล็กลงตามสัดส่วน)
แต่ในทางปฏิบัติ multi-head ต้องการการ implement ที่ระวังเรื่อง memory layout (reshape/transpose)
ให้แต่ละ head คำนวณแบบ batched matrix multiplication ได้อย่างมีประสิทธิภาพบน GPU

## 5. Residual Connection + LayerNorm → Trainability ที่ความลึกมาก

**Engineering Implication:** ด้วย N=6 layer (และในงานยุคหลังไปถึงหลักร้อย layer) residual connection
และ layer normalization เป็นกลไกที่ทำให้ gradient ไหลผ่านโมเดลลึก ๆ ได้โดยไม่ vanish/explode
เป็นแพทเทิร์นที่โมเดลยุคหลัง (GPT, BERT) สืบทอดมาโดยตรง

## 6. Sinusoidal Positional Encoding → Extrapolation ความยาว sequence

**Engineering Implication:** เพราะ sinusoidal PE ไม่มี parameter ให้เรียนรู้ ทฤษฎีคือโมเดลควร
extrapolate ไปยัง sequence ที่ยาวกว่าที่เห็นตอน training ได้ — ในทางปฏิบัติแนวทางนี้ยัง extrapolate
ได้จำกัด และเป็นแรงจูงใจของงาน positional encoding รุ่นหลัง เช่น RoPE (Rotary Positional Embedding),
ALiBi ที่ออกแบบมาเพื่อรองรับ context length ที่ยาวกว่าตอน training ได้ดีขึ้น

## 7. Training Cost vs. Model Quality

**Engineering Implication:** ตัวเลข FLOPs ที่ paper รายงาน (Transformer big ใช้ compute น้อยกว่า
ensemble ของ GNMT+RL และ ConvS2S อย่างมาก) แสดงถึง **compute efficiency** ไม่ใช่แค่ accuracy
เพียงอย่างเดียว — เป็นประเด็นสำคัญเวลาตัดสินใจเลือกสถาปัตยกรรมในงบ compute ที่จำกัด
ซึ่งเป็นจุดตั้งต้นของแนวคิด scaling law ในงานยุคหลัง (Kaplan et al., Chinchilla)

---

## สรุปสำหรับ AI/Software/Research Engineer

Transformer ไม่ได้แค่ "แม่นกว่า" RNN/CNN เดิม แต่เปลี่ยนโจทย์ทางวิศวกรรมทั้งหมด: จาก
"ทำอย่างไรให้ sequential computation เร็วขึ้น" เป็น "ทำอย่างไรให้ O(n²) attention คุ้มค่าและ scale ได้"
โจทย์หลังนี้คือแกนกลางของงานวิจัยด้าน efficient attention, long-context modeling และ inference
serving ตลอด 2018–ปัจจุบัน
