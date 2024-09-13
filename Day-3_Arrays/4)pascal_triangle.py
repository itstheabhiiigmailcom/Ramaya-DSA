def generate(numRows):
    n = numRows
    dp = [[0] * n for _ in range(n)]  # Create a 2D list for Pascal's triangle

    # Fill Pascal's triangle
    for i in range(n):
        for j in range(i + 1):  # Only iterate up to the current row
            if j == 0:
                dp[i][j] = 1  # First element of each row is 1
            elif i == 0:
                dp[i][j] = 0  # This condition is actually redundant
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  # Sum of elements above

    # Extract the triangle up to the required number of rows
    result = []
    for i in range(n):
        result.append(dp[i][:i + 1])  # Append the first i+1 elements of row i

    return result
