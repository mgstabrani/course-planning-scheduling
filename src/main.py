from topologicalSort import topologicalSort
from input import graf

solution = topologicalSort(graf)
for i in range(len(solution)):
    print("Semester", i+1, ": ", end="")
    for j in range(len(solution[i])):
        if(j == len(solution[i])-1):
            print(solution[i][j], end=".")
        else:
            print(solution[i][j], end=", ")
    print()