graph ={
    'S':['B','D','A'],
    'A':['C'],
    'B':['D'],
    'C':['G','D'],
    'D':['G'],
    'G':[]  
}

def BFS(graph ,start,goal):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adj_nodes =graph.get(node, [])
            for node2  in adj_nodes:         
                newPath = path.copy()
                newPath.append(node2)
                queue.append(newPath)    


sol =BFS(graph , 'S','G')
print('path:',sol)