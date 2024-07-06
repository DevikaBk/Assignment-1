#Write a Python program to check if a given number is prime or not
Num = int(input("Enter the number:"))
count=0
for i in range (1,Num+1):
 if Num % i == 0:
  count = count+1
if(count>=3):
 print (f"The {Num} is not prime number.")
else:
 print (f"The {Num} is  prime number.")
