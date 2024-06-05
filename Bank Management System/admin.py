
class Admin:
    def __init__(self) -> None:
        pass
    
    def create_account(self,bank,user):
        if user.ac_type.lower() == 'saving' or user.ac_type.lower() == 'current': 
            bank.create_account(user)
        else:
            print('\nInvalid Account Type.')
            
    def delete_account(self,bank,ac_number):
        user = bank.find_user(ac_number)
        if user:
            bank.delete_account(user)
            print('\nAccount deleted successfully.')
        else:
            print('\nAccount not found.')
            
    def check_all_users(self,bank):
        bank.check_all_users()
        
    def check_total_bank_balance(self,bank):
        bank.check_bank_balance()
        
    def check_bank_transaction_history(self,bank):
        bank.check_bank_transaction()
        
    def total_loan(self,bank):
        bank.check_total_loan()
   
    def find_user(self,bank,ac_number):
        user = bank.find_user(ac_number)
        if user:
            print(f'\nAccount Name : {user.name}\nAccount Number : {ac_number}\nAccount Type : {user.ac_type}\n')
            print('------------------------')
        else:
            print('\nUser not found.')