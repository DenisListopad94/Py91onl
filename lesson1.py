# Изучаем python базовые понятия /однострочный комментарий

"""
это
многострочный
комментарий
переменные
mutable unmutable
int целые числа 4 -6 0 16
float вещественные числа 5.62 0.61 -0.23
str строки 'hello' 'мир' '24' строковые объекты
bool булевый тип True/False
None NoneType ничего/пустота

переменные
не начинаем с цифры
не используем служебные символы
не используем кириллицу
не используем зарезирвированные слова  if else raise
"""

# some_number_1 = 67  # snake case
# SomeNumber = 56  # camel case
# NUMBER_PI = 3.14
# _number_sec = 65
# print(some_number_1, someNumber)

# """
# арифметические операции
# ** возведение в степень 2 ** 3 = 8
# () скобки
# + (сложение)
# - (вычитание)
# * (умножение)
# / (деление обычное) 8 / 3 = 2.6666666667
# // (целочисленное деление) 8 // 3 = 2
# % (остаток от деления) 8 % 3 = 2
#
# """
# # import sys
# # sys.set_int_max_str_digits(700000)
#
# # number_1 = 13
# # number_2 = 10400
# # print(number_1**number_2)
#
# # есть трёхзначное число - найти сумму его цифр = > 567 5 + 6 + 7 = 18
# # import math
# #
# #
# # number = 567
# # ed = number % 10
# # des = number % 100 // 10
# # sot = number // 100
# # print("ed:", ed)
# # print("des:", des)
# # print("sot:", sot)
# # summa_num = ed + des + sot
# # new_numb = ed * 100 + des * 10 + sot
# # print("summa:",summa_num)
# # print("new_numb:",new_numb)
#
# some_var_1 = 6
# print(type(some_var_1))
# some_var_1 = str(some_var_1)
# print(type(some_var_1))


# print(5, ",", 6, )

# Name = "Jack"
# name = "John"
# NaMe = "Bob"
# print(Name, NaMe, name)
# numb_lst_1 = [5, 2]
# numb_lst_2 = numb_lst_1
#
# print(numb_lst_1 is numb_lst_2)

# numb = 5
# # numb += 5
# # numb -= 5
# # numb *= 5
# numb **= 5
# # numb = numb ** 5
# print(numb)

# first_name = "Alex"
# last_name = "Nickals"
# age = 25
# print("info -> first_name:", first_name, "last_name:", last_name, "age:", age)
# print("info -> first_name: {} last_name: {} age: {}".format(first_name,last_name,age))
# print(f"info -> first_name: {first_name} last_name: {last_name} age: {age+2}")
# print("info -> first_name: %s last_name: %s age: %d " % (first_name, last_name, age))
#
# print('The value of pi is: %0.3f' % (0.14))

# some_int = 0
# print(bool(some_int))

# some_str = ""
#
# none = None
# some_lst = []
# # print(id(some_lst))
# numb_1 = 8
# numb_2 = 9
# numb_3 = 7
# and(и) or(или) not(не)
# print(f"numb_2 < numb_3: {numb_2 < numb_3}")
# print(f"numb_3 != 0:{numb_3 != 0}")
# print(f"not numb_1 < numb_2:{not numb_1 < numb_2 }")

#
# if not numb_1 < numb_2 and (numb_2 < numb_3 or numb_3 != 0):
#     # тело условного оператора
#     print(f"{numb_2} more than {numb_1}")
#     numb_1 += 2
#     numb_2 += 6
#     print(f"numb_2: {numb_2}")
#     print(f"numb_1: {numb_1}")

# number = 18
# if number > 0:
#     print(f"{number} -> positive")
#     if number > 9:
#         print("two signs")
# elif number == 0:
#     print(f"{number} -> zero")
# else:
#     print(f"{number} -> negative")

# number = 12
# print(bool(number % 2))
#
# if number % 2:
#     print(f"{number} нечётное")
# else:
#     print(f"{number} чётное")
#
# lst = []
#
# if lst:
#     print(lst)

# тернарный оператор
# что сделать если условие истинно иначе сделай это

# number = 12
# print("нечётное" if number % 2 else "чётное")

# numb_1 = 1
# numb_2 = 3
# numb_3 = 3
# numb_4 = 3
# numb_5 = 1

# counter = 0
# if numb_1 % 2 == 0:
#     counter += 1
# if numb_2 % 2 == 0:
#     counter += 1
# if numb_3 % 2 == 0:
#     counter += 1
# if numb_4 % 2 == 0:
#     counter += 1
# if numb_5 % 2 == 0:
#     counter += 1
# print(f"counter: {counter}")

# print(numb_1,numb_2,end="  /\  ")
# print(numb_2,numb_3,sep="-")

# number = int(input("enter number:"))
# number_2 = int(input("enter number_2:"))

# print(number)
# print(number_2)

# number, number_2, number_3, number_4 = map(int,input().split()) # unpack распаковка
# print(number,number_2,number_3,number_4)
#number = int(input("enter number:"))

print("hello world")

#print(number > 99)
