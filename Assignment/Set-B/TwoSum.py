#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order. 
Numbers = [33,37, 11, 15,66]
target = 26
NumIndex = {}
for i in range(len(Numbers)):
    num = Numbers[i]
    complement = target - num
    if complement in NumIndex:   
        print("Indices of the two numbers are:", [NumIndex[complement], i])
        break
    NumIndex[num] = i