#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. 
numbers = [23,65, 22,22, 23, 56, 65]
result = 0
for num in numbers:
    result ^= num
print("The single number is:", result)