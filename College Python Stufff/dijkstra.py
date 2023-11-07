def Bellman_Ford(graph, start):
    distance = {vertex: float("inf") for vertex in graph}
    distance[start] = 0
    for _ in range(len(graph) - 1):
        for u, edges in graph.items():
            for v, weight in edges.items():
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    return distance


graph = {'X': {"Y": 5, 'Z': 7}, 'Y': {'Z': 3, 'W': 4}, 'Z': {"W": 6}, 'W': {}}
source_vertex = 'X'
result = Bellman_Ford(graph, source_vertex)
print(f"Shortest distances from'{source_vertex}' are : {result}")
