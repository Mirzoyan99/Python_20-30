# Create new list which have 6 different data types.

# For example: str,int

 

# myList = ['Hello', 4, 3.65, False, ['Armenia', 'USA'], {'name': 'Mher', 'Surname': 'Mirzoyan'}]

# print(myList)

 

# Create new list which have data notebooks and you want check if

# the data have Mac?

# For example: my_list =[“Hp”, “Asus”, “Dell”, “Mac”, ”Lenovo”]

# output: True

 

# myList = ['Hp', 'Asus', 'Dell', 'Mac', 'Lenovo']

# if "Mac" in myList:

#     print(True)

# else:

#     print(False)

# password = input("Введите пароль: ")

# if len(password) > 8 and sum(c.isdigit() for c in password) >= 2 and sum(c in '!@#$%&*' for c in password) >= 2:
#     print("Пароль сильный!")
# else:
#     print("Пароль слабый.")

# number = int(input("Enter number: "))

# for i in range(1, number + 1):
#     if number % i == 0:
#         print(i, end=" ")

# import random

# master = ['♥', '♦', '♣', '♠']
# karter = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# kalod = [i + j for i in master for j in karter]
# nor_kalod = []

# while kalod != []:
#     random_kart = random.choice(kalod)
#     nor_kalod.append(random_kart)
#     kalod.remove(random_kart)
# print(nor_kalod)

mylist = [1, 2, 3, 4]
for i in mylist:
    print()