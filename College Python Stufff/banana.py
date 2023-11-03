def bellmanFord(graph, start):
    distance = {vertex: float('inf') for vertex in graph}
    distance[start] = 0
    for _ in range(0, len(graph) - 1):
        for u, edges in graph.items():
            for v, weight in edges.items():
                if distance[v] > distance[u] + weight:
                    distance[v] = distance[u] + weight
        for u, edges in graph.items():
            for v, weight in edges.items():
                if distance[v] < distance[u] + weight:
                    return "Negative Cycle edges"
    return distance


graph = {'0': {"1": 4, '7': 8}, '1': {'2': 8, '7': 11}, '7': {'6': 1, '8': 7}, '6': {'5': 2, '8': 6}, '8': {'2': 2},
         '5': {'2': 4, '3': 14, '4': 10}, '2': {'3': 7, '8': 2}, '3': {'4': 9}, '4': {'5': 10, '3': 9}}
source_vertex = '0'
result = bellmanFord(graph, source_vertex)
print(f"Shortest distance from source vertex '0':{result}")
