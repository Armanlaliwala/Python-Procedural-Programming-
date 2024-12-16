def cube(x):
    return x*x*x

# print(cube(5)) #predefine
# x = int(input("Enter a number ")) #user input method 
# print(cube(x))

#to print the cube of list we do this -- 
List = [1,23,5,44,11,22]
# newlist = []
# for i in List:
#     newlist.append(cube(i))
# print(newlist)    

# but insed we can do --
newl= map(cube,List) # this will print a 0x000001CDB218AA70
print(newl)

#to print the actual list we will use list()
newl= list(map(cube,List)) # this will print a [1, 12167, 125, 85184, 1331, 10648]
print(newl)