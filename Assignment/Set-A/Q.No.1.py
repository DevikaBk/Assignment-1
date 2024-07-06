#Write a Python program that simulates a basic calculator, performing addition, subtraction, multiplication, and division. 
print("Choose the option")
print(" 1 for Addition")
print(" 2 for Subtraction")
print(" 3 for Multiplication")
print(" 4 for Division")
option = int(input("Choose operation:"))
if option not in[1,4]:
 print("Invalid Input.Please! Choose the option among 1,2,3,and 4 only.") 
else:
 num1 = int(input("Enter the first number:"))
 num2 = int(input("Enter the second number:")) 
 if (option==1):
   print(f"The addition of {num1} and {num2} is:{num1+num2}")
 elif (option==2): 
   print(f"The subtraction of {num1} and {num2} is:{num1-num2}")
 elif (option==3):
   print(f"The multiplication of {num1} and {num2} is:{num1*num2}")  
 else:
  if(num2==0):
    print("Divided by zero.")
  else:
    print(f"The division of {num1} and {num2} is:{num1/num2}")
 
    