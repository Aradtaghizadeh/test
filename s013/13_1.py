from random import choice
ch = ['r','p','s', 'end']
while True:
    computer = choice(ch)
    c = ""
    while c not in ch:
        c = input(f"Enter your choice {ch}:")
    if c == 'end':
        break
    elif c==computer:
        print('Draw')
    elif (c, computer)==('r', 's') or (c, computer)==('s', 'p') or (c, computer)==('p', 'r') :
        print('Win')
    else:
        print("Lose")
