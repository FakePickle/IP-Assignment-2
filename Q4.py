import random

#printing rules
def rules():
    print('One random word will be selected from a main word list\n'
    'You have to guess five letter word.\n'
    'You will have 6 attempts to guess the word\n')

#function to check if the letter in correct position or not
def correct_postion(word,guess):
    correct_postion = ""
    for i,j in zip(word,guess):
        if(i==j):
            correct_postion += j
        else:
            correct_postion += '-'
    return correct_postion

#function to check if the letter is in wrong position
def wrong_position(word,guess):
    correct = correct_postion(word,guess)
    wrong_position = ""
    for i in guess:
        if i not in correct:
            if i in word:
                wrong_position += i+', '
    return wrong_position[:-1]

#function where all the user guess take place
def guesser(word):
    #number of attempts set to 6
    attempts = 6
    while(attempts>0):
        print(f"You have {attempts} attempts remaining")
        guess = input("Enter your guess : ")
        #condition to check correct guess in the first attempt
        if(guess==word):
            print("You have guessed the correct word!")
            break
        else:
            #reducing attempt by 1 every run
            attempts -= 1
            #checking correct position
            correct = correct_postion(word,guess)
            print("The letters in the correct position are :- ")
            print(correct)
            #checking wrong position
            wrong = wrong_position(word,guess)
            if wrong is None:
                print("There are no letters in the word")
                pass
            else:
                print("The letters in wrong position are :- ")
                print(wrong)
            #breaking when 0 attempts are remaning
            if attempts==0:
                print("You loose!")
                print("The word is "+word)
                break

#drivers code
if __name__ == '__main__':
    word_list = ['which','there','their','about','would','these','other','words','could','write','first',
    'water','after','where','right','think','three','years','place','sound','great','again','still','every',
    'small','found','those','never','under','might','while','house','world','below','asked','going','large',
    'until','along','shall','being','often','earth','began','since','study','night','light','above','paper']
    #randomly choosing word
    word = random.choice(word_list)
    print(word)
    rules()
    guesser(word)