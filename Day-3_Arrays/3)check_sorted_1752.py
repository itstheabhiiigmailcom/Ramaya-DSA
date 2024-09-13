def check(nums):
    n = len(nums)
    count = 0

    # Count the number of places where the array is not sorted
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            count += 1
    
    # If no unsorted pairs, it's already sorted
    if count == 0:
        return True
    # If more than 1 unsorted pair, it's not a rotated sorted array
    elif count > 1:
        return False
    # Otherwise, check if the array is rotated
    else:
        return nums[n - 1] <= nums[0]
