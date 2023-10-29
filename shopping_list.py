shopping_list = ["oil", "tomato paste", "pea", "sauce", "pepper", "split pea", "flour", "macaroni", "soya", "cheese", "halva sugary", "softener", "soap"]
s = shopping_list
a = input("What do you need? ")
if a in ["oil", "tomato paste"]:
    b = print(f"Your required thing index is : {s.index(a)}")
    e = print(f"and your required thing count is : {s.count(a)}")
elif a not in ["oil", "tomato paste"]:
    f = print("This item not in your list! ")
c = input("Do you like to add any thing in list? ")
if c == "yes":
    d = input("What would you like to addition? ")
    s.append(d)
    print ("Your addition successful.")
    s.sort()
    print(s)
    print("*Nice for answered to you see you later*")
elif c != "yes":
    print("*Nice for answered to you, see you later*")
