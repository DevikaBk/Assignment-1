#Write a Python program that takes three numbers as input and checks if the third number is the sum of the first two numbers using logical operators. 
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if (c==a+b or c==b+a):
 print(f' Yes, {c} is sum of {a} and {b}')
else:
  print(f' No, {c} is not sum of {a} and {b}')
