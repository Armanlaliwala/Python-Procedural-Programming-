# # print("Hello: ,")
# # a = int(input("Enter your name :"))
# # # print(a)
# # print("Hello :",a)

# # B = (45)
# # print(B)
# # print(type(B))

# #  name = input(("Enter your name : "))
# #  Greeting = ("Hello : ")
# #  print(Greeting + name  )


# # Name =input("Enter Your name  : \n ")
# # date =(input("Enter the date :"))
# # print("Dear," + Name , "you are selected on"  + date)

# # Letter = "Hello Harry, This python course is great thanks you arman"
# # print(Letter)
# # Letter = "Hello Harry,\nThis python course is great \nthanks you \narman"
# # print(Letter)

# # Str = 'Arman  laliwala is a boi '
# # print(Str.find("a"))
# # program 3
# # Str= Str.replace('  ', ' ')
# # print(Str)

# # L1 = ["ios, andriod, pokimon"]
# # print(L1)
# # L2 = [1,2,23,44,3,5, 8,99,56]
# # print(L2)

# # L2.pop()#pops or remove out an element at a desired index
# # print(L2)
# # A = len(L2)
# # print(A)

# fruits = ['banana', 'Mangoes', 'grapes', 'watermelon']
# i= 0
# while i < len(fruits):
#     print( fruits[i], str(i))
#     i = i+1


# # fruits = ['banana', 'mangoes', 'grapes', 'watermelon']
# # i =0
# # while i < len(fruits):
# #     print(fruits[i], str(i))
# #     i = i+1

# # print("Hello this is my number", 7405006001 , sep=": ", end=" thank u \n")

# # print(
# #     "this is the "  + "python programming language"
# # )

# # name = input("Enter your name: ")
# # print("Hello, " + name + "!")

# # Add = input("Enter a number :")
# # print("this is = " + Add)
# # No = int(input("Enter another number :"))
# # print("the sum of both numbers are =" + str(int(Add)+int(No)))
# # print(str(int(Add)+int(No)))
# # print(type(Add), type(No))

# # A = 50
# # B = 40
# # print("this is the", A, "+", B,"=", A+B)
# # print("this is the", A, "-", B,"=", A-B)
# # print("this is the", A, "*", B,"=", A*B)
# # print("this is the", A, "/", B,"=", A/B)
# # print("this is the", A, "//", B,"=", A//B)# it will show integer division only
# # print("this is the", A, "**", B,"=", A**B)

# # a = "5"
# # b= '6'
# # print(int(a)+ int(b))

# # a = input("enter your name : ")
# # print("your name is :",a)

# # a = 8 
# # b = "Arman"
# # print(str(int(a)) + b)
# # print(b[0])
# # # print(b[2])
# # print("this is a new line of code ")
# # b="this is ok"
# # for word in b:
# #     print(word)

# # names = "Arman, Harry, Ruhan"
# # print(names[0:5]) #from  index 0 to 5 but not including 5
# # print(names[7:12]) 
# # print(names[:9]) # from    index 0 to 9 but not including 9      
# # print(names[14:19])
# # print(len(names))


# # Fruits = "Mangos"
# # len1 = len(Fruits)
# # print(len1)
# # print("Mangos is a ",  len1 ,  "Character word")


# # name = "Harry"
# # # print(
# # #     name[:-3]
# # # )
# # # print(
# # #     name[-1]
# # # )
# # print(
# #     name[-4:-2]
# # )

# # a = "armannnnnn"
# # print(a)
# # # print(a.rstrip("n")) #this creates removes characters that match the argument (here n)


# # a = "armannnnnn"
# # print(a.replace("armannnnnn", "Arman")) # this creates  a function that replaces the old string with the

# # b ="Arman ruhan imran"
# # print(b.split(" ")) # this creates a  list of words in the string b

# # blog = "this is the To success"
# # print(blog.upper()) # this makes all letters capital
# # print(blog.lower()) # this makes all letter small
# # print(blog.title()) # this make first character of each word capital and rest are small
# # print(blog.capitalize()) #this  only makes the first character capital

# # str1 ="This is the heading : Success"
# # print(str1.find("ooo")) # This shows where it finds the substring in the given string , if not found then it will show -1
# # print(len(str1))
# # print(len(str1.center(50))) # This will center the text between two given lengths
# # print(str1.center(50)) 
# # print(str1.center(100)) 

# # a = "Arman Airwen Arbone "                         
# # print(a.count("A")) # this count the element  A from the string a.
# # print(a.endswith(" ")) #this show that the character that with the Space("_")
# # print(a.find("Airwe"))  # it shows the position of the element which we want to find,if not found it shows -1
# # print(a.index("Arbon"))   # same as above but if the element is not there it gives an error


# # A ="Armam"
# # print(A.islower()) #this check the string is in lower case or not if yes the ture else return false 
# # print(A.istitle()) #this check the string is title casing or not if yes then true else falseṇ
# # print(A.isupper()) #this check the string is uppercase or not if yes then true else false
# # print(A.startswith("A"))

# # a = "thisisanormallineofcode"                         
# # print(a.isalnum())# The isalnum() method in Python returns True if all characters in the string are alphanumeric (either alphabets or numbers) and there is at least one character, otherwise it returns False.(Space is a special charater )   
                         
# # names = "Arman, Harry, Ruhan" #this is using a string method 
# # rev_name = names[::-1]
# # print(rev_name)


# s = "Arman" # this is using a for loop
# reversed_s = ""  
# for Char in s:
#     reversed_s = Char + reversed_s
# print(reversed_s)

# # Rev_S ="world hello"
# # rev_s = Rev_S[::-1]
# # print(rev_s)


# # #this is a reverse string 
# # string = "This is hello in reverse"
# # Reverse = string[::-1]
# # print(Reverse)

# # #this is a reverse string
string = "123456789"
string.reversed()
print(string)