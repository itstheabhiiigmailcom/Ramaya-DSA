Code-:
def firstMissingPositive(nums):
    n = len(nums)
    
    # Step 1: Replace all non-positive numbers with a number larger than n
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1
    
    # Step 2: Mark the presence of each number
    for i in range(n):
        val = abs(nums[i]) - 1
        if val < n and nums[val] > 0:
            nums[val] = -nums[val]
    
    # Step 3: Find the first missing positive number
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    return n + 1
