import random

mark = 0

def run():
    getRandom()
    question()
    calcAns()
    calcPoint()

def getRandom():
    global firstNumber
    global secondNumber
    firstNumber = round(random.randrange(1,100))
    secondNumber = round(random.randrange(1,100))

def question():
    ask = "What is "+str(firstNumber)+"+"+str(secondNumber)+"?"
    print(ask)

def calcAns():
    ans = firstNumber+secondNumber
    userAns = int(input("Your Answer:"))
    global mark
    if userAns == ans:
        mark += 1
        print("Answer correct")
    else:
        mark -= 1
        print("Answer incorrect")
        
def calcPoint():
    print("Current Point(s):"+str(mark))
    if mark >= 10:
        print("Congratularions! You beat the challenge!")
        input("Press enter/return to close")
    elif mark <= 0:
        print("Whoops! You failed the game. You got "+str(mark)+" marks.")
        input("Press enter/return to close")
    else:
        run()

run()