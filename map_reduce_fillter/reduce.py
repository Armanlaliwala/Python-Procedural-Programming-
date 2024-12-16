from functools import reduce

l = [5,6,20,10,4,6,4]

def mysum(a, b): #this is with the def function 
    return a + b

sum = reduce(mysum, l) #this will return 25
print(sum)

arr = [5,3,2,4,1]
newarr = reduce(lambda x,y:x+y, arr) #this is with the lambda function 
print(newarr)