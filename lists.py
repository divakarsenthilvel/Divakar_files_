# non mutable items

# name = "Divakar"
# another_name = name
#
# print(id(name))
# print(id(another_name))
# name = name + " priya"
# print()
# print(id(name))
# print(id(another_name))
# number = 3.1415
# another_number = number
#
# print(id(number))
# print(id(another_number))
# number = number + 1.0
# print()
# print(id(number))
# print(id(another_number))
#
# print()
# print(number)
# print(another_number)
#
# classic = ["puffs", "tea", "coffee", "juice"]
# newClassic = classic
# a = b = c = d = classic
# print(id(classic))
# print(id(newClassic))
#
# classic = classic.append("new item")
#
# print()
# print(id(classic))
# print(id(newClassic))
#
# print(newClassic)
# print(a)
# print(b)
# print(c)


# plate =  []
#
# chosenItem = "-"
# while chosenItem != "0":
#     if chosenItem in "123456":
#         print(f"So you ordered item {chosenItem}")
#         if chosenItem == "1":
#             plate.append("idly")
#         elif chosenItem == "2":
#             plate.append("Dosa")
#         elif chosenItem == "3":
#             plate.append("Poori")
#         elif chosenItem == "4":
#             plate.append("Pongal")
#         elif chosenItem == "5":
#             plate.append("Vada")
#         elif chosenItem == "6":
#             plate.append("juice")
#     print(""" You can choose from the menu
#         1: Idly
#         2: Dosa
#         3: Poori
#         4: Pongal
#         5: vada
#         6: juice
#         Enter 0 if you finished""")
#     chosenItem = str(input( " enter the id of item: "))
#
# print(f"So you have orderd {plate}")

# menu = ["idly", "dosa", "Poori", "Pongal", "Vada", "juice"]
# idMenu = [str(i) for i in range(1,len(menu) + 1)]
# # for i in range(1,len(menu) + 1):
# #     idMenu.append(str(i))
# plate =  []
# print(idMenu)
# chosenItem = "-"
# while chosenItem != "0":
#     if chosenItem in idMenu:
#         print(f"So you ordered item {chosenItem}")
#         plate.append(menu[int(chosenItem)-1])
#     print("You can choose the items listed below using numbers")
#     for ind, item in enumerate(menu):
#         print(f"{ind+1} : {item}")
#     print("Enter 0 if finished")
#     chosenItem = str(input( " enter the id of item: "))
#
# print(f"So you have orderd {plate}")

number = [2,10,50,25,36,75,2]
print(min(number))
print(max(number))
print(number.count(2))
print(len(number))




