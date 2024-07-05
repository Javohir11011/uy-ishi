import os
os.system("cls")

lst = [-1, 2, 3, -1, -2]

for son in range(len(lst) - 1):
    if (lst[son] > 0 and lst[son + 1] > 0) or (lst[son] < 0 and lst[son + 1] < 0):
        print(lst[son], lst[son + 1])
