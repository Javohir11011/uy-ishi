import os
os.system("cls")

'''
3-masala. IT-COMPANY

Faylda bir nechta qatoridan iborat IT kompaniya hodimlari to'g'risidagi ma'lumot yozilgan. 
Har bir qatorida IT kompaniya hodimining ismi, lavozimi, oyligi, oyligiga bonus summa va 
qaysi bo'limda ishlashi. Ushbu ma'lumotlar ichidan bonuslari orasida musbat va manfiy qiymatlar 
mavjud. Kompaniyada yaxshi ishlaganlar bonusi musbat, yomon ishlaganlar uchun manfiy qiymatlar 
bilan to'ldirilgan. Sizning vazifangiz yaxshi ishlagan hodimlar ko'proq qaysi bo'limda ishlashini aniqlang. 
Agar shunday bo'limlar ko'p bo'lsa, hammasini chiqaring.

Eslatma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga 
past ball qo'yiladi.

Input (Faylning ichidagi ma'lumot)  Output (Chi'quvchi ma'lumot)
Anvar Junior 500 100 1-bo'lim  2-bo'lim
Asror Middle 1500 500 2-bo'lim  
Kamola Senior 2500 -100 3-bo'lim  
Vali Junior 500 -100 1-bo'lim  
Davron Middle 1500 100 2-bo'lim  
Bahodir Senior 2500 300 3-bo'lim  
Farrux Junior 500 100 1-bo'lim  
Jamila Middle 1500 200 2-bo'lim  
Jasur Senior 2500 300 3-bo'lim  
Komila Junior 500 -100 1-bo'lim  
Anvar Junior 500 100 1-bo'lim  2-bo'lim
Asror Middle 1500 500 2-bo'lim  3-bo'lim
Kamola Senior 2500 100 3-bo'lim  
Vali Junior 500 -100 1-bo'lim  
Davron Middle 1500 100 2-bo'lim  
Bahodir Senior 2500 300 3-bo'lim  
Farrux Junior 500 100 1-bo'lim  
Jamila Middle 1500 200 2-bo'lim  
Jasur Senior 2500 300 3-bo'lim  
Komila Junior 500 -100 1-bo'lim
'''


lst = []
with open("file.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
# print(data)                    
for i, val in enumerate(data):
    data[i] = val.split(" ")
    if int(data[i][3]) > 0:
        lst.append(int(data[i][-1][0]))
print(lst)
def funk(lst):
    dik = {}
    for i in lst:
        if i in dik:
            dik[i] += 1
        else:
            dik[i] = 1
    katta =  max(dik.values())
    kop = [i for i, val in dik.items() if val == katta]
    return kop

print(funk(lst))