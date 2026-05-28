# Banking Application 

# Deposit
# Withdraw
# BalanceCheck
# Exit

pin=4545

userPin=int(input("Enter your PIN :"))

if userPin==pin:

    print("PIN Verified... ✔✔✔")

    print("Welcome to SLL bank of UK")

    print("""
1. Deposit
2. Withdraw
3. Balance check
4. Exit
   """)

    bankblnc=5000

    choice=int(input("Enter your choice :"))

    if choice==1:
        deposit=float(input("Enter the deposit amount :"))

        if deposit>0:
            bankblnc += deposit
            print("Rs=",deposit,"Has been deposit successfully .. New bank balance Rs. ",bankblnc)
        else:
            print("Invalid amount")
    elif choice==2:
        withdraw=float(input("Enter the withdrawal amount :"))

        if withdraw > 0:

            if withdraw <= bankblnc:
                bankblnc -= withdraw
                print(" Rs. ",withdraw,"Withdrawal successfully done Balance Rs. ",bankblnc)
                
            else:
                print("Insufficient Bank Balance")
        else:
            print("Invalid amount please try again....")

    elif choice == 3:
        print("Your balnce Rs. ",bankblnc)  

    elif choice == 4:
        print("Thanks for using our banking services")

    else:
        print("Invalid choice")

else:
    print("Incorrect Pin... 👎👎")




        



