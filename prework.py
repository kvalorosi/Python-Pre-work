#Question_1
#Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
   
   print("hello_" + user_name.upper() + "!")  

hello_name("username")



#Question_2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds(odd_numbers):
   
   for odd in odd_numbers:
      
      if odd % 2 != 0:
         
         print(odd)
         
number = range(1,100)
first_odds(number)

#Question_3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
#The first block of code you see is my code that I created, the second code block is the correct code from the internet. I posted both for reference. 
def max_num_in_list(a_list):
   for list in a_list:
      list = int(list)
      list = max(list)
      print(list)

numbers = [1,2,3,4,5,6,7,8,9,10]
max_num_in_list(numbers)


def max_num_in_list(a_list):
    max_num = a_list[0]  
    for num in a_list:
        if num > max_num:
            max_num = num
    
    return max_num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_num_in_list(numbers))



#Question_4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
   for leap in a_year:
       
       if leap % 4 == 0 and leap % 400 == 0:
          
          return True
       
       else:
          
          leap % 100 == 0

          return False


#Question_5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# I didn't get any errors when I ran this block of code, but when I looked up other possible answers mine didnt't look like them. I'm not sure if my block of code for question 5 is correct or not.

def is_consecutive(a_list):
   sorted_list = sorted(a_list)
   
   for order in a_list:

      if order.sorted():

         return True

      else:
         
         return False





       
       
       
       


 
          


          
          

             



   
   
   
         
   
         
    


      


   
      
   
   



         
        



