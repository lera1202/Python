import math


print('Вычислить корни квадратного уравнения ax² + bx + c = 0, где:')


a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
D = b ** 2 - 4 * a * c


if D > 0:
    x1 = ((- b + math.sqrt(D)) / (2 * a))
    x2 = (- b - math.sqrt(D)) / (2 * a)
    print('x1 равен ' + str(x1) + ', x2 равен ' + str(x2))
elif D == 0:
    x = (-b) / (2 * a)
    print('x равен ' + str(x))
else:
    print('Уравнение не имеет корней')



