

# def factori(number):
#     if number > 0:
#         return number * factori(number-1)
#     else:
#         return 1
#
# number = int(input('enter the number for factorial: '))
# print("the factorial is " , factori(number))



number = int(input('enter the positive number for factorial: '))

def factori(number):
    if number > 0:
        return number * factori(number-1)
    elif number < 0:
       print ('get lost you idiot..........  factorial can be calculated only for positive numbers')
    else:
        return 1


print("the value of {}! is {} " .format (number,factori(number)))


# number = int(input('enter the positive number for factorial: '))
#
# def factori (number):
#     if number == 0:
#         return 1
#     else:
#         return number * factori(number-1)
#
#
# print("the value of {}! is {} " .format (number,factori(number)))




