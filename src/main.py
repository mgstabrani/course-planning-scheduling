from topologicalSort import topologicalSort
from problem import *

# Initialize a graph using array
graf = []

# User introduction
print(50*"=")
name = input("Hello, Enter your name please : ")
print("Welcome", name)
print("We'll help you to decide your course planning")

# Input the problem
inputFile(graf)

# Solve the problem
print("\n" + 50*"=")
print("You can follow this planning to grab your cumlaude")
print(50*"-")
solution = topologicalSort(graf)

# Display the soltuion
outputSolution(solution)