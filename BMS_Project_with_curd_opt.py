import mysql.connector as c
con= c.connect(host="localhost",
               user="root",
               passwd="2580",
               database=" bank_management_system")
cursor=con.cursor()

while True:
    print("WELLCOME TO BANK MANAGEMENT SYSTEM! " )
    user_input= input('''
    What Wolud you like To Proceed?
    1. press 1 if you want Open Account
    2. Press 2 if you want to Deposit money
    3. Press 3 if you want to Withdrew money
    4. Press 4 if you want to check Balance
    5. Press 5 if you want Exit
    ''')
    if user_input=="1":
        name=input("Enter your Name: ")
        DOB=input("Enter your DOB: ")
        PAN=input("Enter Your PAN No: ").capitalize()
        ID= int(input("Enter Your ADHAR: "))
        mob=int(input("Enter Your Mobile no.: "))
        amount=float(input("Enter Amount: "))
        query="Insert into customer_details values('{}','{}','{}',{},{},{})".format(name,DOB,PAN,ID,mob,amount)
        cursor.execute(query)
        con.commit()
        print("Account Open SuccessFully")
    elif user_input=="2":
        ID = int(input("Enter Your Adhar No.: "))
        amount=float(input("Enter Amount"))
        query="Update customer_details set amount={} where ID={}".format(amount,ID)
        cursor.execute(query)
        con.commit()
        print("Amount Deposit Successfully!")
    elif user_input=="3":
        amount=float(input("Enter Amount"))
        ID=int(input("Enter Your Adhar No.: "))
        query="Update customer_details set amount={} where ID={}".format(amount,ID)
        cursor.execute(query)
        con.commit()
        print("Amount Withdraw Successfully")
    elif user_input=="4":
        query="select * from customer_details"
        cursor.execute(query)
        details=cursor.fetchmany()
        print(details)
        print("You have Received your Bank Details Successfully")
    elif user_input=="5":
        print("You Are Exited!")
        break
    else:
        break




