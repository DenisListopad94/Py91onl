#              0
# some_string = "hello world"
#
# for elem in some_string:
#     print(elem)
#
# length = len(some_string)
#
# for ind in range(length):
#     print(some_string[ind])

# range()
# range(start,stop) range(1,4) 1 2 3 step = 1
# range(start,stop,step) range(1,9,2) 1 3 5 7
# range(stop) range(5) 0 1 2 3 4 start = 0 step = 1

# summa = 0
# mul = 1
# for numb in range(1,11):
#     summa += numb
#     mul *= numb
# print(summa)
# print(mul)

# оператор принадлежности in(включает) not in(не включает)
# print("le" not in "hello")

# some_string = "hello world"
# glasn = "aeuioyAYIUOE"
# new_str = ""
# for elem in some_string:
#     if elem not in glasn:
#         new_str += elem
#
# print(f"new_str: {new_str}")


# some_string = "djkq  dqwd      dqwd qww     qwq      qwd" + " "
# some_tmp_str = ""
#
# for elem in some_string:
#     if elem != " ":
#         some_tmp_str += elem
#     elif some_tmp_str:
#         if "d" in some_tmp_str:
#             print(some_tmp_str)
#         some_tmp_str = ""

# add ! after r ( after p
# сложность по времени
# сложность O большое или сложность алгоритмическая


# some_string = "qpwd rasd qwdpr rr dqwd dasppdsa"
# new_string = ""
# for elem in some_string:
#     if elem == "r":
#         new_string += "r!"
#     elif elem == "p":
#         new_string += "p("
#     else:
#         new_string += elem
# print(new_string)
# new_second_string = some_string.replace("r","r!").replace("p","p(")
# print(new_second_string)
#
# some_string = " dasda(sada) dsad((dasd(dsad) dasd() sdas) sda)"
# some_tmp_str = ""
#
# for ind in range(len(some_string)):
#     if some_string[ind] == "(":
#         for elem in some_string[ind+1:]:
#             if elem == "(":
#                 some_tmp_str = ""
#                 break
#             if elem == ")":
#                 if some_tmp_str:
#                     print(some_tmp_str)
#                 some_tmp_str = ""
#                 break
#             if elem != ")":
#                 some_tmp_str += elem
# for number in range(6):
#     print(number)

# number = 0
# while number < 6:
#     print(number)
#     number += 1
# summa = 0
# while True: # forever loop
#     number = int(input("enter number:"))
#     if number == 11:
#         break
#     if number % 2 == 0:
#         continue
#     summa += number
#
# print(summa)

# number = int(input("enter number: "))
# max_number = number % 10
# # 42151 4 + 2 + 1 + 5 + 1  = 13
# while number:
#     numeric = number % 10
#     number //= 10
#     if numeric == 9:
#         max_number = numeric
#         break
#     if numeric > max_number:
#         max_number = numeric
# else:
#     print("max number in not 9")
#
# print(f"max number: {max_number}")
# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(i * j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1

# some_lst = [True, True, "hello", 5, 2.3, None]
# print(some_lst[0])
# some_lst[2] = "world"
# print(some_lst[:3])
# elem = some_lst.pop()
# print(elem)
# some_lst.remove(True)
# print(some_lst)

tup = 4,
lst = [4,8, "hello"]
print(tup.__sizeof__())
print(lst.__sizeof__())
