# x=int(input("Enter a number: "))
# match x:
#     case 0:
#         print("X is zero")
#     case _ if x >0:
#         print(f"{x} is positive ") # fstring is used
#     case _ if x <0:
#         print(x," it is a negative")

while True:
 a = int(input("Enter a 1st number : "))        
 b = int(input("Enter a 2st number : "))        
 x = int(input("Enter :  1 to (a+b),\nEnter :  2 to (a-b),\nEnter :  3 to (a*b),\nEnter :  4 to (a/b) \n"))  

 match x:
     case 1:
         print(a+b)
     case 2:
         print(a-b)
     case 3:
        print(a*b)        
     case 4:
         print(a/b)  
     case 5:
         print("Enter valid input ")           
 break


        
        