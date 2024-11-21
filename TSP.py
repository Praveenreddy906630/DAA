n = 4  # Number of cities

# Distance matrix representing the cost to travel between cities
dist = [[0, 0, 0, 0, 0], 
        [0, 0, 10, 15, 20], 
        [0, 10, 0, 25, 25], 
        [0, 15, 25, 0, 30], 
        [0, 20, 25, 30, 0]]

# Memoization table for storing results of subproblems
memo = [[-1] * (1 << (n + 1)) for _ in range(n + 1)]

def tsp(i, mask):
    # Base case: if only the starting city and the current city are visited
    if mask == ((1 << i) | 3):
        return dist[1][i]

    # Check if the result is already computed
    if memo[i][mask] != -1:
        return memo[i][mask]

    res = float('inf')  # Initialize result for this subproblem

    # Explore all cities to find the minimum cost
    for j in range(1, n + 1):
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            res = min(res, tsp(j, mask & (~(1 << i))) + dist[j][i])
    
    memo[i][mask] = res  # Store the result
    return res

# Driver code to test the function
ans = float('inf')
for i in range(1, n + 1):
    ans = min(ans, tsp(i, (1 << (n + 1)) - 1) + dist[i][1])

print("The cost of the most efficient tour = " + str(ans))
