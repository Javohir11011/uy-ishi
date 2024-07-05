"""
6-masala. SORTING

My_sort nomli funksiya yarating va ushbu funksiyaga parameter sifatida faqat butun sonlardan iborat List ma'lumotlari beriladi. Sizning vazifangiz bu funksiyaga qiymat qaytarish sifatida Listning har bir elementlarining raqamlar yig'indisi bo'yicha o'sish tartibida saralash kerak. Foydalanuvchi List elementlariga faqat musbat sonlar kirita oladi va shuni shartini ham exception orqali tekshirib oling.

Eslatma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo'yiladi.

Input (Kiruvchi ma'lumot)  Output (Chi'quvchi ma'lumot)
My_sort([14, 30, 103])    [30, 103, 14]
My_sort([5, 31, 123, 80, 11])  [11, 31, 5, 123, 80]


"""


import os
os.system("cls")
def sow(lst):
    a = sorted(lst, key=funk)
    return a
def funk(son):
    return sum(int(i) for i in str(son))

n = int(input("n = "))
i = 0
list2 = []
while i < n:
    try:
        son = int(input(f"{i + 1} son -- "))        
        if son < 0:
            raise ValueError("Musbat son kiriting")
        list2.append(son)
        i += 1
    except ValueError as e:
        print(e)
sortt = sow(list2)
print(sortt)