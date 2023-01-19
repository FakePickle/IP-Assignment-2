import random
import requests

#printing rules
def rules():
    print('One random word will be selected from a main word list\n'
    'You have to guess five letter word.\n'
    'You will have 6 attempts to guess the word\n')

#api to check if the guess is meaningful or not
def check_word(word):
    app_id = "ccc28cad"
    app_key = "5000c84ad7d2c2776572066bea7cc792	"
    language = "en-gb"
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word.lower()
    r = requests.get(url, headers={"app_id": app_id , "app_key": app_key})
    if word in r.text:
        return 'Yes'
    else:
        return 'No'

#function to check if the letter in correct position or not
def correct_postion(word,guess):
    correct_postion = ""
    for i,j in zip(word,guess):
        if(i==j):
            #if the letter in the word and in the guess is at same position it will add to the string
            correct_postion += j
        else:
            #if the letter in word and in guess is not at same position then a hyphen will be added to the string
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
        #making guess lower to check in the api
        guess = guess.lower()
        #checking the guess in the api
        check = check_word(guess)
        if check=='No':
            print("Please enter a meaningful word")
            pass
        else:
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

if __name__ == '__main__':
    word_list = ['which','there','their','about','would','these','other','words','could','write','first',
    'water','after','where','right','think','three','years','place','sound','great','again','still','every',
    'small','found','those','never','under','might','while','house','world','below','asked','going','large',
    'until','along','shall','being','often','earth','began','since','study','night','light','above','paper']
    #choosing random word
    word = random.choice(word_list)
    print(word)
    rules()
    guesser(word)