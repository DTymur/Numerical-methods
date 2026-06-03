from math import *
import sympy as sp

def f(x):
    return eval(func)
while True:
    try:
        func=input('Введіть функцію:')
        r1=f(1)
        break
    except NameError:
        print('Ви ввели абракадабру, введіть функцію')
    except:
        break

while True:
    try:
        e = float(input('Введіть до якої точності буде обчислення:'))
        if 0 < e < 1:
            break
        else:
            print('Точність має бути більше 0 і менше 1')
    except ValueError:
        print('Ви не ввели число або ввели неправильний вид числа')


while True:
    try:
        a=float(input('Введіть нижню межу (а):'))
        break
    except:
        print('Ви не ввели число')

while True:
    try:
        b=float(input('Введіть верхню межу (b):'))
        break
    except:
        print('Ви не ввели число')

while True:
    try:
        r2=f(a)
        break
    except:
        print('Функція не існує у точці а, введіть межу заново')
    while True:
        try:
            a = float(input('Введіть нижню межу (а):'))
            break
        except:
            print('Ви не ввели число')

while True:
    try:
        r3=f(b)
        break
    except:
        print('Функція не існує у точці b, введіть межу заново')
    while True:
        try:
            b = float(input('Введіть нижню межу (b):'))
            break
        except:
            print('Ви не ввели число')


while True:

    if f(a)*f(b)>0:
        ans=input('Функція або межі не підходять, що ви хочете змінити?  ').lower()
        if ans== 'функцію' or ans=='function':
            while True:
                try:
                    func = input('Введіть нову функцію:')
                    r1 = f(1)
                    break
                except NameError:
                    print('Ви ввели абракадабру, введіть функцію')
                except:
                    break
            continue
        if ans == 'межі':
            while True:
                try:
                    a = float(input('Введіть нову нижню межу (a): '))
                    b = float(input('Введіть нову верхню межу (b): '))
                    fa = f(a)
                    fb = f(b)
                    if fa * fb < 0:
                        break
                    else:
                        while True:

                            if f(a) * f(b) > 0:
                                ans = input('Функція або межі не підходять, що ви хочете змінити?  ').lower()
                                if ans == 'функцію' or ans == 'function':
                                    while True:
                                        try:
                                            func = input('Введіть нову функцію:')
                                            r1 = f(1)
                                            break
                                        except NameError:
                                            print('Ви ввели абракадабру, введіть функцію')
                                        except:
                                            break
                                    continue
                                if ans == 'межі':
                                    while True:
                                        try:
                                            a = float(input('Введіть нову нижню межу (a): '))
                                            b = float(input('Введіть нову верхню межу (b): '))
                                            fa = f(a)
                                            fb = f(b)
                                            if fa * fb < 0:
                                                break
                                            else:
                                                print('Межі не підходять')
                                        except:
                                            print('Функція не існує в одній із точок або введено неправильні дані')
                except:
                    print('Функція не існує в одній із точок або введено неправильні дані')

    if f(a)==0:
        print(a, ' - відповідь')
    if f(b)== 0:
        print(b, ' - відповідь')
    if f(a)*f(b) <0:
        break
a11=a
b11=b
M1=[]
S1=0
M2=[]
S2=0
M3=[]
S3=0
M4=[]
S4=0

def avr(a1, b1):
    return (a1+b1)/2

while True:
    S1+=1
    c=avr(a,b)
    if f(c)*f(a)<0:
        b=c
    else:
        a = c
    M1.append(c)
    if c==0:
        print(M1)
        print(c,' - відповідь')
        print(S1, ' - Кількість кроків')
        break
    if abs(a-b)<e:
        print(M1)
        print(avr(a,b), ' - відповідь')
        print(S1, ' - Кількість кроків')
        break


def fd(x):
    return eval(str(diff))
x=sp.Symbol('x')
f1=sp.sympify(func)
diff=sp.diff(f1,x)

print()
print('Метод Ньютона')
while True:
    try:
        xk=float(input(f'Введіть точку для метода Ньютона у межах [{a11}, {b11}]:'))
        if a11 <= xk <= b11 and f(xk) and 1/fd(xk)!=0:
            break
        else:
            print('Точність має бути у межах')
    except ValueError:
        print('Ви не ввели число або ввели неправильний вид числа')
    except ZeroDivisionError:
        print('Виникає діллення на 0 на одному з етапів, змініть точку')
xkk=xk
const=fd(xk)
while True:
    S2+=1
    x0=xk-f(xk)/fd(xk)
    xk=x0
    M2.append(x0)
    if x0==0:
        print(M2)
        print(x0,' - відповідь')
        print(S2, ' - Кількість кроків')
        break
    if S2>1 and abs(M2[S2-1] - M2[S2-2]) < e:
        print(M2)
        print(x0, ' - відповідь')
        print(S2, ' - Кількість кроків')
        break
print()
print('Модифікований метод Ньютона ')

while True:
    S3+=1
    xj=xkk-f(xkk)/const
    xkk=xj
    M3.append(xj)
    if x0==0:
        print(str(diff), ' - похідна')
        print(M3)
        print(x0,' - відповідь')
        print(S3, ' - Кількість кроків')
        break
    if S3>1 and abs(M3[S3-1] - M3[S3-2]) < e:
        print(str(diff), '- похідна')
        print(M3)
        print(xj, ' - відповідь')
        print(S3, ' - Кількість кроків')
        break
print()
print('Метод січних')
while True:
    S4+=1
    xi=a11-(f(a11)*(b11-a11))/(f(b11)-f(a11))
    if f(c) * f(a11) < 0:
        b11 = xi
    else:
        a11 = xi
    M4.append(xi)
    if xi==0:
        print(M4)
        print(xi,' - відповідь')
        print(S4, ' - Кількість кроків')
        break
    if S4>1 and abs(M4[S4-1] - M4[S4-2]) < e:
        print(M4)
        print(xi, ' - відповідь')
        print(S4, ' - Кількість кроків')
        break
print()
S=[S1, S2, S3, S4]
m=min(S)
if min(S)==S1:
    print(f'Метод половинного поділу виявився найшвидшим, {S1} кількість кроків')
if min(S)==S2:
    print(f'Метод Ньютона виявився найшвидшим, {S2} кількість кроків')
if min(S)==S3:
    print(f'Модифікований Метод Ньойтона виявився найшвидшим, {S3} кількість кроків')
if min(S)==S4:
    print(f'Метод січних виявився найшвидшим, {S4} кількість кроків')
