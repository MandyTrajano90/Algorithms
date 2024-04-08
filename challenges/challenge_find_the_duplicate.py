def find_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] and nums[i] > 0:
            return nums[i]
    return False
