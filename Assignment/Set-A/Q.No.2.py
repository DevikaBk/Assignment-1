#Write a Python program that converts a given decimal number to its binary equivalent. 
DecimalNumber = int(input("Enter a decimal number: "))
BinaryNumber = bin(DecimalNumber)
print(f"The binary equivalent of {DecimalNumber} is: {BinaryNumber[2:]}")
