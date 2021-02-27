from graf import *

# Procedure for inputing problem from file
def inputFile(graf):
    inputFile = input("Please input your file: ")
    inputFile = open(inputFile, "r")

    print("\n" + 50*"=")
    print("Here are your courses, followed by required courses")
    print(50*"-")
    read = inputFile.readline()
    while(read != ""):
        if(read != "\n"):
            print(read, end="")
            nodes = read.split(", ")
            for i in range(len(nodes)):
                if(i == 0):
                    inputNode(graf, clearNode(nodes[i]))
                else:
                    inputEdge(graf, clearNode(nodes[i]), nodes[0])
        read = inputFile.readline()
    print()

# Procedure for displaying the solution
def outputSolution(solution):
    for i in range(len(solution)):
        print("Semester", i+1, ": ", end="")
        for j in range(len(solution[i])):
            if(j == len(solution[i])-1):
                print(solution[i][j], end=".")
            else:
                print(solution[i][j], end=", ")
        print()
        print()
    print(50*"=")