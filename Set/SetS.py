# s= {2 ,4,2,5}
# print(s)
# print(type(s)) #type SET
# print(s[2])

#Set Methods
    #Joining Set
    
# s1 ={1,2,5,6} 
# s2={3,6,7}
# print(s1.union(s2)) #common elements are removed
# print("The S1 And S2 will remain untouched :",s1,s2)
# s1.update(s2) #this line of code update the s1 , It includes the all element present in s2 
# print(s1)

# cities1 = {"Abad", "Surat", "Baroda"}
# cities2 = {"bomay", "Abad", "vapi"}
# cities3 = cities1.union(cities2) #common elements are removed
# print(cities3)

# cities1 = {"Abad", "Surat", "Baroda"}
# cities2 = {"bomay", "Abad", "vapi"}
# cities3 = cities1.intersection(cities2) #comman Element only
# print(cities3)

# cities1 = {"Abad", "Surat", "Baroda"}
# cities2 = {"bomay", "Abad", "vapi"}
# cities1.intersection_update(cities2) #this will take comman Element onlyand directly update the cities1
# print(cities1)


# cities1 = {"Abad", "Surat", "Baroda"}
# cities2 = {"bomay", "Abad", "vapi"}
# cities3 = cities1.symmetric_difference(cities2)
# print(cities3)


# cities1 = {"Abad", "Surat", "Baroda"}
# cities2 = {"bomay", "Abad", "vapi"}
# cities3 = cities1.difference(cities2)
# print(cities3)

# Disjoint Set:

# cities1 = {"Abad", "Surat", "Baroda"}
# cities2 = {"bomay", "Abad", "vapi"} #Disjoint set means there is no common element between two sets
# cities3 = cities1.isdisjoint(cities2)
# print(cities3) #this return true or false #in this case false because abad is in both set

# cities1 = {"abu", "Surat", "Baroda"}
# cities2 = {"bomay", "Abad", "vapi"} #Disjoint set means there is no common element between two sets
# cities3 = cities1.isdisjoint(cities2)
# print(cities3) #this return true or false #in this case True because no repeating of element in set

# #superset
# cities1 = {"Abad", "Surat",  "vapi", "Baroda"}
# cities2 = { "Abad", "vapi"} # all element of cities2 should be in cities1 
# cities3 = cities1.issuperset(cities2)
# print(cities3)  #this return true or false #in this case True because all element of cities2 are in cities1 

# cities1 = {"abu", "Surat", "Baroda"}
# cities2 = {"bomay", "Abad", "vapi"} # all element of cities2 should be in cities1 
# cities3 = cities1.issuperset(cities2)
# print(cities3)  #this return true or false #in this case false because all element of cities2 are not in cities1 

# #subset
# cities1 = {"Abad", "Surat",  "vapi", "Baroda"}
# cities2 = { "Abad", "vapi","Abad", "Surat",  "vapi", "Baroda"} # all element of cities1 should be in cities2
# cities3 = cities1.issubset(cities2)
# print(cities3)  #this return true or false #in this case True because all element of cities1 are in cities2

# cities1 = {"abu", "Surat", "Baroda"}
# cities2 = {"bomay", "Abad", "vapi"}# all element of cities1 should be in cities2
# cities3 = cities1.issubset(cities2)
# print(cities3) #this return true or false #in this case false because all element of cities are not in cities2

# add method
# A = {1,2,3,4}
# A.add(5) #This methos is used to add a single element into the set
# print(A)

# # update method
# A = {1,2,3,4}
# B= {5,6,5,7,8}
# A.update(B) #This is update method which adds multiple elements at once
# print(A)

# # Remove() method
# A = {1,2,3,4}
# A.remove(4) #This is use to remove element from the set and if a element is not present in the set then it raises a error
# print(A)

# # Remove()\ method
# A = {1,2,3,4}
# A.remove(5) #This is use to remove element from the set and if a element is not present in the set then it raises a error
# print(A) #this will give error if we try to remove an element from set

# # discard() method
# A = {1,2,3,4}
# A.discard(5) #This is use to remove element from the set and if a element is not present in the set then it will not raises an error but printing the set
# print(A) 

# # discard() method
# A = {1,2,3,4}
# A.discard(4) #This is use to remove element from the set and if a element is not present in the set then it will not raises an error but printing the set
# print(A) 

# #pop method
# A = {1,2,3,4}
# item = A.pop() #pop is used to remove last element from the set but  the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
# print(A) 
# print(item) #this is a variable  that we can assign any value to it and then use it inside pop method

# # del keyword it is not a method
# A ={1,2,3,4}
# print(A)
# del A #this set A is not deleted
# print(A) # now this will show error because set A is deleted

#clear method
# A ={1,2,3,4,5}
# A.clear()
# print(A) #this is a empty set now
# print(type(A))

# # to check the elemet is present in the set or not 
# A ={1,2,3,4,5,6,7,8,9,1,0}
# if 1 in A:
#     print("The number is present")
# else:
#     print("The number not is present")