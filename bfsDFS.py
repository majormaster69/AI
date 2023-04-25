from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    while queue:
        vertex=queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
    
def dfs(graph, start ,visited=None): 
    if visited is None:
        visited =set()
    visited.add(start)
    print(start)
    for neighbour in graph[start]: 
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
graph = {}
num_edges = int(input("Enter No.of Edges: "))
for i in range(num_edges):
    edge=input(f"Enter edge {i+1} a 'from to':")
    edge=edge.split()
    if edge[0] not in graph:
        graph[edge[0]]=[]
    if edge[1] not in graph:
        graph[edge[1]]=[]
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
start =input("enter the start vertex: ")
print("DFS: ")
dfs(graph, start)
print("BFS: ")
bfs(graph, start)