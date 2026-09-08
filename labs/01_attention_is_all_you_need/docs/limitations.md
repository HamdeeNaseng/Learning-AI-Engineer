# Limitations — Attention Is All You Need

## ข้อจำกัดที่ผู้เขียนระบุไว้เอง (Author-Stated)

- **Quadratic complexity:** self-attention มี complexity ต่อ layer เป็น O(n²·d) ผู้เขียนเสนอว่า
  self-attention อาจ "restricted to considering only a neighborhood of size r" เพื่อลด max path
  length เหลือ O(n/r) สำหรับ sequence ที่ยาวมาก และระบุว่า "we plan to investigate this approach
  further in future work" — กล่าวคือ paper ฉบับนี้ **ไม่ได้ทดลอง** local/restricted attention จริง
  เป็นเพียงทิศทางที่เสนอไว้
- **จำกัดอยู่ที่ text modality:** การทดลองทั้งหมดในฉบับนี้เป็นงาน machine translation และ constituency
  parsing เท่านั้น ยังไม่มีการทดลองกับ image, audio, video

## ข้อจำกัดที่สังเกตได้จากขอบเขตการทดลอง (Observed, ไม่ใช่คำกล่าวของผู้เขียนโดยตรง)

- **Sequence length ที่ทดสอบ:** ผลลัพธ์ BLEU ที่รายงานมาจาก sentence-level translation
  (WMT 2014 En-De/En-Fr) ซึ่งความยาว sequence โดยทั่วไปสั้นกว่า long-document หรือ long-context
  use case ที่พบในงานยุคหลัง — paper ไม่ได้วัด behavior ที่ context length ยาวมาก ๆ
- **Hardware เดียว:** ผลลัพธ์ด้าน training time (12 ชั่วโมง / 3.5 วัน) วัดบน 8× P100 เครื่องเดียว
  เท่านั้น ยังไม่มีการเปรียบเทียบ scaling behavior ข้าม hardware generation หรือ multi-node

## Interpretation (มุมมองเชิงวิศวกรรม ไม่ใช่ finding จาก paper)

ข้อจำกัดเรื่อง O(n²·d) ที่ผู้เขียนระบุไว้เอง กลายเป็นหัวข้อวิจัยหลักของวงการในช่วงหลายปีถัดมา
(FlashAttention, sparse attention, linear attention, sliding-window attention) — การที่ผู้เขียน
เห็นข้อจำกัดนี้ตั้งแต่ต้นและระบุไว้ตรง ๆ ใน paper มีคุณค่าเชิงประวัติศาสตร์ในการเข้าใจว่างานวิจัยด้าน
efficient attention ต่อยอดจากจุดไหน

ดูคำถามเปิดที่เกี่ยวข้องใน [open-questions.md](open-questions.md)
