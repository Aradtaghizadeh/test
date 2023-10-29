import random
from string import ascii_lowercase


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

l = list(ascii_lowercase)
answer = random.choice(words)
guess = list(len(answer)*'?')
i = 0
guessed_letters= []
print(answer)

while i<7:
    print("".join(guess))
    a = input("Enter one character: ").lower()
    while a not in l:
        a = input("Enter exactly one character: ")
      
    if a in guessed_letters:
        print("This letter has been used.")
        continue
    guessed_letters.append(a)
        
    if a in answer:
        count = answer.count(a)
        index = -1
        for j in range(count):
            index = answer.index(a, index+1)
            guess[index]=a
        if guess == list(answer):
            print(f"____You win____ the answer was {answer}.")
            break
    else:
        print(HANGMANPICS[i])
        i = i+1
if i == 7:
    print(f"____ You lose____ the answer was {answer}.")
                                
        