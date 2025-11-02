import math
import random

axioms = {
    "^" : "**",
}

templates = [
    "n*x",
    "n/x",
    "x^n",
    "n^x",
    "n+x",
    "n-x",
    "(n/x)*(n^x)"
]

def genProblem(highestCoef, highestEval):
    coefficient = random.randint(0,highestCoef)
    evaluation = random.randint(1,highestEval)

    problem = list(templates[random.randint(0,len(templates)-1)])

    for char in problem:
        if char == "n":
            problem[problem.index(char)] = str(coefficient)
    
    toEval = problem # same memory position, changes both for some reason!

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

    answer = eval("".join(toEval))
    problem = str(problem) + " ; when x = " + str(evaluation)

    print("Problem: " + "".join(problem))
    print("Answer: " + str(answer))
    return problem, answer


for i in range(10):
    genProblem(10,10)

    #make i/o

    

