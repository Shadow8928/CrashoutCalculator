import sympy
import numpy
from sympy import Symbol
import math
import time
import random
from sympy.codegen import While

insults = ["It is impossible to underestimate you",
           "The only time you are not as dumb as you look is when I close my eyes",
           "You look like something I drew with my left hand", "Your face would make an onion cry",
           "You bring as much joy to the world as a wet sock", "You're why shampoo bottles have instructions",
           "I would say you are dumb as a rock, but at least rocks are useful", "You bring joy to every room you exit",
           "Does it make you sad that you didn't even make the main stage at the circus",
           "You are about as bright as a cave",
           "I'll never forget the day we met, But that does not mean I won't keep trying",
           "You have the attention span of an ice cream in July",
           "I get so emotional when you’re not around, that emotion is happiness",
           "It’s okay to be dumb but don’t abuse it", "If like were a game of chess, you’d be the pawn",
           "You’re as reliable as a chocolate teapot", "You are the proof that evolution can go in reverse",
           "If being clueless were a sport you’d be the MVP", "The wrong sperm won the race",
           "If zombies tried eating your brain they’de starve"]
a = input('Enter Equation: ')
while True:
    if "x" in a:
        print("too complicated just coefficients")
        print("im not even a day old")
        a = input('Enter Equation Without letters: ')
    else:
        break
while True:
    if not ("," in a):
        k = random.randint(0, len(insults))
        # print(insults[k])
        print("add commas between coefficients")
    else:
        break
c = input("you did remember your zeros for coefficients right")
c = list(c)
if c[0].lower() == 'y':
    print("i dont believe you")
if c[0].lower() == 'n':
    print(insults[random.randint(0, len(insults))])
else:
    print(insults[random.randint(0, len(insults) - 1)])
a = input('ReEnter Equation')
ka = True
while ka:
    print('Alpha Question Time')
    time.sleep(1)
    print("Prove Alpha status to pass")
    time.sleep(1)
    print('if a train is going 11 miles/hr')
    time.sleep(1)
    print('and an apple is dropped')
    time.sleep(1)
    print('How large is the sun in terms of gooners')
    a1 = int(input(''))
    if random.randint(1, a1) != 1:
        print(insults[random.randint(0, len(insults))])
        print("wrong Do it again")
    elif a1 == 1:
        print("Alpha Accepted")
        ka = False
        st = 0
    else:
        print('True Sigma Status Unlocked')
        print('You now possess Rizz')
        ka = False
        st = 1
print("I forgot the question can you rewrite it")
while True:
    na = input("enter again")
    if na == a:
        print('looks about right')
        break
    else:
        print(insults[random.randint(0, len(insults))])
        print("Wrong, go again")
print('now to fight the Math Demon')
time.sleep(2)
print('choose your attack')
time.sleep(2)
while True:
    print('1. Fight, 2. Run, 3. Rizz')
    ch = int(input("Option #"))
    if ch == 3 and st != 1:
        print('You Lack possession of Rizz you are now simp')
        rt = input('press enter to try again')
    elif ch == 3 and st == 1:
        print("True Sigma rizz turns demon into simp")
        sm = 1
    else:
        roll = random.randint(1, 20)
        if roll < 15:
            if ch == 2:
                print("Fatty go to the gym she catches you going 2mph")
            if ch == 1:
                print("Fatty that is not muscle it is still fat you get beaten and cooked to render your fat")
        else:
            print('the demon feels bad for you because you lack complete ability and lets you go')
            break
while True:
    print("Time To Face the Final Boss")
    time.sleep(2)
    print("Calculator Bot")
    time.sleep(2)
    print('1. Fight, 2. Run, 3. Rizz')
    ch = int(input("Option #"))
    if ch == 3 and st == 1:
        print("You possess the 6-6-6 package but")
        time.sleep(2)
        print("Robot height is Infinite")
        time.sleep(2)
        print("Robot can create bitcoin for infinite money")
        time.sleep(2)
        print("Robot can also has infinite stamina and length")
        time.sleep(2)
        print("he overpowers you and wins")
    if ch == 3 and st == 0:
        print("you got molested instantly")
    if ch == 2:
        print("you are still fat and get caught and killed")
    if ch == 1:
        chance = random.randint(0, 20)
        if chance == 20:
            print(
                "the robot beats you till death but your blood leaks into his system corroding him and makes him shutdown")
            break
        else:
            print("you die from him literally beating you with his meat")

print('you have won now your question will be answered')
time.sleep(5)
print("The Answer is...")
print("LOADING...")
time.sleep(15)
print("Due to the construction of this game we cannot solve your problem")
print("visit www.chatgpt.com for the answer to your question")
















