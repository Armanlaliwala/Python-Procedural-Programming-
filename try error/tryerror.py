# a = input("Enter any number  : ")
# try:
#     for i in range (1, 11):
#         print(int(a), "x", i, "=", int(a)*i)
#     print("\n")
#     a[3,6]
# except ValueError:
#     print("This is a value error") 
# except IndexError:
#     print("This is an index error")  
# except:
#     print("This is an error")          
    
# print("This is some imp line of the program")
# print("This is  the end of the program")


# finally Keyword will allways run in the program
def func1():
    try:
        l=[1,2,3,4,5]
        i = int(input("Enter the index of the list : "))
        print(l[i])
        return 1
    except:
        print("This is an error")
        return 0    
    finally: 
        print("This is finally and it will run no matter what")

x = func1()
print(x)        
