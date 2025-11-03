import math
import random
import time

axioms = {
    "^" : "**",
}

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

    answer = '%.2f' % eval("".join(toEval))
    problem = problem + " ; when x = " + str(evaluation)
    return "".join(problem), answer

score = 0

while True:
    problem, answer = genProblem(math.floor(score/5)+1, math.floor(score/10)+2)
    
    print(problem)
    userAnswer = '%.2f' % float(input())
    
    if userAnswer == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect, answer: " + str(answer))
