from bank import Bank
from user import User
from admin import Admin

bank = Bank('Bangla Bank','Dhaka')
admins = [{'email' : 'admin','password' : 'admin' },]

def User_menu(user):
    print(f'\nWelcome to {bank.name}\n')
    while True:
        print("Option : ")
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Check Balance')
        print('4. Check Transaction')
        print('5. Transfer Money')
        print('6. Take Loan')
        print('7. Exit')
        
        op = int(input("Enter Your Choice : "))
        
        if op == 1:
            amount = int(input("Enter Deposit Amount : "))
            user.deposit(amount,bank)
        elif op == 2:
            amount = int(input("Enter Withdraw Amount : "))
            user.withdraw(amount,bank)
        elif op == 3:
            user.check_balance()
        elif op == 4:
            user.check_transaction()
        elif op == 5:
            transfer_ac_number = int(input("Enter Transfer Account Number : "))
            transfer_ac = bank.find_user(transfer_ac_number)
            if transfer_ac:
                amount = int(input('Enter Transfer Amount : '))
                user.transfer_money(transfer_ac,amount,bank)
            else:
                print('Account does not exist')
        elif op == 6:
            amount = int(input("Enter Loan Amount : "))
            user.take_loan(bank,amount)
        elif op == 7:
            break
        else:
            print("\nInvalid Choice!!\n")


def Admin_menu(admin):
    
    while True:
        print("\nOption : ")
        print('1. Create Account')
        print('2. Delete Account')
        print('3. Check All Users')
        print('4. Check Bank Transaction')
        print('5. Check Total Bank Balance')
        print('6. Check Total Loan')
        print('7. Find User')
        print('8. Exit')
        
        op = int(input("Enter Your Choice : "))
        
        if op == 1:
            name = input('Enter User Name : ')
            email = input('Enter Account Email : ')
            address = input('Enter User Address : ')
            ac_type = input('Enter Account Type(saving/current) : ')
            user = User(name,email,address,ac_type)
            admin.create_account(bank,user)
        elif op == 2:
            ac_number = int(input('Enter Account Number : '))
            admin.delete_account(bank,ac_number)
        elif op == 3:
            admin.check_all_users(bank)
        elif op == 4:
            admin.check_bank_transaction_history(bank)
        elif op == 5:
            admin.check_total_bank_balance(bank)
        elif op == 6:
            admin.total_loan(bank)
        elif op == 7:
            ac_number = int(input('Enter Account Number : '))
            admin.find_user(bank,ac_number)
        elif op == 8:
            break
        else:
            print("\nInvalid Choice!!\n")
            
            
while True:
    print("\n<---------Welcome to Bank Management System--------->")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    
    op = int(input("Enter your choice : "))
    
    if op == 1:
        email = input('Enter Your Email : ')     
        ac_number = int(input('Enter Your Account Number : ')) 
        user = bank.find_user(ac_number)
        if user:
            User_menu(user)  
        else:
            print("\nUser not fount.\n")         
    elif op == 2:
        email = input('Enter Admin Email : ')   # admin email manually set : admin
        password = input('Enter Passward : ')   # admin passward manually set : admin
        for admin_check in admins:
            if admin_check['email'].lower() == email.lower() and admin_check['password'].lower() == password.lower():
                admin = Admin()
                Admin_menu(admin)
            else:
                print('\nAdmin not found')
    elif op == 3:
        print('\n<--------Thank You for visiting this system--------->')
        break
    else:
        print('\nInvalid Choice!!\n')       