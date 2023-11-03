def Bellman_Ford(graph, start):
    distance = {vertex: float("inf") for vertex in graph}
    distance[start] = 0
    for _ in range(len(graph) - 1):
        for u, edges in graph.items():
            for v, weight in edges.items():
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
        for u, edges in graph.items():
            for v, weight in edges.items():
                if distance[u] + weight < distance[v]:
                    return "Negative-weight cycle detected"

    return distance


# graph = {'0': {"1": 4, '7': 8}, '1': {'2': 8, '7': 11}, '7': {'6': 1, '8': 7}, '6': {'5': 2, '8': 6}, '8': {'2': 2},
#          '5': {'2': 4, '3': 14, '4': 10}, '2': {'3': 7, '8': 2}, '3': {'4': 9}, '4': {'5': 10, '3': 9}}
graph = {'A': {'B': 1}, 'B': {'C': -1}, 'C': {'A': -1}}
source_vertex = 'A'
# source_vertex = '0'
result = Bellman_Ford(graph, source_vertex)
print(f"Shortest distance from source vertex '0':{result}")
