#Write a Python program that prints a multiplication table up to (numberx10). 
Number=int(input("Enter the number:"))
for i in range(1,11):
 print(f"{Number}x{i}={Number*i}")
