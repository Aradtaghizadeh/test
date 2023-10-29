from json import dump, load 

try:
    f = open ('contacts.json', 'r')
    contacts = load(f)
    f.close()
    # mylist = f.read()
    # contacts = {}
    # mylist = mylist.strip()
    # mylist = mylist.replace('}', '')
    # mylist = mylist.replace('{', '')
    # mylist = mylist.replace("'", '')
    # mylist = mylist.split(",")
    # for item in mylist:
    #     temp = item.strip().split(":")
    #     contacts[temp[0]]=temp[1]
    #     print(temp)
except FileNotFoundError:
    contacts = {}
for item in contacts.values():
    print(item)
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
f = open('contacts.json', 'w')
dump(contacts, f, indent = 4)
f.close()
print(contacts)