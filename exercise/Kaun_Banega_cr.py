Rs = 0

print("Welcome to kbc")
Q1 =input("Q1. What is 2 + 2 : /n Your option are \nA.4 \nB.6\nC.2 \nD.0 \n")
if (Q1 == "A") or (Q1 == "a"):
    print("You Won ! , You got 5 Rs")
    won = Rs+5
    print(won)
else:
    print("Opps you loose!")    

Q2 =input("Q2. What is 2 / 2 : /n Your option are \nA.1 \nB.0\nC.2 \nD.0 \n")
if (Q2 == "A") or (Q2 == "a"):
    print("You Won ! , You got 5 Rs")
    won = Rs+10
    print(won)
else:
    print("Opps you loose!")    
