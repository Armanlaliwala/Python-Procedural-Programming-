def filter_function(a):
    return a>4 # element greater then 4 

L = [1,3,4,5,6,7,9]
newl = filter(filter_function, L) #this wil return <filter object at 0x0000023D1CE7AA10>
print(newl)

newl = list(filter(filter_function, L))#this wil return [5, 6, 7, 9] element greater then 4 
print(newl)