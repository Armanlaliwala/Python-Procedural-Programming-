#p1

# import pandas as pd
# dic ={
#     "arman": "Python",
#     "Imran": "Owner",
    
# }
# print(dic.get("Imran")) # Imrans role in the company is Owner
# print(dic.get("arman")) # arman role in the company is python developer
# print(dic)

# df = pd.DataFrame(dic.items(), columns=["Name", "Role"])
# print(df)

#p2

# dic ={
#     "arman": "Python",
#     "Imran": "Owner",    
# }
# print(dic)
# keys_list = list(dic.keys()) #this print all the keys in the dictionary
# print(keys_list)
# values_list = list(dic.values()) #this print all the values of dictionary
# print(values_list)

#p3

# dic = {
#     1: "Arman", 
#     2: "Imran",
#     3: "Ruhan"
# }
# print(dic[1])

# Value = list(dic.values()) #this print all the values of dictionary
# print(Value) #output will be values of dictionary

# key =list(dic.keys()) #this print all the keys in the dictionary
# print(key) #output will be keys in the dictionary

# Value1 = dic[1] #this is same as print(dic[1])
# print(Value1) #output will be Arman

# dict = list(dic)
# print(dic.items()) #this will print the whole dictionary in a list manner 
# print(dic) #this will print the whole dictionary

#p4

# info = {
#     "name" : "Arman",
#     "age" : 20,
#     "country" : "india",
#     "RollNo" : "123",
#     "Subject" : "Python",
# }

# print(info)
# print(info['name']) #output will be Arman and raise an error if name is not present in the dictionary
# print(info.get('name')) #output will be Arman this will not raise an error if name is not present in the dictionary the output will show none if the name is not present in the dictionary
# print('\n')

# print(info.get('name', "Not Found")) #output will be Arman this will not raise an error if name is not present in the dictionary the output will show Not Found if the name is not present in the dictionary
# print('\n')

# print(info['name']) #output will be an error because if name is not present in the dictionary
# print(info.keys()) #this will be print all the keys of the dictionary
# print(info.values()) #this will be print all the values of the dictionary
# print('\n')

# for key in info:
#     print(key, info[key]) #output will be all the keys and values of the dictionary
# print('\n')

# for key in info.keys():
#     print(key) #output will be all the values of the dictionary
# print('\n')

# for key in info.keys():
#     print(info[key]) #output will be all the values of the dictionary

# for key, value in info.items():
#     print(f"the values that are corresponding to {key} is {info[key]}") #output will be all the values of the dictionary
# print("\n")   
 
# print("this is the dic", info.items()) #output will be all the items of the dictionary
# for key, value in info.items():
#         print(key, value) #output will be all the keys and values of the dictionary one by one
# for key, value in info.items():
#         print(f"The Values That Are Corresponding to {key} is {value}") #output will be all the keys and values of the dictionary one by one
        
  # -->  ##practice program : -   
      
# dic = {
#     1: "Arman", 
#     2: "Imran",
#     3: "Ruhan"
# }        
# for key, values in dic.items():
#     print(f"this is {key} is {values}")

# print(dic)  
# print(dic[2])# output will be Imran
    
#p5
# Books = {
#     1 : "Python",
#     2 : "Java",
#     3 : "C++",
#     4 : "C#",
#     5 : "Ruby",
#     6 : "Rust"
# }    

# print(Books)
# print(Books.items())
# print(Books[5])
# for keys, Values in Books.items():
#     print(f"the book_id {keys} is for {Values}")