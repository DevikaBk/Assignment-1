#Write a Python program that takes two numbers as input and performs division, handling the case where the divisor is zero. 
try:
  a=int(input("Enter the divident:"))
  b=int(input("Enter the divisor:"))
  c=a//b
except ZeroDivisionError:
  print("Sorry! the divisor is zero")
else:
  print(f"The output of operation is {c} ")
finally:
  print("Thank You")  
