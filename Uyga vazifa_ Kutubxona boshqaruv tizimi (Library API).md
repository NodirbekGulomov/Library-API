**Uyga vazifa: Kutubxona boshqaruv tizimi (Library API)**

Kutubxona uchun oddiy backend API ishlab chiqing.

Tizimda kitoblar saqlanishi va boshqarilishi kerak.

**Talablar**

* Backend FastAPI yordamida yozilishi kerak.  
* Ma'lumotlar bazasi bilan ishlash uchun SQLAlchemy ishlatilishi kerak.  
* Request va Response modellari uchun Pydantic ishlatilishi kerak.

**Quyidagi API larni yaratishiz kerak**

1\. Kitob qo'shish

Foydalanuvchi yangi kitob qo'sha olishi kerak.

Har bir kitob kamida quyidagi ma'lumotlarga ega bo'lishi kerak:

* nomi  
* muallifi  
* nashr yili  
* sahifalar soni

---

2\. Barcha kitoblarni ko'rish

Tizimdagi barcha kitoblarni olish imkoniyati bo'lishi kerak.

---

3\. Bitta kitob haqida ma'lumot olish

ID orqali bitta kitob ma'lumotlarini olish mumkin bo'lishi kerak.

Agar kitob topilmasa mos xatolik qaytarilishi kerak.

---

4\. Kitob ma'lumotlarini tahrirlash

Mavjud kitob ma'lumotlarini yangilash mumkin bo'lishi kerak.

---

5\. Kitobni o'chirish

Mavjud kitobni o'chirish mumkin bo'lishi kerak.

---

6\. Qidiruv

Kitoblarni muallif nomi bo'yicha qidirish imkoniyati bo'lishi kerak. Bunda qidiruv sozi query param sifatida yuborilishi kerak

