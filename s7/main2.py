import os
os.system("cls")
'''
2-masala. ELECTION
Foydalanuvchi tomonidan Dictionaryga keyga ismlar va valuega esa Boolean type (1 yoki 0) kiritadi. 
Sizning vazifangiz eng ko'p ovoz berganlarning ismlarini chiqarish. Agar durang bo'lsa, ikkalisini 
ham chiqarish kerak. Chiqishda birinchi qatorda qaysi qiymat ko'p ovoz berilganini va keying qatorda 
esa ismlarni chiqarish kerak. Ma'lumotlar chiqishini ma'nunada keltirilgandek bo'lishi kerak.

Eslatma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga 
past ball qo'yiladi.

Input (Kiruvi ma'lumot)     `                                                       Output (Chiquvchi ma'lumot)
{'Anvar': 1, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}  1 \n Anvar Lobar Vali Baxtiyor
{'Anvar': 0, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}  0 \n Lobar Vali Baxtiyor
{'Anvar': 0, 'Lobar': 0, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}  0 \n Vali Baxtiyor
{'Anvar': 0, 'Lobar': 0, 'Asror': 0, 'Vali': 0, 'Surayyo': 1, 'Baxtiyor': 0}  0 \n Asror Surayyo

'''
dic = {}
for i in range(3):
    k = input("ism : ")
    b = int(input("1 or 0 ->"))
    dic[k] = b
# print(dic)
sana1 = 0
sana0 = 0
for k, v in dic.items():
    if v == 1:
        sana1 += 1
    elif v == 0:
        sana0 += 1
# print(sana1)
# print(sana0)
if sana1 > sana0:
    print("1")
    for i, val in dic.items():
        if val == 1:
            print(i, end = ' ')
elif sana1 < sana0:
    print("0")
    for i, val in dic.items():
        if val == 0:
            print(i,end = ' ')
else:
    print("0")
    for i, val in dic.items():
        if val == 0:
            print(i,end = ' ')
    print("1")
    for i, val in dic.items():
        if val == 1:
            print(i,end = ' ')


        


