#Write a Python function that takes a name and an optional age parameter and prints a greeting. If the age is not provided, it should default to 25
def greet(name,age=None):
  try:
   if age is  None:
     age=25
     print("hello{name}!.You are {age} years old")
  except ValueError:
     print("hello{name}!.You are 25 years old")
  finally:
     print("THANK YOU")
greet("Devika")    
greet("Devika",17)