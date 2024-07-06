#Write a Python program to swap the values of two variables without using a third variable. 
p = int(input("Enter the first number:"))
q = int(input("Enter the second number:"))
p,q = q,p
print(f"The value of first number after swaping is :{p}")
print(f"The value of second number after swaping is :{q}")