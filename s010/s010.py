contacts = {
    'baba': '09111251',
    'reza': '09123652',
}
name = input("Enter name:")
while name!='end':
    if name in contacts:
        print(f"{name}: ----{contacts.get(name)}")
    else:
        print("Not in contacts.")
        a = input("Want to add?").lower()
        if a == 'yes':
            number = input("Enter number: ")
            contacts[name]=number
            # contacts.update({name:number})
    name = input("Enter name:")
f = open('contacts.txt', 'w')
for i in contacts.items():
    f.write(str(i))
    f.write('\n')
print(contacts)