from logo import artz
import random
a=random.randint(1,100)#46
count=0
new_count=0
print(artz)
print("Welcome to the Number Guessing game called 'EnigmaGuess'!")
print("I am thinking of a number between 1 and 100")
x=input("Choose the difficulty.Type'easy' or 'hard' or 'medium':")#hard
def attempt(x):
    global count
    if x=='easy':
     count=10
    elif x=='hard':
     count=5
    elif x=='medium':
     count=7
    return count
new_count=attempt(x)#5
print(f"You have {new_count} Attempts remaining to guess the number.")
m=input("Make your guess:")#70
def guess_num(m):#
    global new_count
    global a
    p=("You've run out of guesses. You lose!")
    while(new_count):
        if int(m)>int(a):
            print("Too high.")
            print("Guess again!")
            new_count-=1
            attempt(new_count)
            print(f"You have {new_count} Attempts remaining to guess the number.")
            m=int(input("Make a guess:"))

        elif int(m)<int(a):
             print("Too low.")
             print("Guess again!")
             new_count-=1
             attempt(new_count)
             print(f"You have {new_count} Attempts remaining to guess the number.")
             m=int(input("Make a guess:"))
        elif int(m)==int(a):
             print(f"You got it, the answer was {m}")
             break
        elif new_count==0:
           return p
guess_num(m)



