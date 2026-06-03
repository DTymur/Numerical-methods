import sympy as sp
from sympy.abc import x, y
from math import *
import matplotlib.pyplot as plt

while True:
    try:
        f=input('Введіть функцію: ')
        sp.sympify(f)
        break
    except:
        print('Ви ввели абракадабру!')

def check(name):
    while True:
        try:
            n=float(input(f'Введіть {name}: '))
            return n
        except:
            print('Ви не ввели число')

x0=check('x0')
y0=check('y0')

while True:
    try:
        n=int(input(f'Введіть кількість кроків: '))
        if n>0:
            break
        else:
            print('крок має бути додатнім')
    except:
        print('Ви не ввели число')

while True:
    try:
        h=float(input(f'Введіть велечину кроку: '))
        if h>0:
            break
        else:
            print('крок має бути додатнім')
    except:
        print('Ви не ввели число')

F = sp.sympify(f, locals={'x': x, 'y':y, 'e': sp.E})
M1=[[x0,y0]]
X1=[x0]
Y1=[y0]

yk=y0+h*float(F.subs({x:x0, y:y0}))
for k in range (1, n+1):
    xk=x0+k*h
    yk1=yk+h*float(F.subs({x:xk, y:yk}))
    row1=[]
    row1.append(xk)
    row1.append(yk)
    M1.append(row1)
    X1.append(xk)
    Y1.append(yk)
    yk=yk1
print('пари xk, yk для Ейлера', M1)

M2=[]
X2=[]
Y2=[]
for m in range (n+1):
    xm=x0+m*h
    K1 = float(F.subs({x: xm, y: y0}))
    K2 = float(F.subs({x: xm + h / 2, y: y0 + K1 * h / 2}))
    K3 = float(F.subs({x: xm + h / 2, y: y0 + K2 * h / 2}))
    K4 = float(F.subs({x: xm + h, y: y0 + K3 * h}))
    ym = y0 + h / 6 * (K1 + 2*K2 + 2*K3 + K4)
    row2 = []
    row2.append(xm)
    row2.append(y0)
    M2.append(row2)
    X2.append(xm)
    Y2.append(y0)
    y0 = ym
print('пари xk, yk для Рунге-Кутти', M2)

plt.plot(X1, Y1, 'o-', label="Ейлер")
plt.plot(X2, Y2, 'o-', label="Рунге-Кутти")

plt.grid()
plt.legend()
plt.show()
