#Write a Python program to count the number of vowels in a given string. 
String=input("Enter the string:")
count=0
vowel=['A','a','E','e','I','i','O','o','U','u']
for  char in String: 
  if char in (vowel):
   count=count+1
print(f"The vowel count in string is {count}")
