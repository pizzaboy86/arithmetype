import math
import random

axioms = [
    "^",
]

pyAxioms = [ # hashtables are too hard
    "**"
]

templates = [
    "n*x",
    "n/x",
    "x^n",
    "n^x"
]

def genProblem(highestCoef, highestEval, arguments):
    if arguments < 1:
        arguments = 1
    problem = ""
    answer = 0
    
    coefficient = random.randint(0, highestCoef)
    evaluation = random.randint(1, highestEval)
    
    template = list(templates[random.randint(0,len(templates)-1)]) # init problem
    template.insert(template.index("n"), str(coefficient))
    template.remove("n")
    problem = "".join(template)
    
    for i in range(arguments-1):
        template = list(templates[random.randint(0,len(templates)-1)])
        template.insert(template.index("n"), str(coefficient))
        template.remove("n")
        problem += " + " + "".join(template)
    
    syntaxxedProblem = list(problem)
    
    counter = 0
    for axiom in axioms:
        if syntaxxedProblem.count(axiom) > 0:
            syntaxxedProblem[syntaxxedProblem.index(axiom)] = pyAxioms[counter]
        counter+=1
    
    for i in range(syntaxxedProblem.count("x")):
        syntaxxedProblem.insert(syntaxxedProblem.index("x"), str(evaluation))
        syntaxxedProblem.remove("x")
    
    print("Evaluated: " + str(syntaxxedProblem))
    
    answer = eval("".join(syntaxxedProblem))
    problem += " when x = " + str(evaluation)
    
    print(problem + " : " + str(answer))
    return problem, answer
    
genProblem(10,3,2)
