#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. 
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
nums1 = [31, 21, 31, 46]
print("Array nums1 contains duplicate elements:", contains_duplicate(nums1))
