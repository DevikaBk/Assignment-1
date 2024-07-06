#Write a Python function that takes a list of numbers and returns the maximum value in the list
number_list=[1,2,5,7,9,2,13,35,55,32]
MaxValue=number_list[0]
for num in number_list:
   if(num>MaxValue):
     MaxValue=num         
print(f"The maximum number in the list is {MaxValue}")
 
   
   
   
   
   
   
   