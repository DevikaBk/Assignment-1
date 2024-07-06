#Write a Python program to print the first 10 numbers of the Fibonacci series.

n=8 #as it is already mentioned first 10 numbers we already have first two so we need to calculate is remaining 8
    # so the number of time for the loop repitation is 8
a=0
b=1
print(f'{a}')
print(f'{b}')
for i in range (n):
 c=a+b
 a=b
 b=c
 print(f"{c}")