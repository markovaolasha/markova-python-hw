#________________________________________________________________
# СЕМИНАР 2
#________________________________________________________________

'''Списки
a = [[1], 2, 3]

= deepcopy(a)

print('a =', a)
print('b =', b)

a[0].append(4)
b[0].append(5)

print('a =', a)
print('b =', b)

a.append(9)
b.append(8)

print('a =', a)
print('b =', b)'''
'''________________________________________________________________
1. Напишите программу, которая принимает на вход число N и выдаёт последовательность 
из N членов.
*Пример:*
- Для N = 5: 1, -3, 9, -27, 81'''
#вариант 1
'''n = int(input('Введите число '))

a = [1]
for i in range(1, n):
    a.append(a[-1]*-3)
print(a)'''
#вариант 2
'''n = int(input('Введите число '))
num = 1

for i in range(n):
    print (num)
    num  *= -3'''
#вариант 3
'''for i in range(int(input())):
    print((-3)**i)'''
'''________________________________________________________________
2. Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
*Пример:*
4 -> [1, 4, 7, 10]'''
#вариант 1
'''n = 4
a = []
for i in range(4):
    a.append(3*i+1)
print(a)'''
#вариант 2
'''n = 4
a = [3*i+1 for i in range(n)]
print(a)'''
#________________________________________________________________
# СЕМИНАР 3
#________________________________________________________________