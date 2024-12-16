x = 5
print(f"this is a global variable {x}")
def my():
    global x
    x = 4
    print(f"here the global variable is changed to {x}")
my()    

print("now the global variable is ",x)