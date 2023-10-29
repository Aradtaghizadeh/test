phone_numbers = {
    'Sanam'         :       9911570826,
    'Mommy'         :       9111365403,
    'Dady'          :       9118386545,
    'Dady2'         :       9336655597,
    'Sara aunt'     :       9113342082,
    'Samid bro'     :       9115054547,
    'Sahand'        :       9935045494, 
    'Saeed uncle'   :       9111360229,
    'Grandma'       :       9112372987,
    'Sepideh aunt'  :       9111350158,
    'Mahyar'        :       9925109635,
    'Ali'           :       9382751279
}
a = input("Enter contact name: ")
b = print(f"Your contact number is {phone_numbers.get(a, 'not in your contacts. ')}")
if a not in ['Sanam', 'Momy', 'Dady', 'Dady2', 'Sara aunt', 'Samid bro', 'Sahand', 'Saeed uncle',  'Grandma', 'Sepideh aunt', 'Mahyar', 'Ali']:
    c = input("Do you like to creat or update contact? ")
    if c in ["yes", "ok"]:
        d = input("Enter new number: ") 
        phone_numbers.update({a : d})
        print(a)
        e = print("Your operation was successful. ")
        for i in phone_numbers:
            print(i)
print("Thanks for using of this app. ")
        

















# b = int[input("Enter contact number: ")]
# if a in phone_numbers:
#     print(f"contact number is {phone_numbers(a)}")
# elif b in phone_numbers:
#     print(f"contact name is {phone_numbers(b)}")