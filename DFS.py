graph ={
    'S':['B','D','A'],
    'A':['C'],
    'B':['D'],
    'C':['G','D'],
    'D':['G'],
    'G':[]  
}

def DFS(graph ,start,goal):
    visited = []
    stack = [[start]]
    while stack:
        path = stack.pop()
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
                stack.append(newPath)    


sol =DFS(graph , 'S','G') 
print('path:',sol)