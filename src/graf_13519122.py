# Function to find the index from the node
def nodeIndex(graf, node):
    index = -1
    for i in range(len(graf)):
        if graf[i][0] == node:
            index = i
    return index

# Function to clear unused character from the node
def clearNode(node):
    if node[-1] == "\n":
        return node[:-2]
    elif node[-1] == ".":
        return node[:-1]
    else:
        return node

# Procedure to add the node
def inputNode(graf, node):
    if nodeIndex(graf,node) == -1:
        graf.append([node,[]])

# Procedure to add the edge
def inputEdge(graf, nodeFrom, nodeTo):
    if nodeIndex(graf, nodeTo) != -1:
        graf[nodeIndex(graf, nodeTo)][1].append(nodeFrom)
    else:
        inputNode(graf, nodeTo)
        graf[nodeIndex(graf, nodeTo)][1].append(nodeFrom)

# Procedure to delete the edge
def deleteEdge(graf, nodeFrom, nodeTo):
    graf[nodeIndex(graf,nodeTo)][1].remove(nodeFrom)

# Procedure to delete the node
def deleteNode(graf, node):
    popNode = graf.pop(nodeIndex(graf,node))
    for i in range(len(graf)):
        for j in range(len(graf[i][1])):
            if graf[i][1][j] == node:
                deleteEdge(graf, node, graf[i][0])
                break

# Function to find the degree of the node
def degree(graf, node):
    return len(graf[nodeIndex(graf,node)][1])