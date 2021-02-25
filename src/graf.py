def nodeIndex(graf, node):
    index = -1
    for i in range(len(graf)):
        if(graf[i][0] == node):
            index = i
    return index

def inputNode(graf, node):
    if(nodeIndex(graf,node) == -1):
        graf.append([node,[]])

def inputEdge(graf, nodeFrom, nodeTo):
    if(nodeIndex(graf, nodeTo) != -1):
        graf[nodeIndex(graf, nodeTo)][1].append(nodeFrom)
    else:
        inputNode(graf, nodeTo)
        graf[nodeIndex(graf, nodeTo)][1].append(nodeFrom)