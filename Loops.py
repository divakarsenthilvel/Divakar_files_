# for i in range(10,-1,-1):
#     print(f"Now i is {i}")

# classic = ["puffs", "Coffee", "Priya", "Tea", "Juice"]
#
# for pos in range(len(classic)):
#     if classic[pos].casefold() != 'priya':
#         continue
#     print(f"The position of priya is {pos}")

# a = 2
# b = 6
# sum = 0
#
# for x in range(16):
#     if x<10:
#         continue
#     sum = sum + a + b*x
# print(f"The sum is {sum}")

# for i in range(1,11):
#     for j in range(1,13):
#         print(f"{i} X {j} = {i*j}")
#     print('***************************')
#
# classic = ["puffs", "Coffee", "priya", "Tea", "Juice"]
# item = None
# i = 0
# while item==None:
#     if classic[i] == 'priya':
#         print(i)
#         break
#     i = i+1


# error = 100
# xold = 0
# xnew = 1
# while abs(error) > 0:
#     xold = xnew
#     xnew = 2.0*(xnew**(1/2))
#     error = xnew - xold
#     print(f"update x is {xnew}")
# print()
# print(f"The result is {xnew}")


k=int(input("enter the value"))
error = 100
xold = 0
xnew = 1
while abs(error) > 0.005:
    xold = xnew
    xnew = (xold**2+k)/(2*xold)
    error = xnew - xold
    print(f"update x is {xnew}")
print()
print("The result is {:.2f}" .format(xnew))





# number = int(input("enter the values"))
# root= number**(1/2)
# print(f"the root is {root}")

# for i in range (1,10):
#     x=i**.5
#     print(f'the root is {x}')
# x=i+1











# for item in classic:
#     if item.casefold() != "priya":
#         print(item)











# letters = input("Enter any thing including some numbers")
# letters = "9,afj6yt124klt:'"
#
# for i in range(len(letters)):
#     if not letters[i].isnumeric():
#         print(f"The position of non numeric charector is {i}")
















# notNumber=  ""
# Number = ""
# Alphabet = ""
# i = 0
# for char in letters:
#     if char.isalpha():
#         Alphabet = Alphabet + char
#         print(f" The index of {char} is {i}")
#     elif char.isnumeric():
#         Number = Number + char
#     else:
#         notNumber = notNumber + char
#     i = i+1
# print(f"""The alphabet other than digits are {Alphabet}
# and digits are {Number}
# and other charectors are {notNumber}""")