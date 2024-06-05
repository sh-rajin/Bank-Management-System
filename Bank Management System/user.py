

class User:
    def __init__(self,name,email,address,ac_type) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.ac_type = ac_type
        self.__balance = 0
        self.__transaction_history = []
        self.loans_taken = 0
        self.total_loan_amount = 0
        
        
    def deposit(self,amount,bank):
        self.__balance += amount
        print(f'\nDeposit {amount} Successful.\n')
        self.__transaction_history.append(f'Deposit : {amount}')
        bank.total_balance += amount
        bank.transaction_history.append(f'Account No. : {bank.find_ac_num(self)} Deposit : {amount}')
        
    def withdraw(self,amount,bank):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'\nWithdraw {amount} Successful.\n')
            self.__transaction_history.append(f'Withdraw : {amount}')
            bank.total_balance -= amount
            bank.transaction_history.append(f'Account No. : {bank.find_ac_num(self)} Withdraw : {amount}')
        else:
            print('\nWithdrawal amount exceeded')
            
    def received_money(self,from_ac_number,amount,bank):   
        self.__balance += amount
        self.__transaction_history.append(f'Received Money : {amount} from Account No.: {from_ac_number} ')
        bank.transaction_history.append(f'Received Account No. : {bank.find_ac_num(self)} Transfer Account No.: {from_ac_number} Received Money : {amount}')
        
    def check_balance(self):
        print(f'\nYour Current balance : {self.__balance}\n')
        
    def check_transaction(self):
        print('\n<--------Transaction History-------->')
        for transaction in self.__transaction_history:
            print(transaction)
        print('\n')
    
    def transfer_money(self, transfer_ac, amount,bank):
        if self.__balance > amount:
            transfer_ac_number = bank.find_ac_num(transfer_ac)
            transfer_ac.received_money(bank.find_ac_num(self),amount,bank)
            self.__balance -= amount
            self.__transaction_history.append(f'Transferred : {amount} to Account No. : {transfer_ac_number}')
            bank.transaction_history.append(f'Transfer Account No. : {bank.find_ac_num(self)} Receive Account No. : {transfer_ac_number} Transferred : {amount}')
            print(f'\nTransfer {amount} successful.\n')
        else:
            print('\nTransfer amount exceeded')
            
            
    def take_loan(self,bank,amount):
        if self.loans_taken >= 2:
            print('\nLoan limit exceeded. Already two or more time take loan\n')
        else:
            if bank.total_balance > self.__balance and bank.total_balance > amount:
                self.__balance += amount
                self.total_loan_amount += amount
                bank.total_loan += amount
                self.__transaction_history.append(f'Take Loan : {amount}')
                bank.transaction_history.append(f'Account No. : {bank.find_ac_num(self)}Take Loan : {amount}')
                self.loans_taken += 1
                print(f'\nThis time loan amount : {amount}')
                print(f'Total loan amount : {self.total_loan_amount}\n')
            else:
                print('No available money of the Bank')
        
    