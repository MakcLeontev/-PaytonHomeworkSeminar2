# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
n=int(input())
flag=True
for i in range(2,n+1):
    if flag:
        if n%i==0:
            print(i)
            flag=False

