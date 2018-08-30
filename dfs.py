def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

def bfs(graph, node, visited):
    visited.append(node)
    q=[]
    q.append(node)

    while q:
        temp=q.pop(0)
        for n in graph[temp]:
            if n not in visited:
                q.append(n)
                visited.append(n)
    return visited

if __name__ == '__main__':
    #creating graph
    graph1 = {
    'A' : ['B','S','H'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C', 'E'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S', 'A'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
    }
    visited1 = bfs(graph1,'A', [])
    visited2 = dfs(graph1, 'A', [])
    print(visited1,'\n', visited2)
    