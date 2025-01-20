def add_node(v):
    if v in graph:
        print(v, 'is present in the graph!')
    else:
        graph[v] = []

def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, 'is not present in the graph!')
    elif v2 not in graph:
        print(v2, 'is not present in the graph!')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def del_node(v):
    if v not in graph:
        print(v, ' is not present in the graph!')
    else:
        del graph[v]
        for i in graph:
            li = graph[i]
            if v in li:
                li.remove(v)

def del_edge(v1, v2):
    if v1 not in graph:
        print(v1, 'is not present in the graph!')
    elif v2 not in graph:
        print(v2, 'is not present in the graph!')
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)
        else:
            print(f'{v1} and {v2} have no connection!')

def DFS(start, graph):
    if start not in graph:
        print(start, 'is not present in the graph!')
        return
    visited = [start]
    stack = [start]
    while stack:
        node = stack.pop()
        print(node, '-->', end=' ')
        for i in graph[node]:
            if i not in visited:
                stack.append(i)
                visited.append(i)
    for i in graph:
        if i not in visited:
            print('\nGiven graph is a disconnected graph!')
            break
    else:
        print('\nGraph is a connected graph.')

def BFS(start, graph):
    if start not in graph:
        print(start, 'is not present in the graph!')
        return
    visited = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(node, '-->', end=' ')
        for i in graph[node]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    for i in graph:
        if i not in visited:
            print('\nGiven graph is a disconnected graph!')
            break
    else:
        print('\nGraph is a connected graph.')


graph = {}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_edge('A', 'B')
add_edge('A', 'D')
print(graph)
DFS('A', graph)
BFS('A', graph)
