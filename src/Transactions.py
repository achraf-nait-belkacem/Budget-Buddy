from datetime import date

class Transactions():
    def __init__(self, master):
        self.master = master

    def check_withdraw(self, desc, amount, category, type, account):
        if amount.strip() == "" or category == "Categories*":
            return "missing_fields"

        try:
            amount_float = float(amount)
            if amount_float <= 0:
                return "invalid_amount"
        except ValueError:
            return "invalid_amount"

        if account[2] - amount_float < 0:
            return "not_enough_money"

        if desc.strip() == "":
            desc = None

        transaction_date = date.today().strftime('%Y-%m-%d')

        transaction_data = {
            "description": desc, 
            "amount": amount_float, 
            "date": transaction_date, 
            "type": type, 
            "category": category, 
            "account_id": account[0]
        }


        new_balance = account[2] - amount_float
        self.master.data.update_account_funds(account[0], new_balance)
        self.master.data.create_transaction(transaction_data)
        
        return "success"
    
    def check_deposit(self, desc, amount, category, trans_type, account):
        if amount.strip() == "" or category == "Categories*":
            return "missing_fields"

        try:
            amount_float = float(amount)
            if amount_float <= 0:
                return "invalid_amount"
        except ValueError:
            return "invalid_amount"

        if desc.strip() == "":
            desc = None

        transaction_date = date.today().strftime('%Y-%m-%d')

        transaction_data = {
            "description": desc, 
            "amount": amount_float, 
            "date": transaction_date, 
            "type": trans_type, 
            "category": category, 
            "account_id": account[0]
        }


        new_balance = account[2] + amount_float
        self.master.data.update_account_funds(account[0], new_balance)
        self.master.data.create_transaction(transaction_data)
        
        return "success"