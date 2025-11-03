import math
import random
import time

coefScaling = 3
evalScaling = 5
roundTo = 5

axioms = {
    "^" : "**",
}

spacedTemplates = [
    "n * x",
    "n / x",
    "x ^ n",
    "n ^ x",
    "n + x",
    "n - x"
]

templates = [
    "n*x",
    "n/x",
    "x^n",
    "n^x",
    "n+x",
    "n-x"
]

def genProblem(highestCoef, highestEval):
    coefficient = random.randint(0,highestCoef)
    evaluation = random.randint(1,highestEval)

    problem = list(templates[random.randint(0,len(templates)-1)])

    for char in problem:
        if char == "n":
            problem[problem.index(char)] = str(coefficient)
    
    problem = "".join(problem)
    toEval = list(problem)
    for char in toEval:
        if char == "x":
            toEval[toEval.index(char)] = str(evaluation)
        try: 
            axioms[char]
        except:
            continue
        else:
            toEval[toEval.index(char)] = axioms[char]
            continue

    answer = f'%.{roundTo}f' % eval("".join(toEval))
    problem = problem + " ; when x = " + str(evaluation)
    return "".join(problem), answer

def startGame():
    score = 0
    while True:
        problem, answer = genProblem(math.floor(score/coefScaling)+1, math.floor(score/evalScaling)+2)
    
        print(problem)
        rawInput = input()
        try:
            userAnswer = f'%.{roundTo}f' % float(rawInput)
        except:
            userAnswer = None
        else:
            userAnswer = f'%.{roundTo}f' % float(rawInput)
    
        if userAnswer == answer:
            score += 1
            print("\033[92mCorrect!\033[00m Score : " + str(score))
        else:
            print("\033[91mIncorrect.\033[00m Answer: " + str(answer))
        

# init
print("Play with defaults? (y/n)")
defaultPlay = input()
if defaultPlay == "y":
    startGame()
else:
    print("Easy read problems? (y/n)")
    spacedProblems = input()
    if spacedProblems == "y":
        templates = spacedTemplates
    
    print("Coefficient scaling (higher is easier): ")
    coefScaling = int(input())
    
    print("Evaluation scaling (higher is easier): ")
    evalScaling = int(input())
    
    print("Decimal places: ")
    roundTo = int(input())
    
    startGame()
    

        
        
        
        
        
        
        
        #
