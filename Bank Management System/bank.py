from random import randint

class Bank:
    def __init__(self,name,branch) -> None:
        self.name = name
        self.branch = branch
        self.total_balance = 0
        self.transaction_history = []
        self.__users = {}
        self.total_loan = 0
        
    def create_account(self,user):
        ac_number = randint(1000000, 9999999)
        self.__users[user] = ac_number
        print(f'\nYour Account create successfully. Your account number : {ac_number}')
    
    def find_user(self,ac_num):
        for user,ac_number in self.__users.items():
            if ac_number == ac_num:
                return user  
        return None
         
    def find_ac_num(self,find_user):
        for user,ac_number in self.__users.items():
            if user == find_user:
                return ac_number  
        return None
    
    def delete_account(self,user): 
        del self.__users[user]
            
    def check_bank_balance(self):
        print(f'\nTotal available bank balance : {self.total_balance}')
    
    def check_bank_transaction(self):
        print('\n<-------Transaction History------->')
        for transaction in self.transaction_history:
            print(f'{transaction}')
                
    def check_all_users(self):
        print('\n <-------Show All Users------>')
        for user,ac_number in self.__users.items():
            if user:
                print(f'\nAccount Name : {user.name}\nAccount Number : {ac_number}\nAccount Type : {user.ac_type}\n')
                print('------------------------')
        print(f'Total Users : {len(self.__users)}\n')
 
    def check_total_loan(self):
        print(f'\nBank Total Loan amount : {self.total_loan}')  
                         
