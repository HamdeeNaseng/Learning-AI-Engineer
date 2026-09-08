# Open Questions — Attention Is All You Need

คำถามเหล่านี้ยังไม่ได้ตอบจาก paper ฉบับนี้โดยตรง เหมาะสำหรับต่อยอดใน lab notebook หรือ lab ถัดไป

## เกี่ยวกับกลไกภายในโมเดล

1. ถ้าลด `d_k` ลงจนต่ำมาก (เช่น 8 หรือ 16) ผลของการ scale ด้วย `1/√d_k` ต่อ gradient flow
   จะยังช่วยได้เท่าเดิมหรือไม่? ควรทดลองวัด variance ของ pre-softmax logits จริงเทียบกับทฤษฎี
2. Multi-head แต่ละหัวเรียนรู้ pattern ที่ต่างกันจริงหรือไม่ (เช่น head หนึ่งจับ syntax, อีก head จับ
   long-range dependency)? ต้องอาศัย attention visualization เพื่อตรวจสอบเชิงประจักษ์
3. Sinusoidal positional encoding vs. learned positional embedding: paper บอกว่าผลลัพธ์
   "แทบเหมือนกัน" ในสเกลที่ทดลอง — พฤติกรรม extrapolation ไปยัง sequence ที่ยาวกว่า training
   จริง ๆ แล้วต่างกันแค่ไหน? (เชื่อมโยงกับ lab 20_rope และ 21_alibi ในอนาคต)

## เกี่ยวกับ scaling และ efficiency

4. ที่ n < d ผู้เขียนอ้างว่า self-attention เร็วกว่า recurrent layer — จุดตัด (crossover point)
   ที่ n เริ่มมากกว่า d จนทำให้ recurrent/convolutional คุ้มกว่าอยู่ที่ sequence length เท่าไหร่
   ในทางปฏิบัติบน hardware ปัจจุบัน?
   **ตอบบางส่วนแล้ว** ใน [`../notebooks/04_analysis.ipynb`](../notebooks/04_analysis.ipynb) หัวข้อ 2:
   เชิง operation-count ล้วน (ไม่นับผลของ parallelization) crossover อยู่ที่ `n = d` พอดี (แก้จาก
   `n²d = nd²`) แต่นี่เป็นการวิเคราะห์เชิงทฤษฎีจากสูตร Big-O เท่านั้น **ยังไม่ได้วัด latency จริงบน
   hardware** ซึ่งต้องพึ่ง benchmark จริง (เชื่อมกับคำถามข้อ 5 ด้านล่าง) — ส่วน "ในทางปฏิบัติ" ของคำถามนี้
   จึงยังเปิดอยู่
5. O(n²·d) complexity หมายถึงต้นทุนจะโตเร็วแค่ไหนเมื่อ context length เพิ่มจาก 512 → 4096 → 32768?
   ควรวัดจริงด้วย benchmark (latency, VRAM) แทนการคำนวณ complexity เชิงทฤษฎีอย่างเดียว
   (เชื่อมโยงกับ lab 18_flashattention, 19_flashattention2)

## เกี่ยวกับ engineering implication

6. KV cache growth ต่อ token ที่เพิ่มขึ้นระหว่าง decoding ส่งผลต่อ throughput การ serving แบบ
   batch อย่างไร และ MQA/GQA (lab 22, 23) แก้ปัญหานี้ได้มากแค่ไหนเทียบกับ multi-head attention
   original ใน paper นี้?
7. Layer normalization ในตำแหน่ง post-norm (ตามที่ paper ใช้) เทียบกับ pre-norm ที่โมเดลยุคหลัง
   นิยมใช้ ต่างกันอย่างไรในแง่ training stability ที่ความลึกมาก?

## สถานะ

Implementation และ experiment ใน `notebooks/01`–`04` เสร็จสมบูรณ์แล้ว คำถามข้อ 4 ตอบได้บางส่วน
(เชิงทฤษฎี) ส่วนคำถามข้อ 1–3, 5–7 ยังเปิดอยู่ทั้งหมด เพราะต้องมี trained model จริงหรือ benchmark
บน hardware จริง ซึ่งอยู่นอกขอบเขตของ lab นี้ (ดู [engineering-notes.md](engineering-notes.md)
และ [`../notebooks/04_analysis.ipynb`](../notebooks/04_analysis.ipynb) สำหรับบริบทเต็ม)
