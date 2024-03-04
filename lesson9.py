# friends = {}
#
# friends["Nick"] = "+462121412"
#
# friends.update({"Paul":"+7421412412"})
#
# print(friends)
# school = {'9a': 23, '9б': 22, '9в': 21, '9м': 20, '9ф': 19}
# school['9a'] = 28  # измененное количество учеников в 9а классе
#
# print(school['9a'])
#
# print(school['9б'])
# lst_best_student = ["9a","9ф"]
#
# for student in school: # O(n)
#     if student in lst_best_student: # O(n)
#         print(school['9б']) # O(1)
import json

# O(N) * O(N)  => O(N*N)
# O(N+1) => O(N) + O(1) => O(n) т.к O(1) не оказывает влияния на O(n)
# del school['9б'] # класс 9б удален
# print(school)
# print(f'Всего учеников в школе 9-х классов:{sum(school.values())}') #выводим общее число учеников в школе

# import os
#
#
# print(os.getcwd())
# if not os.path.exists("test_dir"):
#     print(os.mkdir("test_dir"))

# # print(os.mkdir("test_dir_2"))
# print(os.makedirs("test_1/test_2"))
# os.remove("test_dir/test.txt")
# os.rmdir("test_dir")


# try:
#     file = open('test_file.txt', "a")
#     for i in range(1,10):
#         file.write(str(20))
# except Exception:
#     print("some error")
# finally:
#     file.close()
# file_path = 'C:/Users/Denis/PycharmProjects/py51onl/test_file.txt'
# with open(file_path,encoding="UTF-8") as file:
#     # file_data = file.read().rstrip().split("\n")
#     # file_data = file.readlines()
#     students = {}
#     for line in file:
#         student, mark = line.rstrip().split()
#         students[student] = int(mark)
#     print(students)

# some_list = ["Mark","Peter","Kate"]
# some_serialization_string = json.dumps(some_list)
# print(some_serialization_string)
# some_loads_list = json.loads(some_serialization_string)
# print(type(some_loads_list))
# students = {
#     "Mark": 4,
#     "Nick": 9,
#     "Ann": 7,
#     "Peter": 4,
#     "Kate": 6,
# }
#
# students = {
#     "Mark": 4,
#     "Nick": 9,
#     "Ann": 7,
#     "Peter": 4,
#     "Kate": 6
# }
#
# with open("students.json", "w") as file:
#     json.dump(students, file)
    # students = json.load(file)
