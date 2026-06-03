import random
import sympy as sp
from sympy.abc import x

while True:
    try:
        n = int(input('Введіть кількість чисел: '))
        break
    except:
        print('Ви не ввели число')


while True:
    choice = input('Ви хочете вводити числа в ручну чи випадково? ').lower()
    if choice not in ['вручну', 'самостійно', 'dhexye', 'випадково', 'рандомно', 'dbgflrjdj']:
        print('Такої відповіді немає')
    else:
        break

Mx=[]
My=[]
if choice=='вручну' or choice=='самостійно' or choice=='dhexye':
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

if choice=='випадково' or choice=='рандомно' or choice=='dbgflrjdj':
    for i in range(n):
        xk = random.uniform(-20,20)
        yk = random.uniform(-20,20)
        Mx.append(xk)
        My.append(yk)
print('Mx - ', Mx)
print('My - ', My)

C1=[]
def X2(a):
    S1 = 1
    for i in range(n):
        if a-Mx[i]!=0:
            S1*=a-Mx[i]
    return C1.append(S1)

for i in range(n):
    X2(Mx[i])
print(C1)

C2=[]
for i in range(n):
    k=My[i]/C1[i]
    C2.append(k)
print(C2)

C3=[]
for i in  range(n):
    S3=1
    for j in range(n):
        if i!=j:
            S3*=x-Mx[j]
    C3.append(sp.expand(S3))
print(C3)

Lk=[]
for i in range(n):
    Lk.append(C2[i]*C3[i])
print('L(x)=', sum(Lk))

def L(a):
    return sum(Lk).subs({x:a})
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

        print(f"L({xkk})={L(xkk)}")
    if choice2=='ys' or choice2=='ні':
        break
