# PG - 1(To Check if you can vote or not !)
# Age = int(input("Enter Your Age : "))
# print("Your Age Is : ",Age)
# if  Age >= 18 :
#     print("You are able to vote ")
# else:
#     print("you are not able to vote yet ")    
#     print("You will be able to after : ", 18 - Age, "Years")
  
# if(Age>=13 and Age<=19)    :
#     print("You are in your teen")
    
# elif (Age>= 19) :
#     print("you are a adult")
        
# else:
#     print("you are a child ")    
    
# PG - 2 (To Check Wether you can buy stock or not and check max quantity you can buy )    
# Stock = float(input('Enter Rs Of One Stock : '))
# Balance = float(input('What is your Balance : '))
# if Balance > Stock:
#     print("You Can Add To Cart")        
# else:
#     print("Add Funds")    
# max_Stock = Balance // Stock #// is when you used // operator then it will only take interger eg: - 10/3 = 3.333 10//3 = 3
# if  max_Stock == 0:
#     print("Insufficiant Balance ")
# else:
#         print("Maximum number of stock  you can buy:", max_Stock)

#PG - 3 (To check the number is positive or not and to check is it even and can be divied by 2 or not )
# num = int(input("Enter a value for num : "))
# if num < 0:
#     print("The number is negative ")
    
# elif num > 0:
#     print("The number is positive ")
#     if num >0 and num <=20:
#         print("it is in between 0 to 20")
#     elif num >21 and num <=50:
#         print("it is between 21 to 50")   
#     else:
#         print("the number is more then 50 ")     
# else:
#     print("The number is 0")    
    
# if num % 2 ==0:
#     print("the number is divisible by 2 " )
#     print("The division by 2 is : ", num / 2)
# else:
#     print("The number is odd & it cant be completly divide by 2")   
#     print("The Remender is : ", num % 2)

import time

time_stamp = time.strftime('%H:%M:%S')
print(time_stamp) 
