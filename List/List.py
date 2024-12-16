# Marks = [1,2,3,4,3,8,5,"Arman"]
# if 7 in Marks: #this is used to check the membership(is present) of a value (7) within the list
#     print("yes ")
# else:
#     print("No")   
    
# if 8 in Marks: #this is used to check the membership(is present) of a value (8) within the list
#     print("yes ")
# else:
#     print("No") 
    
# if "rm" in "Arman":
#     print(Marks.index("Arman"))
#     print("Yess")
# else:
#     print("No")    

# print(Marks)    
# print(Marks[:])
# print(Marks[:-1], "This will be till index 7")
# print(Marks[1:4:2], "Here every 2 element is jumped, jump index")
# print(len(Marks))

# lst = [i*i for i in range(10)] #here i can add a for loop in list
# print(lst)#this will print the square of i, i starts from 0 

# lst = [i*i for i in range(10) if i%2 == 0] #here i can also add if statementin list 
# print(lst)#this will print the squares of even numbers 
# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if "o" in item] # this will print the element that has o in the string
# print(namesWith_O)

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if (len(item) > 4)] #Accepts items which have more than 4 letters
# print(namesWith_O)

# l = [4,5 ,2, 1,0,3,44,22,55]
# l.append(66) #add an element at last
# print(l.pop(5))# Remove and return the element at index 5
# l.sort(reverse=True)#it sorts the elements in the list in the reverse manner   # Sort the list in descending order
# print(l)

# l = [4,5 ,2, 1,0,3,44,22,55]
# l.reverse()
# print(l)
# l = [4,5 ,2, 1,0,3,44,22,55]
# m = l.copy() #this create a copy of a list 
# m[0] = 0
# print(l)
# print(m)
# l.insert(0,556)
# print(l)

# M = [232,323,454,545]
# l.extend(M)#Add elements of one list to another add at last 
# print(l)
