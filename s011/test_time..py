# import string
# from turtle import *
# a = string.ascii_letters+string.digits
# b = textinput("First name", "Enter yor name: ")
# c = textinput("Lastname", "Enter your last name: ") 
# d = numinput("Age", "Enter your age: ")
# e = textinput("Password", "Enter your password: ")
# p = e
# for i in a:
#     for j in a:
#         for k in a:
#             # for l in a:
#             #     for m in a:
#                     guess = i+j+k
#                     #+l+m
#                     if p == guess:
#                         up()
#                         goto(250, 200)
#                         write(f"password is {guess}. ", '', font= 'bold')
#                         exit()
# write("End")
# done()

from time import sleep
wrong = 0
p = input('Enter password: ')
a = "arad"
while p != a:
    wrong = wrong + 1
    print(f"You entered wrong password for {wrong} times! ")
    if wrong>3:
        for i in range (wrong, 0, -1):
            print(f"You must wait for {i} second to enter next password.")
            sleep(1)
        input("Enter password: ")
        print("Welcom.")

p = input('Enter password: ')
a = "arad"
w = 0 
if p != a:
    w = w + 1
    print(f"You entered wrong password for {w} times! ")
    

