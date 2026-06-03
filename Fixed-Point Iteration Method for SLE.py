while True:
    try:
        e = float(input('Введіть до якої точності буде обчислення:'))
        if 0 < e < 1:
            break
        else:
            print('Точність має бути більше 0 і менше 1')
    except ValueError:
        print('Ви не ввели число або ввели неправильний вид числа')

n = int(input("Введіть кількість невідомих: "))
print("Вводіть коефіцієнти та вільні члени")
while True:
    M = []
    for i in range(n):
        row=[]
        for j in range(n+1):
            xi = float(input())
            row.append(xi)
        M.append(row)

    for i in range(n):
        for j in range(n):
            if i == j:
                M[i][j] = 0

    Si=[]
    for i in range(n):
        S = 0
        for j in range(n):
            S+=abs(M[i][j])
        Si.append(S)
    if max(Si)>=1:
        print("СЛР не збігається, перзапишіть данні")
        print()
    else:
        break


Mk = []
for i in range(n):
    Mk.append(M[i][n])
print(Mk)

Mkk=[]
for i in  range(n):
    K=[]
    for j in range(n):
        K.append(M[i][j]*Mk[j])
        a=Mk[i]
    Mkk.append(a+sum(K))
print(Mkk)

while True:
    Mk1 = []
    for i in range(n):
        K1 = []
        for j in range(n):
            K1.append(M[i][j] * Mkk[j])
            b=Mk[i]
        Mk1.append(b+sum(K1))
    kk=Mkk
    Mkk=Mk1
    print(Mkk)
    print(kk)
    B=[]
    for i in range(n):
        B.append(abs(kk[i]-Mkk[i]))
    if max(B)<e:
        print(Mkk, " - приблизні розв'язки СЛР")
        break
