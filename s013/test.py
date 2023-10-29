mystring = ""
count = mystring.count('Iran')
i=-1
# for j in range(count):
#     i = mystring.index('Iran', i+1)
#     print(i)
while True:
    try:
        i = mystring.index('Iran', i+1)
        print(i)
    except ValueError:
        break
