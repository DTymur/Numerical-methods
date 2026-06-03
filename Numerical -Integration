import sympy as sp
from sympy.abc import x
from math import *

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
            n=float(input(f'Введіть межу {name}: '))
            return n
        except:
            print('Ви не ввели число')

a=check('a')
b=check('b')

while True:
    try:
        n=int(input(f'Введіть кількість відрізківі: '))
        if n>0 and n%2==0:
            break
        else:
            print('Відрізків має бути натуральна парна кількість')
    except:
        print('Ви не ввели число')

S1 = 0
F = sp.sympify(f, locals={'x': x, 'e': sp.E})

for k in range(1, n + 1):
    xk = a + k * ((b - a) / n)
    if F.subs({x: xk}).has(sp.nan):
        continue
    S1 += F.subs({x: xk})

print('Приблизна площа інтегралу методом прямокутників', format(float(S1 * (b - a) / n), '.10f'))

h = (b - a) / n
S2 = 0

for k in range(1, n):
    if F.subs({x: a + k * h}).has(sp.nan):
        continue
    S2 += F.subs({x: a + k * h})


print()
print('Приблизна площа інтегралу методом трапецій',
      format(float((h/ 2) * (F.subs({x: a}) + F.subs({x: b})) + S2 * h), '.10f'))

Sev = 0
for k in range(2, n, 2):
    if F.subs({x: a + k * h}).has(sp.nan):
        continue
    Sev += F.subs({x: a + k * h})

Sodd = 0
for k in range(1, n, 2):
    if F.subs({x: a + k * h}).has(sp.nan):
        continue
    Sodd += F.subs({x: a + k * h})

print()
print('Приблизна площа інтегралу методом Сімпсона',
      format(float((h / 3) * (F.subs({x: a}) + F.subs({x: b}) + 2 * Sev + 4 * Sodd)), '.10f'))
