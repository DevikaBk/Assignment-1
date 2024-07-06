#Write a Python program to print a right-angled triangle of '*' with a given number of rows.
n = int(input("Enter the number of row: "))
for i in range(n+1):
 for j in range(i):
  print("*",end=' ')
 print()