#Write an algorithm to determine if a number n is happy. 
n=int(input("Enter the numbers :"))
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    next_n = 0
    while n > 0:
        digit = n % 10
        next_n += digit * digit
        n //= 10
    n = next_n
if n == 1:
    print("The number is a happy number!")
else:
    print("The number is not a happy number.")