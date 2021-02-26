def nodeIndex(graf, node):
    index = -1
    for i in range(len(graf)):
        if(graf[i][0] == node):
            index = i
    return index

def clearNode(node):
    if(node[len(node)-1] == "\n"):
        return node[:-2]
    elif(node[len(node)-1] == "."):
        return node[:-1]
    else:
        return node

def inputNode(graf, node):
    if(nodeIndex(graf,node) == -1):
        graf.append([node,[]])

def inputEdge(graf, nodeFrom, nodeTo):
    if(nodeIndex(graf, nodeTo) != -1):
        graf[nodeIndex(graf, nodeTo)][1].append(nodeFrom)
    else:
        inputNode(graf, nodeTo)
        graf[nodeIndex(graf, nodeTo)][1].append(nodeFrom)

def deleteEdge(graf, nodeFrom, nodeTo):
    graf[nodeIndex(graf,nodeTo)][1].remove(nodeFrom)

def deleteNode(graf, node):
    popNode = graf.pop(nodeIndex(graf,node))
    for i in range(len(graf)):
        for j in range(len(graf[i][1])):
            if(graf[i][1][j] == node):
                deleteEdge(graf, node, graf[i][0])
                break

def degree(graf, node):
    return len(graf[nodeIndex(graf,node)][1])