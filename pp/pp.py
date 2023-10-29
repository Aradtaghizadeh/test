from asc import *
from time import sleep
# import pygame

def myinput(items):
    answer = input(f"{items}: ").lower()
    while answer not in items:
        answer = input(f"{items}: ").lower()
    return answer

def play(a):
    # if a=='house':
    #     player.music.play()
    if a =='exit':
        exit()
    elif a in fridge_items and a!='kitchen':
        print(pictures.get(a))
        fridge_items.remove(a)
        sleep(1)
        print(pictures['fridge'])
        a = myinput(actions.get('fridge'))
        play(a)
    elif a in macrofer_items and a!='kitchen':
        t = int(input("Enter time in seconds: "))
        print(pictures['macrofer'])
        for i in range(t, 0, -1):
            sleep(1)
            print(i)
        print(pictures.get(a))
        macrofer_items.remove(a)
        sleep(2)
        print(pictures['kitchen'])
        a = myinput(actions.get('kitchen'))
        play(a)
    elif a == 'sleep':
        for i in range(1, 10):
            sleep(1)
            print(f'sleeping for {i} seconds.')
        print(pictures['room'])
        a = myinput(actions.get('room'))
        play(a)
    print(pictures.get(a))
    a = myinput(actions.get(a))
    play(a)

pictures = {
    'out': out,
    'house': salon,
    'tv': television,
    'tv1': tv1,
    'tv2': tv2,
    'tv3': tv3,
    'tv4': tv4,
    'tv_off': tv_off,
    'egg': egg,
    'cheese': cheese,
    'chocolate': chocolate,
    'icecream': icecream,
    'drink': drink,
    'apple': apple,
    'cake': cake,
    'pizza': pizza,
    'hotdog': hotdog,
    'hamburger': hamburger,
    'kitchen': kitchen,
    'lamp': l_on,
    'on': l_on,
    'off': l_off,
    'room': room,
    'salon': salon,
    'fridge': refrigerator,
    'macrofer': macrofer,
}
fridge_items = ['kitchen', 'apple', 'egg', 'cheese', 'chocolate', 'icecream', 'drink', 'cake', 'exit']
macrofer_items = ['kitchen', 'pizza', 'hotdog', 'hamburger', 'exit']
actions = {
    'out': ['house', 'exit'],
    'room': ['salon', 'sleep', 'lamp', 'exit'],
    'tv': ['salon', 'tv1', 'tv2', 'tv3', 'tv4', 'exit'],
    'tv1': ['salon', 'tv2', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv2': ['salon', 'tv1', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv3': ['salon', 'tv1', 'tv2', 'tv4', 'tv_off', 'exit'],
    'tv4': ['salon', 'tv1', 'tv2', 'tv3', 'tv_off', 'exit'],
    'tv_off': ['salon', 'tv1', 'tv2', 'tv3', 'tv4', 'exit'],
    'house': ['room', 'kitchen', 'tv', 'exit'],
    'kitchen': ['salon', 'fridge', 'macrofer', 'exit'],
    'lamp': ['room', 'off', 'exit'],
    'on': ['room', 'off', 'exit'],
    'off': ['room', 'on', 'exit'],
    'fridge': fridge_items,
    'macrofer': macrofer_items,
    'salon': ['room', 'kitchen', 'tv', 'exit'],
}

# player = pygame.mixer
# player.init()
# player.music.load('music1.mp3')
# player.music.set_volume(0.1)
play('out')
