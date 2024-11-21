def optimal_bst(keys, freq):
    n = len(keys)
    
    # Create a table to store the cost of optimal BST
    cost = [[0 for _ in range(n)] for _ in range(n)]
    
    # Fill the diagonal of the cost table
    for i in range(n):
        cost[i][i] = freq[i]
    
    # Build the cost table
    for length in range(2, n + 1):  # length of the subarray
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')  # Initialize cost to infinity
            
            # Try making each key in the range keys[i] to keys[j] the root
            for r in range(i, j + 1):
                # Calculate cost when keys[r] is the root
                c = (cost[i][r - 1] if r > i else 0) + \
                    (cost[r + 1][j] if r < j else 0) + \
                    sum(freq[i:j + 1])  # Add the sum of frequencies
                cost[i][j] = min(cost[i][j], c)  # Update the minimum cost

    return cost[0][n - 1]  # The cost of the optimal BST for the whole array

# Example usage
if __name__ == "__main__":
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    
    min_cost = optimal_bst(keys, freq)
    print("Minimum cost of the Optimal Binary Search Tree is:", min_cost)
