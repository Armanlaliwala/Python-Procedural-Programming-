Name_Stock = input("Enter Name Of Stock : ")
Stock = float(input('Enter Rs Of One Stock : '))
Balance = float(input('What is your Balance : '))

if Balance > Stock:
    print("You Can Add To Cart")
    max_Stock = Balance // Stock
    if  max_Stock == 0:
        print("Insufficiant Balance ")
    else:   
        print("Maximum number of stock  you can buy:", max_Stock)  
          
        while True:
            Buyornot = input("Do you want to buy stock Y/N : ")
            if Buyornot == 'Y' or Buyornot == 'y':
                Quantity =int(input("How much Quantity You want to buy : "))
                if Quantity  <= max_Stock:
                    print("You have buyed the stock ")
                    price =Stock * Quantity
                    print("Your Total Price Is : ", price , "Rs.")            
                    New_Balance = Balance - price
                    print("The New Balance is : ", New_Balance)        
                    break
                else:
                    print("insufficient balance : Enter quantiy less then or equal to ", + max_Stock)
            elif Buyornot == 'N' or Buyornot == 'n':
                print("You dont want to buy")
                break
            else:
                print("Please enter a valid input (Y/N)")

else:
    print("insufficient balance : Add Funds") 
