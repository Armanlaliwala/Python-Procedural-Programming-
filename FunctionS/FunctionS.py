# a = 9
# b = 8
# Gmean = (a*b)/(a+b)
# print(Gmean)

# Function to calculate geometric mean

# def calGmean(a,b):
#     # Formula for geometric mean
#     mean = (a*b)/(a+b)# geometric mean
#      # Print the result
#     print(mean)

# # c = 11
# # d = 14
# # calGmean(c,d)

# A = int(input("enter any number : \n"))
# B = int(input("enter any number : \n"))
# print("the geometric mean is : ", )
# calGmean(a,b)

# def IsGreater(a,b):
#     if(a>b):
#         print("1st No. is greater")
#     else:
#         print("2nd No. is greater or equal")
        
# A = int(input("enter any number : "))
# B = int(input("enter any number : "))
# IsGreater(A,B)
# calGmean(A,B)

# def IsLowwer(a,b):
#     # the pass function when you will create the function logic afterwards 
#     pass # your code here 

# def name(Fname, Lname):
#     print("Hello ", Fname, Lname)
# Fname = input("Enter 1st name : ")
# Lname = input("Enter 2st name : ")

# name(Fname,Lname)

# def add_numbers():#snake case is used here
#     num1 = float(input("Enter first number:"))
#     num2 = float(input("Enter second number:"))
#     sum = num1 + num2
#     return sum
# # print(add_numbers())
# def sort_array(arr):
#     n = len(arr)
#     for i in range(0, n-1):
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr

# # Example usage
# arr = [64, 25, 12, 22, 11]
# print("Original array:", arr)
# sorted_arr = sort_array(arr)
# print("Sorted array:", sorted_arr)

# def sub(a,b):
#     c = a-b
#     print(c)

# c = int(input("Ente value c = "))
# d = int(input("Ente value d = "))
# sub(c,d)    

# def multi(a,b):
#     c = a*b
#     print(c)

# c = int(input("Ente value c = "))
# d = int(input("Ente value d = "))
# multi(c,d)    

# def div(a,b):
#     c = a/b
#     print(c)
    
# c = int(input("Ente value c = "))
# d = int(input("Ente value d = "))
# div(c,d)    

# def add(a,b):
#     c = a+b
#     print(c)
    
# c = int(input("Ente value c = "))5

# d = int(input("Ente value d = "))
# add(c,d)    

# def sum_natural_no(n):
#     N = n*(n+1)/2
#     print(N)

# n = int(input("Ente value 'n' = "))
    
# sum_natural_no(n)    

# a = int(input("Enter any number : "))

# def fibonacci(n):
#     if (n == 1 or n == 0):
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# for i in range(a):
#     print(fibonacci(i))

# PG - start
# def avg(a,b):
#     c = (a+b)/2
#     print(c)
# def sum(x,y):
#     z = x+y
#     return z

# c = int(input("Ente value c = "))
# d = int(input("Ente value d = "))
# print(f"{avg(c,d)} this is the avg of  {c} and {d}")
# print(f"The sum of {c} and {d} is ", sum(c,d))


# PG - start
def cube(x):
    return x*x*x

# x = int(input("Enter a Number : "))
# print(cube(x))

List = [1,2,3,5,3,5]
NewList = []

for item in List:
    NewList.append(cube(item))    
print(NewList)    