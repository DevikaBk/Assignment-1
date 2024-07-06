#Given an integer x, return true if x is a palindrome, and false otherwise. (LeetCode: Palindrome Number) 
x=int(input("Enter an integer:"))
x_str=str(x)
reverse=x_str[::-1]
if (x_str==reverse):
 print("True")
else:
 print("False")