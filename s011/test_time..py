# import string
# a = string.ascii_letters+string.digits

# b = input("Enter your password: ")
# p = b
# for i in a:
#     for j in a:
#         for k in a:
#             for l in a:
#                 for m in a:
#                     guess = i+j+k+l+m
#                     if p == guess:
#                         print(f"password is {guess}. ")
#                         exit()
# print("End")

from time import sleep
# wrong = 0
# p = input('Enter password: ')
# a = "arad"
# while p != a:
#     wrong = wrong + 1
#     print(f"You entered wrong password for {wrong} times! ")
#     if wrong>3:
#         for i in range (wrong, 0, -1):
#             print(f"You must wait for {i} second to enter next password.")
#             sleep(1)
#         input("Enter password: ")
#         print("Welcom.")

p = input('Enter password: ')
a = "arad"
w = 0 
if p != a:
    w = w + 1
    print(f"You entered wrong password for {w} times! ")
    

