letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(f"Hey my name is {name} ?and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!" # this take only 2 digit after the decimal point
print(txt)
# print(txt.format())
print(f"{2 * 30}") # we can use the f string to multi of 2 elements 
print(type(f"{2 * 30}"))
