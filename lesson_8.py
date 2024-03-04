# def minimum(num_1: int, num_2: int, num_3: int) -> int:
#     min_numb = num_1
#     if min_numb > num_2:
#         min_numb = num_2
#     if min_numb > num_3:
#         min_numb = num_3
#     return min_numb
#
#
# print(minimum(minimum(9, 10, 9),minimum(8, 11, 7),minimum(19, 100, 4)))

# def modify_list(some_lst: list) -> None:
#     # new_list = [elem // 2 for elem in some_lst if elem % 2 == 0]
#     # print(new_list)
#     ind = 0
#     while ind < len(some_lst):
#         if some_lst[ind] % 2 == 0:
#             some_lst[ind] //= 2
#             ind += 1
#         else:
#             some_lst.pop(ind)
#
#     print(some_lst)
#
# modify_list([6, 3, 7, 12, 22])

# Создать список используя comprehension. Продублировать все неповторяющиеся элементы.
# lst = [5, 2, 7, 1, 1, 5, 2, 9, 11]
# ind = 0
# while ind < len(lst):
#     if lst.count(lst[ind]) == 1:
#         lst.insert(ind + 1, lst[ind])
#         ind += 1
#     ind += 1
#
# print(lst)
# some_set = set("hello")
# elem = some_set.pop()
# print(elem)
# print(some_set)
# some_set = {1, 2, 6, 3, 10}
# some_set_2 = {1, 5, 7, 3, 19}
# print(some_set.union(some_set_2))
# print(some_set | some_set_2)
# print(some_set.intersection(some_set_2))
# print(some_set & some_set_2)
# print(some_set.difference(some_set_2))
# print(some_set - some_set_2)
# some_set = {5, 2, 6, "hello"}
# some_dct = {"London": "England", "Minsk": "Belarus"}
# print("hello" in some_set)
# some_lst = [5, 2, 6, "hello"]
# print("hello" in some_lst)
# # some_set.add([5.2, 6.3, 7.2])
# some_set.update((5, 3, 2, 1))
# some_set.add((5, 2, 1))
# print(some_set)
# print(hash((5, 2, 1)))
# print(hash((1, 2, 5)))
# print(hash("hello"))
# print(hash(-42151))

# students = {
#     "Nick": {
#         "average mark": 5.35,
#         "age": 23,
#         "group": "3B"
#     },
#     "Ann": {
#         "average mark": 7.25,
#         "age": 22,
#         "group": "3B"
#     },
#     "Peter": {
#         "average mark": 9.21,
#         "age": 25,
#         "group": "5A"
#     }
# }
# for name in students:
#     print(name,":")
#     for info in students[name]:
#         print(info,students[name][info])
# for name in students:
# def registration(name: str, age: int) -> None:
#     if not name.isalpha():
#         raise NameError("name must be alpha")
#     if age < 1 or age > 150:
#         raise ValueError("age must be more then 0 and less than 150")
#     print("register success")
#
#
# while True:
#     try:
#         name = input("name:")
#         age = int(input("age"))
#         registration(
#             name=name,
#             age=age
#         )
#     except Exception as e:
#         print(f"faild: {e}")
#     else:
#         break
#     finally:
#         print("always work")
# lst = [1, 2, 5, 2, 3, 1, 1, 6, 5]
# 1  => NO
# 2  => NO
# 5  => NO
# 2  => YES
# 3 => NO
# 1  => YES
# 1  => YES
# 6  => NO
# 5  => YES
# import json
#
# json.dumps("hello")


