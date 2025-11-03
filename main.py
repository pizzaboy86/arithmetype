import math
import random
import time

axioms = {
    "^" : "**",
}

templates = [
    "n * x",
    "n / x",
    "x ^ n",
    "n ^ x",
    "n + x",
    "n - x"
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

    answer = '%.2f' % eval("".join(toEval))
    problem = problem + " ; when x = " + str(evaluation)
    return "".join(problem), answer
    
score = 0
print("Score: " + str(score))

while True:
    problem, answer = genProblem(math.floor(score/3)+1, math.floor(score/5)+2)
    
    print(problem)
    rawInput = input()
    try:
        userAnswer = '%.2f' % float(rawInput)
    except:
        userAnswer = None
    else:
        userAnswer = '%.2f' % float(rawInput)
    
    if userAnswer == answer:
        score += 1
        print("\033[92mCorrect!\033[00m Score : " + str(score))
    else:
        print("\033[91mIncorrect.\033[00m Answer: " + str(answer))
        
        
        
        
        
        
        
        
        #
