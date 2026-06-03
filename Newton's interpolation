import sympy as sp
from sympy.abc import x, q
from math import *

while True:
    try:
        n = int(input('Введіть кількість чисел: '))
        break
    except:
        print('Ви не ввели число')

Mx=[]
My=[]
while True:
    for i in range(n):
            while True:
                try:
                    xk = float(input('Введіть х: '))
                    break
                except:
                    print('Ви не ввели число')

            while True:
                try:
                    yk = float(input('Введіть y: '))
                    break
                except:
                    print('Ви не ввели число')
            Mx.append(xk)
            My.append(yk)
    ok=True
    if len(Mx)>=3:
            for t in range(0,n-2):
                    if Mx[t+1]-Mx[t]!=Mx[t+2]-Mx[t+1]:
                        print('Різниця між х має бути сталою, перезапишіть дані ')
                        Mx.clear()
                        My.clear()
                        ok=False
                        break
    if ok==False:
        continue
    break

print('всі х - ', Mx)
print('всі у - ', My)

y0=My[0]
T=[]
K=[]
m=n
for i in range(m):
    row=[]
    for j in range (m-1):
            dety=My[j+1]-My[j]
            row.append(dety)
    My=row
    m=m-1
    T.append(row)
    K.append(row[0])
    if m==1:
        break
print('таблиця дельта у - ', T)
print('дельта у0 - ', K)

q1=(x-Mx[0])/(Mx[1]-Mx[0])
C1=[]
S1 = 1
for i in range(n-1):
    S1*=(q1-i)
    C1.append(K[i]*S1/factorial(i+1))

C2=[]
S2 = 1
for i in range(n-1):
    S2*=(q-i)
    C2.append(K[i]*S2/sp.factorial(i+1, evaluate=False))

print()
S3=y0+sum(C1)
print('P(x) де все крім дужок перемножено й додано - ', S3)
print()
S4=y0+sum(C2)
print('P(x) через q та факторіал - ', S4)
print()

def P(a):
    return S3.subs({x:a})
while True:
    while True:
        choice2=input("Чи хочете ви перевірити функцію підставивши в неї xk? ").lower()
        if choice2 not in ['nfr','так' ,'ys' ,'ні']:
            print('Немає такої відповіді')
        else:
            break

    if choice2=='nfr' or choice2=='так':
        while True:
            try:
                xkk=float(input('xk='))
                if xkk in Mx:
                    break
                else:
                    print('xk має бути серед тих, що ви вводили')
            except:
                print('Ви не ввели число')

        print(f"P({xkk})={P(xkk)}")
    if choice2=='ys' or choice2=='ні':
        break
