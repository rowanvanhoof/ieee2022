from platform import node
import numpy as np
import scipy


class tree_node():

    def __init__(self,index,weight,parent=None):
        self.index = index
        self.weight = weight
        self.childs = []
        self.parent = parent






def main():
    num_nodes = 5
    weights = [9, 11, 11, 13, 13]
    nodes = []

    for i in range(num_nodes):
        temp = tree_node(i+1, weights[i])
        nodes.append(temp)


    for i in range(num_nodes - 1):
        adj = input().split()
        var = int(adj[0])
        var2 = int(adj[1])
        nodes[var-1].childs.append(nodes[var2-1])
        nodes[var2-1].parent = nodes[var-1]

    num_ops = int(input())

    for i in range(num_ops):
        var1 = input().split()
        if int(var1[0]) == 1:
            var2 = int(var1[1])
            nodes[var2+1].weight = int(var1[2])
        else:
            start_index = int(var1[1])
            end_index = int(var1[2])

            curr = nodes[start_index + 1]
            count = 0
            res = 1




    




    # for i in range(len(nodes[0].childs)):
    #     print(nodes[0].childs[i].weight)


main()