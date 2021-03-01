from graf_13519122 import *

# Procedure for inputing problem from file
'''
Input data will be graph represented by array
[[<kode_kuliah_1>, 
    [<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>]],
[<kode_kuliah_2>, 
    [<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>]],
[<kode_kuliah_3>, 
    [<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>, <kode kuliah prasyarat - 4>]],
[<kode_kuliah_4>]]

Note:
[[node, [nodes From]]]
'''
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