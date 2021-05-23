# even = [2, 4, 6, 8, 10]
# odd = [1, 3, 5, 7, 9]
# new_even = even.copy()
# print(id(even))
# even.extend(odd)
# print(id(new_even))
# new_even.sort(reverse=True)
# print(new_even)

# Sorted_list = sorted(even)
# print(Sorted_list)
# print(even)
#
# print(sorted("ghrtTbnsjyryjolKk, 1 5 "))

# NIT = [
#     'Mech',
#     'EEE',
#     'ECE',
#     'CHE',
#     'PROD',
#     'CSE',
# ]
#
# new_list = list(NIT)
# print(new_list)
# new_list = NIT.copy()
# print(new_list)

# number = [1, 2, 5, 100, 120,3, 114, 1050 , 325, 150, 180, 235, 360]
# # nu= [0, 1, 2, 3,   4,   5,   6,   7,   8]
# print(number)
# min_value =  99
# max_value = 200

# for index, num in enumerate(number):
#     if num <= min_value or num >= max_value:
#         del number[index]
# print(number)

# stop = 0
# for index, num in enumerate(number):
#     if num > min_value:
#         stop = index
#         break
# del number[:stop]
# print(number)
#
# start = 0
# max_index = len(number)
# for index, num in enumerate(reversed(number)):
#     print(f"index i s {index} and the value is {num}")
#     if num < max_value:
#         start = max_index - index
#         break
# del number[start:]
# print(number)


# stop = 0
# for index in range(len(number)):
#     if number[index] > min_value:
#         stop = index
#         break
# del number[:stop]
# print(number)
# start = 0
# for index in range(len(number)-1,-1,-1):
#     if number[index] < max_value:
#         start = index + 1
#         break
# del number[start:]
# print(number)

# for index in range(len(number)-1,-1,-1):
#     if number[index] <= min_value or number[index] >= max_value:
#         del number[index]
# print(number)

# name = 'divakar'
# print(name.count('a'))
# print(name.index('a'))

# number = [1,2,3,4,5,6]
# print(number)
# a = number
# a.clear()
# print(number)
# print(a is number)

# nested_list = [
#     [1,2,3],
#     [4,5,6],
# ]
#
# print(nested_list[1][1])

# NITT = [
#     ['KRB', 'SPS', 'spam'],
#     ['RAC', 'spam', 'SS' ],
#     ['VSC', 'MU', 'RBA'],
#     ['AMS', 'SM', 'NG'],
# ]
# for items in NITT:
#     for item in items:
#         if item != 'spam':
#             print(item)
#     print()

# name = 'Kottala Ravi kumar'
# list_name = name.split()
# print(list_name)

number = '1,2,3,4,5,6,7,8,9'
string_num = number.split(',')
print(string_num)

# number_string = input("Enter three numbers separated by comma lke a,b,c: ")
# list_num = number_string.split(',')
# number = []
# for item in list_num:
#     number.append(int(item))
# print(f"The sum is {number[0] + number[1] + number[2] }")

# flower = [
#     'jasmine',
#     'rose',
#     'lotus',
#     'lilly',
# ]
#
# joined = ' & '.join(flower)
# print(joined)









