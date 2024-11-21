def floyd_warshall(graph):
    # Number of vertices in the graph
    n = len(graph)
    
    # Initialize the distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Set the distance from each vertex to itself to 0
    for i in range(n):
        dist[i][i] = 0
    
    # Set the initial distances based on the input graph
    for u in range(n):
        for v, weight in graph[u].items():
            dist[u][v] = weight
    
    # Update the distance matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Example usage
if __name__ == "__main__":
    # Graph represented as an adjacency list
    graph = {
        0: {1: 3, 2: 8},
        1: {0: 3, 2: 2, 3: 5},
        2: {3: 1},
        3: {0: 4}
    }
    
    shortest_paths = floyd_warshall(graph)
    
    print("Shortest path matrix:")
    for row in shortest_paths:
        print(row)
