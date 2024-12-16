# def average(A=8, B = 9): #this is a default Argument 
#     # avg = (A+B)/2.0
#     print("The Avg of", (A+B)/2.0)
# average()

# def Name(Fname= "Ammy", Mname="John" , Lname ="Doe"): #this is a default Argument 
#     print("hello", Fname, Mname, Lname)
# Name(Fname = "Dwain") # this parameter for 1 Arguments are pass in the F - Name
# Name(Mname = "Chamchi") # this parameter for 1 Arguments are pass in the M - Name
# Name(Lname = "Aggarwal") # this parameter for 1 Arguments are pass in the L - Name

# def avg(a,b):   
#     print("the Avg is : ", (a+b)/2)
# avg(b=10, a=15)    # this is a keyword argument


# def avg(a,b = 15):   
#     print("the Avg is : ", (a+b)/2)
# avg(a=15)    # Here "a" is a required argument it should be given compulsary


# def avg(*num): # *args is used when we don't know how many arguments will come. Here * means all the argument
#     sum = 0
#     for i in num:
#         sum = sum +i
#     return sum/len(num) #return the value of  sum/len(num), it basicly store the value
# c = avg(5, 5)
# print(c)


# def avg(*num): # 2 method to print the avg
#     sum = 0
#     for i in num:
#         sum = sum +i
#     print( sum/len(num))  # its a  eg of variable length argument.
# avg(5, 510)

# def name(**name): #this is a dict
    
#     print(type(name)) # this show the type = dict
#     print("Hello", name["Fname"], name["Mname"], name["Lname"])
# name(Fname= "arman", Mname="Imran", Lname="Laliwala")
# print(type(name))
