from graf import *

inputFile = input("Input file: ")
inputFile = open(inputFile, "r")
graf = []

read = inputFile.readline()
while(read != ""):
    if(read != "\n"):
        nodes = read.split(", ")
        for i in range(len(nodes)):
            if(i == 0):
                inputNode(graf, clearNode(nodes[i]))
            else:
                inputEdge(graf, nodes[0], clearNode(nodes[i]))
    read = inputFile.readline()