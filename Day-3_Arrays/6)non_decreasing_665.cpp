def checkPossibility(nums):
    n = len(nums)
    count = 0
    
    for i in range(1, n):
        if nums[i - 1] > nums[i]:
            # If more than one modification is needed, return False
            if count > 0:
                return False

            # Check if modifying nums[i - 1] or nums[i] will fix the issue
            if i > 1 and nums[i - 2] > nums[i]:
                nums[i] = nums[i - 1]  # Modify nums[i] to nums[i - 1]
            else:
                nums[i - 1] = nums[i]  # Modify nums[i - 1] to nums[i]

            count += 1

    return count <= 1
