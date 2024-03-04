# ip_address = "421.421.0.1"

# 1 solve
# ip_first = ip_address[:3]
# ip_second = ip_address[4:7]
# ip_third = ip_address[8]
# ip_forth = ip_address[10]
# print(ip_first,ip_second,ip_third,ip_forth)
# print(int(ip_first)+int(ip_second)+int(ip_third)+int(ip_forth))
# 2 solve
# lst_ip_address = ip_address.split(".")
#
# print(*lst_ip_address)
# print(sum(list(map(int,lst_ip_address))))

# 9.	Дано натуральное число. Определить произведение цифр в нем которые кратны 2, кроме числа 0.

# number = 4127057125
# multiply = 1
# while number:
#     if number % 10 % 2 == 0 and number % 10 != 0:
#         multiply *= number % 10
#     number //= 10
# print(multiply)

#
# n = 9
#
# numeric = 1
# digit = numeric ** 2
# while n >= digit:
#     numeric += 1
#     digit = numeric ** 2
#
# print(digit)
# Удалить в строке все буквы 'b', непосредственно за которыми идет цифра.
# Удалить из текста символы, являющиеся строчными латинскими буквами.

# some_string = "dhasdbdas b4bd 21 bb1dsadb7"
# some_new_string = ""
#
# for ind in range(len(some_string)):
#     if not (some_string[ind] == "b" and some_string[ind + 1].isdigit()):
#         some_new_string += some_string[ind]
#
# print(some_new_string)

# 20.	Числа Фибоначчи – известная числовая последовательность, в которой первые два члена равны единице,
# а каждый последующий получается сложением двух предыдущих.
# По введенному числу n выведите n чисел Фибоначчи через пробел.
# 1 1 2 3 5 8 13 21


# first_number = second_number
# second_number = second_number + first_number
# numb_1 = 3
# numb_2 = 4
# print(numb_1,numb_2)
# # temp = numb_2
# # numb_2 = numb_1 # numb_2 = 3
# # numb_1 = temp
# numb_1, numb_2 = numb_2, numb_1
# print(numb_1,numb_2)

# first_number = 1
# second_number = 1
# number = int(input("enter number:"))
# for numb in range(number):
#     print(first_number,end=" ")
#     first_number, second_number = second_number, first_number + second_number
# some_string = "SsssDdaaaadasd".lower() + " "
#
# some_decode_string = ""
# counter = 1
# for ind in range(len(some_string) - 1):
#     if some_string[ind] == some_string[ind + 1]:
#         counter += 1
#     else:
#         some_decode_string += some_string[ind] + str(counter)
#         counter = 1
#
#
# print(some_decode_string)

# print(5,6,7,2)


# def some_example_function(some_val_1, *args, some_val_2="world", **kwargs):
#     print(f"type: {type(some_val_1)} some_val_1: {some_val_1}")
#     print(f"type: {type(some_val_2)} some_val_2: {some_val_2}")
#     print(f"type: {type(args)} args: {args}")
#     print(f"type: {type(kwargs)} kwargs: {kwargs}")
#
# dct = {'key1': 1, 'key2': 2}
# tpl = ("John","Watson",35)
# name,surname,age = ("John","Watson",35)
# print(name,surname,age)
# some_example_function(
#     (4,5,2,1),
#     *tpl,
#     some_val_2="hello",
#     **dct
# )

# name = "John" # initialization
#
# def some_fun():
#     surname = "Watson"
#     print(locals())
#     # print(name,surname)
#
# some_fun()
# some_fun()
# print(name)
# def some_wrapper():
#     name = "John"
#     age = 25
#     print(f"locals wrapper:{locals()}")
#     def inner():
#         surname = "Watson"
#         print(f"locals inner:{locals()}")
#         print(name,age)
#     inner()
#
# some_wrapper()


# def get_info_user(
#         username: str = "Peter",
#         age: int = 25,
# ) -> str:
#     """
#     get info about current user
#     :param username: str, default = 'Peter':
#     :param age: int, default = 25:
#     :return str:
#     """
#     return f"username: {username.capitalize()} age: {age} "
#
# some_user = get_info_user(
#     # username="john",
#     # age=35
# )
# print(get_info_user.__doc__)

# [что положить for из чего берём in итерабельный объект]
# lst = [6, 3, 7, 1]
# print([i ** 3 for i in lst])
# # [что положить for из чего берём in итерабельный объект if expression]
# lst = [6, 3, 7, 1, 8]
# print([i for i in lst if i % 2 == 0])
# some_str = "1ygvd128gasl&)&@0238nas"
# print("".join([symb for symb in some_str if "a" <= symb <= "z"]))
# # [что положить if expression else что положить for из чего берём in итерабельный объект ]
# lst = [6, 3, 7, 1, 8]
# print([i if i % 2 == 0 else i ** 3 for i in lst])
# # matrix
# print([[0] * 4 for i in range(4)])
#
# print([int(i) for i in input().split()])
# print([int(input(f"enter number:")) for i in range(3)])
# import random
# print({random.randint(1,10) for _ in range(8)})
# lambda function

# lambda_function = lambda x, y, z: x + y + z
# print(lambda_function(5, 7, 2))
# lst = [24, 11, 26, 87, 21, 2, 77]

# lst.sort(key=lambda elem: elem % 2 == 0)

# print(lst)

# lst = [5, 2, 7, 2, 12, 7, 81]
# print(list(map(lambda elem: elem / 5, lst)))
# print([elem / 5 for elem in lst])

# lst = [4, 6, 0, "da", [], ""]
# print(list(filter(None,lst)))

#
# lst = [5, 2, "dsa", (), True, 4.26, "dsa", "123","", [2, 5, 2]]
# print(list(filter(lambda elem: type(elem) == str and elem, lst)))

#
# def some_owner_func(x: int):
#     def inner(arg: int):
#         nonlocal x
#         x += arg
#         print(x)
#     return inner
#
# fun = some_owner_func(10)
# fun(1)
# fun(1)
# fun(1)


# def decorator(fun: callable) -> callable:
#     def inner():
#         print("before decorated")
#         fun()
#         print("after decorated")
#     return inner
#
#
# def some_simple_functon():
#     print("hello world")
#
# decorated_function = decorator(some_simple_functon)
# # decorated_function()
# some_simple_functon()

# import random
#
#
# def decorator(fun: callable) -> callable:
#     def inner(numbers: int, *args, **kwargs) -> bool:
#         lst = fun(numbers)
#         return len(list(filter(lambda elem: elem >= 50, lst))) > 5
#     return inner
#
# @decorator
# def create_some_random_list(numbers: int) -> list:
#     return [random.randint(1, 100) for _ in range(numbers)]


# create_some_random_list = decorator(create_some_random_list)
print(create_some_random_list(10))

# some_bool_value = decorated_function()
# print(some_bool_value)
# print(create_some_random_list())