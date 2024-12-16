a = 3
b =3
print(a is b) #true both are store on same memory location, as 3 constant and it is immutable 
print(a == b) #true both has same values 

print("\n")

a = [1,3,22]
b = [1,3,22]
print(a is b) #False both are store on diff memory location, as list is mutable 
print(a == b) #true both has same values 

print("\n") 

a = "Arman"
b ="Arman"
print(a is b) #true both are store on same memory location, as  String and it is immutable 
print(a == b) #true both has same values 

print("\n")

a =  (1,2,3,5,6)
b = (1,2,3,5,6)
print(a is b) #true both are store on same memory location, as  String and it is immutable 
print(a == b) #true both has same values 

print("\n")

a =  None
b = None
print(a is b) #true both are store on same memory location, as  String and it is immutable 
print( a is None) #tur because a in none 
print(a == b) #true both has same values 
