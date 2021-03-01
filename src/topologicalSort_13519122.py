from graf_13519122 import *

# Function to find the nodes that have zero degree
def findZeroDegree(graf):
    solution = []
    for i in range(len(graf)):
        if(degree(graf,graf[i][0]) == 0):
            solution.append(i)
    return solution

# Function to solve the problem using topological sort
def topologicalSort(graf):
    solution = []
    semester = 0
    while(len(graf) > 0):
        solution.append([])
        zeroDegree = findZeroDegree(graf)
        for i in range(len(zeroDegree)):
            solution[semester].append(graf[zeroDegree[i]-i][0])
            deleteNode(graf, graf[zeroDegree[i]-i][0])
        semester += 1
    return solution