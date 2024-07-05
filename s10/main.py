'''
1-masala.

Tasavvur qiling-a, sizda berilgan naqshga muvofiq turli xil ranglar bilan toʻldirishingiz kerak boʻlgan kvadratchalar qatori bor.
 Kvadratchalarni ketma-ket boʻyash kerak, ya’ni keyingi kvadrat boshqa rangda boʻlsa, qalamni oʻzgartirishingiz kerak boʻladi.

Eslatma: Barcha ma’lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qoʻyiladi.

Ranglar roʻyxatini oladigan va butun naqshni toʻldirish uchun zarur boʻlgan vaqtning qiymatini (soniyalarda) qaytaradigan funksiyani yozing. Bunda:
- qalamni almashtirish uchun 1 soniya kerak boʻladi
- kvadratni toʻldirish uchun 2 soniya kerak boʻladi

Input (Kiruvchi ma’lumot)                                 Output (Chi'quvchi ma’lumot)
naqsh(["Red", "Blue", "Red", "Blue", "Red"])                 14
naqsh(["Blue"])                                              2
naqsh(["Red", "Yellow", "Green", "Blue"])                    11
naqsh(["Blue", "Blue", "Blue", "Red", "Red"])                13


'''
import os
os.system("cls")

rang = input("rang kiting: ")
k = rang.split(" ")
print(k)
vaqt  = 2
for i in range(1, len(k)):
    if k[i] != k[i - 1]:
        vaqt += 3
    else:
        vaqt += 1
print(vaqt)