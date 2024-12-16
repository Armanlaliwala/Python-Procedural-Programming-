# i = 0
# while(i<3):
#     print(i)
#     i = i +1
    
# i = int(input("Enter number less then 33 : "))    
# while (i<33):
#     i = int(input("Enter number less then 33 : "))  
#     print(i)  
    
# print("done")

# count = 5
# while(count > 0):
#     print(count)
#     count = count + 1 # this cretes an infinite loop
    
# print("done")    


# count = 5
# while(count > 0):
#     print(count)
#     count = count - 1 # this cretes a decrimenting loop and a finite loop
    
# print("done")    

# count = - 5
# while(count > 0):
#     print(count)
#     count = count - 1 
# else: #checking the else statement in while loop
#     print("im insdide the loop")    
# # print("done")    

while True:
    print("this is a hello from the do while loop")
    us = input("Do you want this (y/n) : \n")
    if us == 'y':
        print("So it is a yes")
    elif us == 'n':
        print("So its no")
    else:
        print("Invalid input. Please enter 'y' or 'n'")
    
    # Check if the user wants to continue
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        break  # Exit the loop if the user does not want to continue


# # Emulating a do-while loop in Python

# # Initialize a flag variable
# flag = True

# # Start the do-while loop
# while flag:
#     # Code block to be executed at least once
#     print("Hello, this is inside the do-while loop")

#     # Ask user if the loop should continue
#     user_input = input("Do you want to continue? (y/n): ")
#     if user_input.lower() != 'y':
#         # Set the flag to False if user does not want to continue
#         flag = False
