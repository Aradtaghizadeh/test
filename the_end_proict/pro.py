from ascii_pro import *
import pygame
from time import sleep


player = pygame.mixer
player.init()
player.music.set_volume(0.5)
def load(n):
    player.music.load(n)
    player.music.play()
def myinput(i):
    answer = input(f"{i}: ").lower()
    while answer not in i:
        answer = input(f"{i}").lower()
    return answer
def pause():
    player.music.pause()
def stop():
    player.music.stop()

def play(a):
    if a=='salon':
        load('hang_drum.mp3')
        player.music.set_volume(0.3)


    elif a =='exit':
        print('***Thank for playing this game***')
        exit()

    elif a in fridge_i and a!='kitchen':
        print(p.get(a))
        fridge_i.remove(a)
        load('food.mp3')
        sleep(10)
        load('hang_drum.mp3')
        player.music.set_volume(0.3)
        print(p['fridge'])
        a = myinput(act.get('fridge'))
        play(a)

    elif a in microwave_i and a!='kitchen':
        t = int(input("Enter time in seconds: "))
        print(p['microwave'])
        for i in range(t, 0, -1):
            sleep(1)
            print(i)
        print(p.get(a))
        microwave_i.remove(a)
        pause()
        load('food.mp3')
        sleep(10)
        load('hang_drum.mp3')
        player.music.set_volume(0.3)
        print(p['kitchen'])
        a = myinput(act.get('kitchen'))
        play(a)

    elif a == 'sleep':
        print(sleepi)
        load('sleep.mp3')
        for i in range(1, 11):
            sleep(1)
            print(f'sleeping for {i} seconds.')
        load('hang_drum.mp3')
        player.music.set_volume(0.3)
        print(p['room'])
        a = myinput(act.get('room'))
        play(a)

    elif a in transport_i:
        print(p.get(a))
        items = act.get(a)
        print(items)
        c = ''
        while c not in items:
            c = input('Where do you go? ')
        if a=='airplane':
            load('plane.mp3')
        elif a=='car':
            load('car.mp3')
        elif a == 'ship':
            load('ship.mp3')  
        elif a=='train':
            load('train.mp3')
        elif a=='horse':
            load('horse.mp3')
        for i in range(10, 0, -1):
            sleep(1)
            print(f"wait {i} seconds to arrive that place. ")
        stop()
        if c == 'mount':
            load('gorg.mp3')
        if c == 'garden':
            load('birds.mp3')
        if c == 'jungle':
            load('jungle.mp3')
        if c == 'beach':
            load('beach.mp3')
        if c == 'city':
            load('city.mp3')
        print(p.get(c))
        c = myinput(act.get(c))
        play(c)
    elif a == "tv3":
        pause()
        load('football.mp3')
    elif a == 'tv1':
        pause()
        load('news.mp3')
    elif a == 'tv2':
        pause()
        load('animals.mp3')
    elif a == 'tv4':
        pause()
        load('cook.mp3')
    elif a == 'tv_off':
        pause()
        load('hang_drum.mp3')
        player.music.set_volume(0.3)
    elif a == 'lamp' or a == 'on':
        load('lamp.mp3')
        sleep(1)
        load('hang_drum.mp3')
        player.music.set_volume(0.3)




    print(p.get(a))
    a = myinput(act.get(a))
    play(a)



    

out_i = ['beach', 'jungle', 'garden', 'city', 'mount', 'exit']
transport_i = ['car', 'airplane', 'ship', 'horse', 'train', 'exit']
fridge_i = ['kitchen', 'banana', 'choco', 'milk', 'pineapple', 'icecream', 'drink', 'cheese', 'apple', 'exit']
microwave_i = ['kitchen', 'cake', 'pizza', 'hotdog', 'burger', 'coffee', 'exit']
p = { 
      'home'    : house,
      'house'   : house,
      'kitchen' : kitchen,
      'salon'   : salon,
      'room'    : bedroom,
      'fridge'  : fridge,
      'microwave': microwave,
      'burger'  : burger,
      'banana'  : banana,
      'choco'   : chocolate,
      'milk'    : milk,
      'cake'    : cake,
      'pizza'   : pizza,
      'hotdog'  : hotdog,
      'cheese'  : cheese,
      'apple'   : apple,
      'drink'   : drink,
      'icecream': icecream,
      'coffee'   : coffee,
      'horse'   : horse,
      'car'     : car,
      'airplane': airplane,
      'ship'    : ship,
      'garden'  : bird_garden,
      'mount'   : mount,
      'jungle'  : jungle,
      'city'    : city,
      'beach'   : beach,
      'train'   : train,
      'pineapple':pineapple,
      'tv'      : television,
      'tv1'     : tv1,
      'tv2'     : tv2,
      'tv3'     : tv3,
      'tv4'     : tv4,
      'tv_off'  : tv_off,
      'on'      : l_on,
      'off'     : l_off,
      'lamp'    : l_on,
      'outside' : out
}
act = {
    'home': ['salon', 'outside', 'exit'],
    'house': ['salon', 'outside', 'exit'],
    'room': ['salon', 'sleep', 'lamp', 'exit'],
    'tv': ['salon', 'tv1', 'tv2', 'tv3', 'tv4', 'exit'],
    'tv1': ['salon', 'tv2', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv2': ['salon', 'tv1', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv3': ['salon', 'tv1', 'tv2', 'tv4', 'tv_off', 'exit'],
    'tv4': ['salon', 'tv1', 'tv2', 'tv3', 'tv_off', 'exit'],
    'tv_off': ['salon', 'tv1', 'tv2', 'tv3', 'tv4', 'exit'],
    'salon': ['outside', 'room', 'kitchen', 'tv', 'exit'],
    'kitchen': ['salon', 'fridge', 'microwave', 'exit'],
    'lamp': ['room', 'off', 'exit'],
    'on': ['room', 'off', 'exit'],
    'off': ['room', 'on', 'exit'],
    'fridge': fridge_i,
    'microwave': microwave_i,
    'outside'  : transport_i,
    'car':['mount', 'city', 'jungle','garden', 'home','exit'],
    'airplane':['mount', 'jungle', 'beach', 'home', 'exit'],
    'horse':['garden', 'jungle', 'mount', 'home', 'exit'],
    'ship':['beach', 'home', 'exit'],
    'train':['city', 'mount', 'home', 'exit'],
    'mount':['car', 'airplane', 'ship', 'horse', 'train', 'exit'],
    'beach':['car', 'airplane', 'ship', 'horse', 'train', 'exit'],
    'city':['car', 'airplane', 'ship', 'horse', 'train', 'exit'],
    'garden':['car', 'airplane', 'ship', 'horse', 'train', 'exit'],
    'jungle':['car', 'airplane', 'ship', 'horse', 'train', 'exit']
    


}

play('house')