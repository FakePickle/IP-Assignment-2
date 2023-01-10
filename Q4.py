import random
from colored import fg


def rules():
    print('One random word will be selected from a main word list\n'
    'You have to guess five letter word.\n'
    'If the letter is in correct position and also in the word the letter will be printed green in color\n'
    'If the letter is in the word but not in the correct position the letter will be printed blue in color\n'
    'If the letter is not in word the letter will be printed red in color\n'
    'You will have 6 attempts to guess the word')

def random_word(word_list):
    word = random.choice(word_list)
    return word

def guesser(word):
    attempts = 6
    while(attempts>0):
        guess = input(fg('white') + "\nEnter your guess : ")
        if(guess == word):
            print(fg('green') + guess)
            print(fg('white') + "You have guessed the word correctly.!!!")
            break
        else:
            attempts -= 1
            print(f'You have {attempts} attempt(s) remaining')
            for i,j in zip(guess,word):
                if(i == j):
                    print(fg('green') + i,end = " ")
                elif(i in word):
                    print(fg('blue') + i,end = " ")
                else:
                    print(fg('red') + i, end = " ")
        if attempts == 0:
            print(fg('white') + "\nYou loose")
            print(fg('white') + 'The word is ' + word)

if __name__ == '__main__':
    word_list = ['which','there','their','about','would','these','other','words','could','write','first',
    'water','after','where','right','think','three','years','place','sound','great','again','still','every',
    'small','found','those','never','under','might','while','house','world','below','asked','going','large',
    'until','along','shall','being','often','earth','began','since','study','night','light','above','paper']
    word = random_word(word_list)
    rules()
    guesser(word)