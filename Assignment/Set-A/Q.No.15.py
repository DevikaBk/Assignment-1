#Write a Python program to print a pyramid of '*' with a given number of rows. 
n=int(input("Enter the number rows for central pyramid:"))
for i in range(n):
  for j in range(n-i-1):
     print(" ",end=" ")
  for k in range(i+1):
     print("*", end=" ")
  for l in range(i):
    print ("*",end=" ")  
  print()