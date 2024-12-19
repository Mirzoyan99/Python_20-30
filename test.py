# erk = Float(input('Mutqagreq er: '))
# layn = Float(input('Mutqagreq layn: '))
# input(erk * layn)



# mec_tara_gin = 0.10
# poqr_tara_gin = 0.25
# mec_tara_qanak  = int(input('mutqagreq poqr tarraneri qanak: '))
# poqr_tara_qanak  = int(input('mutqagreq mec tarraneri qanak: '))

# print('$',poqr_tara_gin * poqr_tara_qanak + mec_tara_gin * mec_tara_qanak)



# hashiv = float(input('mutqagreq hashivy:  '))
# hark = hashiv * 4 / 100
# matucox = hashiv * 18 / 100
# print(f'hark -> {hark}\nmatucoin -> {matucox}\nmnac -> {hashiv - matucox - hark}')

# num = int(input('Enter Number:  '))
# count_200 = num // 200
# num = num % 200
# count_100 = num // 100
# num = num % 100
# count_100 = num // 25
# num = num % 25
# count_100 = num // 10
# num = num % 10
# count_100 = num // 5
# num = num % 5
# count_100 = num // 1
# num = num % 1

# print()


# THERMOMETER


# celsius = int(input('mutqagreq jermastijany celsiusov: '))

# fahrenheit = (celsius * 1) + 33.8

# print((f'\ncelsius -> {celsius}\n\nfahrenheit = {fahrenheit}'))



# fahrenheit = float(input('mutqagreq jermastijany fahrenheitov: '))

# celsius = (fahrenheit / 33.8) * 1

# print((f'\nfahrenheit -> {fahrenheit}\n\ncelsius = {celsius}'))



# a = float(input('Enter a = '))
# b = float(input('Enter b = '))
# c = float(input('Enter c = '))

# print(f'P = {a + b + c}')


# min = float(input('mutqagreq ropen vajrkyan dardznelu hamar:  '))

# sec = (min * 60)

# print((f'\nmin -> { min } \nsec = { sec }'))

# import math


# x = int(input('enter number: '))

# print(3 - x)

# number = 1234

# print(number % 10, number // 10 % 10, number // 100 % 10, number // 1000)

# import random

# pc = random.randint(0,10)
# user = int(input( 'enter number (1 - 10) : ' ))


# print(f'user -> {user} \n pc -> {pc} \n *****{user == pc}*****')

# pc = random.randint(1,100)
# user = int(input( 'enter number (1 - 100) : ' ))


# print(f'user -> {user} \n pc -> {pc} \n *****{user >= pc}*****')

# import calendar

# year = int(input('Enter the your birthday year: '))
# mount = int(input('Enter the your birthday month: ')) 
# day = int(input('Enter the your birthday day: '))

# print(calendar.month(year, mount, day))

# harc1 = input('inch e pythony\n a)cragravorman lezu \n b)interpritatr \n c)cragir \n d)heraxosi model\n ')
# harc2 = input('erb e stexcvel pythony\n a)1980 \n b)1978 \n c)1967 \n d)1998\n ')
# harc3 = input('erb e stexcvel c# lezun\n a)1998-2001 \n b)2002 \n c)1997 \n d)2000-2001\n ')

# print(harc1 == 'b' and harc2 == 'a' and harc3 == 'a')
# --------------------------------------------------------------------------------------------------
# import random

# num = [1,2,3,5,7]

# print(random.randint(1,10) in num)
# -------------------------------------------------------------------------------------------------

# dog_age = int(input('Enter dog age: '))

# if dog_age <= 2:
#     print(f'Human age = {dog_age * 10.5}')
# else:
#     print(f'Human age {21+ (dog_age - 2) * 4}')

# text = (input('Enter text:  '))
# count = 0

# for i in text:
#     if i == 'a':
#         count += 1
# print(count)

# text = 'Hello World'
# count = 0

# for i in text:
#     if i == 'o':
#          count += 1
# print(i)

# text = input('Enter text: ')
# summ = 0 

# for i in text:
#     if i.isdigit():
#         summ += int(i)
# print(summ)

# for i in range(1, 11):
#     print(i)

# N = int(input("Введите число N: "))
# total = 0
# for i in range(1, N + 1):
#     total += i
# print("Сумма чисел от 1 до", N, "равна:", total)

# for i in range(10, 0, -1):
#     # Ваш код здесь
#     print(i)

# for i in range(1, 21):
#     if i % 2 == 0:
#         # Ваш код здесь
#         print(i)

# n = int(input("Enter number: "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= 1
# print(factorial)

# text = (input('Enter number:  '))
# text = 'Python 3.13'
# summ = 0

# for i in text:
#     if i.isdigit():
#         summ += int(i)
# print(summ)

# for i in range(1, 10):
#     if i == 7:
#         continue
#     else:
#         print(i)

# summ = 0
# count = 0

# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     else:
#         summ += int(number)
#         count += 1
# print(summ / count)

# summ = 0

# while True:
#     age = input('Enter age: ')
#     if age == '':
#         break
#     else:
#         age = int(age)
#         if 2 >= age >= 0:
#             continue
#         elif 12 >= age > 2:
#             summ += 14
#         else:
#             summ += 18
# print(summ)

# pi = 3
# a = 2
# b = 3
# c = 4

# for i in range(15):
#     pi += (4 / (a * b * c) * ((-1) ** i))
# a, b, c = a + 2, b + 2, c + 2
# print(pi)

# ---------------------------------------------------
# n1, n2 = 0, 1
# for i in range(40):
#     print(n1)
#     n1, n2 = n2, n1 + n2
# # ---------------------------------------------------
# for i in range(1, 11):
#     print(i)
# # ---------------------------------------------------

# i = 1
# while i < 11:
#     print(i)
#     i += 1
# # ---------------------------------------------------


# while True:
#     number = int(input('Enter number: '))
#     if number == 128:
#         break
#     else:
#         print(number)
# # ---------------------------------------------------



# summ = 0
# while True:
#     number = int(input('Enter number: '))
#     if number == 0:
#         break
#     else:
#         summ += number
# print(summ)
# # ---------------------------------------------------


# summ = 0
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     else:
#         summ += int(number)
# print(summ)
# # ---------------------------------------------------


# count_ = 0
# sum_ = 0
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     else:
#         sum_ += int(number)
#         count_ += 1
# print(sum_ / count_)
# # ---------------------------------------------------


# kassa = 0
# while True:
#     age = input('Enter age:  ')
#     if age == '':
#         break
#     else:
#         age = int(age)
#         if 2 >= age >= 0:
#             continue
#         elif 12 >= age > 2:
#             kassa += 14
#         elif 65 >= age > 12:
#             kassa += 23
#         else:
#             kassa += 18
# print(kassa)
# # ---------------------------------------------------

# text = input('Enter text:  ')
# for i in text:
#     print(chr(ord(i) + 3), end='')
# # ---------------------------------------------------

# pi = 3
# a = 2
# b = 3
# c = 4
# for i in range(15):
#     pi += (4 / (a * b * c)) * ((-1) ** i)
#     a, b, c = a + 2, b + 2, c + 2
# print(pi)
# ---------------------------------------------------
# import random

# count_o = 0
# count_p = 0
# s = ''
# while True:
#     if count_o == 3 or count_p == 3:
#         break
#     random_letter = random.choice("OP")
#     if random_letter == "O":
#         s += 'O'
#         count_o += 1
#         count_p = 0
#     else:
#         s += 'P'
#         count_p += 1
#         count_o = 0
# print(s)
# ---------------------------------------------------

# a, b = 12, 5
# if a + b:
#     print('True')
# else:
#   print('False')

# x = 0
# for i in range(10):
#   for j in range(-1, -10, -1):
#     x += 1
#     print(x)
# x = 0
# while (x < 100):
#   x+=2
# print(x)
# numbers = [10, 20]
# items = ["Chair", "Table"]

# for x in numbers:
#   for y in items:
#     print(x, y)

# num = int(input('Enter text: '))

# for i in range(1, num):
#     for _ in range(i):
#         print(i, end = '_')
#     print()

# n = int(input('Enter n: '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if i == j or n == i + j:
#             print('^', end = '')
#         else:
#             print(' ', end = '')
#     print()

# bin_code = input('Enter code: ')
# bin_code = bin_code[::-1]
# number = 0
# for i in range(0, len(bin_code)):
#     number += int(bin_code[i]) * 2 ** i
# print(number)

# ------------------------------------------------------------


# n = int(input('Enter n: '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if j == 0 or j == n:
#             print('|', end='')
#         elif i == 0 or i == n:
#             print('--', end='')
#         else:
#             print('  ', end='')
#     print()
# ------------------------------------------------------------


# n = int(input('Enter n: '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if i == j or n == i + j:
#             print('^', end='')
#         else:
#             print(' ', end='')
#     print()
# ------------------------------------------------------------


# n = int(input('Enter n: ')) # 24
# for i in range(2, n): # 2, 3, 4, 5, 6, 7, 8, ...., 22, 23
#     if n % i == 0:
#         print(False)
#         break
# else:
#     print(True)
# ------------------------------------------------------------
# number = int(input('Enter number: '))
# text = ''
# while number > 1:
#     text += str(number % 2)
#     number //= 2
# print("1" + text[::-1])
# ------------------------------------------------------------

# n = int(input('Enter number:  '))
# for i in range(1, n + 1):
#     for _ in range(i):
#         print(i, end='.')
#     print()

# n = int(input('Enter number:  '))
# for i in range(1):
#     for j in range(i):
#         number = j
#     print(f'{number}\t' * 6)

# text = input('Enter text:  ')
# for i in text:
#     if i.isdigit():
#         continue
#     elif i.isalpha():
#         continue
#     else:
#         text = text.replace(i, '')
# print(text == text[::-1])

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i * j: > 4}', end = '')
#     print()

# n = int(input('Введите количество уровней пирамиды: '))
# number = 1

# for row in range(1, n+1):
#   print('\t' * (n - row), end = '')
#   for col in range(row):
#     print(number, end = '')
#     number += 5
#     print('\t' * 2, end = '')
#   print()

# n = int(input('Enter Number: '))
# print()
# let = n - 1
# while let >= 0:
#     for i in range(-n, n + 1):
#         if abs(i) > let:
#             print(abs(i), end='')
#         elif i == 0:
#             print(end='')
#         else:
#             print('.', end='')
#     let -= 1
#     print()


# n = int(input("Enter number: "))
# summ = 1
# for i in range(1, n + 1):
#     factorial = 1
#     for j in range(1, i + 1):
#         factorial *= j
#     summ += factorial
# print(summ)

# n = int(input("Enter number: "))
# summ = 0
# for i in range(0, n + 1, 5):
#     price = int(input(f'{i} Partq: '))
#     summ += price
# print(summ)

# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# c = int(input("Enter number: "))

# for i in range(a, b):
#     if i % c == 0:
#         print(i)

