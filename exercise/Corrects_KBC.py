questions = [
    ["What is 2 + 2", "1", "5", "0","4", 4],
    ["What is 2 x 2", "1", "5", "4","0", 3],
    ["What is 2 - 2", "4", "5", "1","0", 4],
    ["What is 2 + 3", "4", "1", "0","5", 4],
    ["What is 3 - 2", "4", "5", "0","1", 4]
]
levels = [100, 200, 300, 400, 500]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\n\n{i +1 } Question for Rs{levels[i]}")
    print(question[0])
    print(f"a.{question[1]}     b.{question[2]}")
    print(f"c.{question[3]}     d.{question[4]}")
    reply = int(input("Enter Your Answer (1-4) or 0 to Quit:\n"))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct Answer, You have won Rs. {levels[i]}")
        if(i == 1):
            money =200
        elif ( i == 3):
            money = 400  
        elif(i==4):
            money = 500   
    else:
        print("Wrong Answer")
        break
print(f"Your take home moneyy is {money}")    