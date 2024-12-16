def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial  = n * fact(n-1)
        return factorial
c= int(input("Enter any num : "))    
print(fact(c)) # Outputs 12