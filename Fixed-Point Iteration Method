import sympy as sp
from sympy.abc import x, y
from math import *

while True:
    try:
        e = float(input('Введіть до якої точності буде обчислення:'))
        if 0 < e < 1:
            break
        else:
            print('Точність має бути більше 0 і менше 1')
    except ValueError:
        print('Ви не ввели число або ввели неправильний вид числа')

def F1(x,y):
    return eval(f1)
def F2(x,y):
    return eval(f2)

while True:
    try:
        f1=input('Введіть f1 для х: ')
        F1(0,0)
        break
    except ZeroDivisionError:
        break
    except:
        print('Ви ввели абракадабру!')


while True:
    try:
        f2=input('Введіть f2 для y: ')
        F2(0, 0)
        break
    except ZeroDivisionError:
        break
    except:
        print('Ви ввели абракадабру!')

M1diff=[]
M2diff=[]

fsp1=sp.sympify(f1)
fsp2=sp.sympify(f2)
diffx1 = sp.diff(fsp1, x)
diffy1 = sp.diff(fsp1, y)

M1diff=[diffx1,diffy1]

diffx2 = sp.diff(fsp2, x)
diffy2 = sp.diff(fsp2, y)

M2diff=[diffx2, diffy2]

print(M1diff)
print(M2diff)

while True:
    S=[]
    try:
        x0=float(input('Введіть початковий х0: '))
        y0=float(input('Введіть початковий у0: '))

    except:
            print('Ви не ввели число')
            continue

    try:
        a1x=M1diff[0].subs({x: x0, y: y0}).evalf()
        a2x=M2diff[0].subs({x: x0, y: y0}).evalf()
        if not isfinite(float(a1x)) or not isfinite(float(a2x)):
            print('Похідні по x нечислові у цій точці дають нескінченість або NaN')
            continue
        Sx=abs(a1x)+abs(a2x)
        S.append(Sx)
    except:
        print('Похідна по х від якоїсь з функцій не існує у х0')
        continue


    try:
        a1y = M1diff[1].subs({x: x0, y: y0}).evalf()
        a2y = M2diff[1].subs({x: x0, y: y0}).evalf()
        if not isfinite(float(a1y)) or not isfinite(float(a2y)):
            print('Похідні по y нечислові у цій точці дають нескінченість або NaN')
        Sy = abs(a1y) + abs(a2y)
        S.append(Sy)
    except:
        print('Похідна по у від якоїсь з функцій не існує у у0')
        continue

    print(S)

    q=max(S)
    print(q)

    if Sx<1 and Sy <1:
        print ('x0, y0 підходять')
        break
    else:
        print ('x0, y0 не підходять')
        print()

while True:
    B=[]
    xk=fsp1.subs({x: x0, y: y0})
    yk=fsp2.subs({x: x0, y: y0})
    B.append(abs(xk - x0))
    B.append(abs(yk - y0))
    x0=float(xk)
    y0=float(yk)

    if (q/(1-q))*max(B)<e:
        print(f"x={x0}, y={y0} - приблизні розв'язки")
        break
