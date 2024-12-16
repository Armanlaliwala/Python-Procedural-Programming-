double = lambda x: x+2 #lamda func. is use when we want to define a func in a single line 
print(double(5)) #lamda func is used single variable single time

cube = lambda x: x*x
print(cube(5)) #lamda func is used single variable multi time

avg = lambda x,y : (x+y)/2 #lamda func is used 2 variable 2 time
print(avg(5, 5))

avg_3 = lambda x,y,z:(x+y+z)/3 #lamda func is used 3 variable 3 time
print(avg_3(5,5,5))