from topologicalSort import topologicalSort
from input import graf

print("\n" + 50*"=")
print("You can follow this planning to grab your cumlaude")
print(50*"-")
solution = topologicalSort(graf)
for i in range(len(solution)):
    print("Semester", i+1, ": ", end="")
    for j in range(len(solution[i])):
        if(j == len(solution[i])-1):
            print(solution[i][j], end=".")
        else:
            print(solution[i][j], end=", ")
    print()
print(50*"=")