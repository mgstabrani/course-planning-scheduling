from graf import *
print(50*"=")
name = input("Hello, Enter your name please : ")
print("Welcome", name)
print("We'll help you to decide your course planning")
inputFile = input("Please input your file: ")
inputFile = open(inputFile, "r")
graf = []

print(50*"=")
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