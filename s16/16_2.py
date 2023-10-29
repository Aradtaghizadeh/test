from asc import *


def myinput(items):
    answer = input(f"{items}: ").lower()
    while answer not in items:
        answer = input(f"{items}").lower()
    return answer
def play(a):
    print(p.get(a))
    a = myinput(actions.get(a))
    play(a)

p = {
     'house'    : salon,
     'room'     : room,
     'tv'       : television, 
     'tv1'      : tv1,
     'tv2'      : tv2,
     'tv3'      : tv3,
     'tv4'      : tv4,
     'tv_off'   : tv_off,
     'kitchen'  : kitchen,
     'remote'   : remote,
     'refrigerator':Refrigerator,
     'apple'    : apple,
     'cheese'   : cheese,
     'cake'     : cake,
     'chocolate': chocolate,
     'egg'      : egg,
     'icecream' : icecream,
     'drink'    : drink,
     'l_off'    : l_off,
     'l_on'     : l_on,
     'exit'     : out
}
actions = {
    'out'       : ['house', 'exit'],
    'house'     : ['room', 'kitchen', 'tv', 'exit'],
    'room'      : ['l_on', 'l_off', 'exit'],
    'kitchen'   : ['refrigerator', 'exit'],
    'refrigerator'  : ['apple', 'cheese', 'egg', 'icecream', 'drink', 'chocolate', 'cake', 'exit'],
    'tv'        : ['remote', 'exit'],
    'remote'    : ['tv1', 'tv2', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv1'       : ['tv2', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv2'       : ['tv1', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv3'       : ['tv1', 'tv2', 'tv4', 'tv_off', 'exit'],
    'tv4'       : ['tv1', 'tv2', 'tv3', 'tv_off', 'exit'],
    'l_on'      : ['l_off', 'exit'],
    'l_off'     : ['l_on', 'exit'],
     'tv_off'   : ['tv1', 'tv2', 'tv3', 'tv4', 'exit']
}
print(out)
play('out')


