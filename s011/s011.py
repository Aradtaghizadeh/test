try:
    f = open ('contacts.txt', 'r')
    mylist = f.read()
    contacts = {}
    mylist = mylist.strip()
    mylist = mylist.replace('}', '')
    mylist = mylist.replace('{', '')
    mylist = mylist.replace("'", '')
    mylist = mylist.split(",")
    for item in mylist:
        temp = item.strip().split(":")
        contacts[temp[0]]=temp[1]
        print(temp)
except FileNotFoundError:
    contacts = {}
name = input("Enter name:")
while name!='end':
    if name in contacts:
        print(f"{name} : {contacts.get(name)}")
        print(contacts)
    else:
        print("Not in contacts.")
        a = input("Want to add?").lower()
        if a == 'yes':
            number = input("Enter number: ")
            # contacts[name] = number
            contacts.update({name:number})
    name = input("Enter name:")
f = open('contacts.txt', 'w')
f.write(str(contacts))
print(contacts)