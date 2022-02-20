graph ={
    'S':[('A',2),('B',3),('D',5)],
    'A':[('C',4)],
    'B':[('D',4)],
    'C':[('D',1),('G',2)],
    'D':[('G',5)],
    'G':[]
}

# function to return total cost of a given path
def path_cost(path):
    total_cost = 0
    for (node,cost) in path:
        total_cost += cost
    return total_cost , path[-1][0]


def UCS(graph,start,goal):
    visited =[]
    p_queue = [[(start,0)]]
      

    while p_queue:
        p_queue.sort(key=path_cost) #sort using cost and if cost is simillar sort by alpahpet
        path = p_queue.pop(0) #take the least cost
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if goal == node:
            return path
        else:
            adj_nodes =graph.get(node, [])
            for (node2 ,cost) in adj_nodes:         
                newPath = path.copy()
                newPath.append((node2,cost))
                p_queue.append(newPath)




solution = UCS(graph,'S','G')

print("path :", solution)
print("Cost :" , path_cost(solution)[0])