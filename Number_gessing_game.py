from random import randint

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5


##FUNCTION TO CHECK USER IN GUESS AGINSST ACTUAL AN 

def check_answer(guess ,answer,turns):
    if guess>answer:
        print("to high.")
        return turns -1
    elif guess < answer:
        print("too low .")
        return turns -1
    else:
        print(f"you got it ! the answer was {answer}.")

####  MAKE function to set difficulty.
def  set_difficulty():
    print(logo)
    level=input("Choose  a difficulty  type 'easy' or 'hard'  :")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("welcome to the number guessing game ! ")
    print("I's thinking of a number between 1 and 100 ")
    answer=randint(1,100)
    print(f"psst the correect answer is {answer} ")
    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"you have {turns}  attenpts remaining ti guess the number.")
        guess=int(input("Make a guess: "))

        turns=check_answer(guess,answer,turns)
        if turns ==0:
            print("you have run out of guesses ,you lose. ")
            return
        elif guess !=answer:
            print("Guess again.")

game()