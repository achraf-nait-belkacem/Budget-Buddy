from datetime import date

class Transactions():
    def __init__(self, master):
        self.master = master

    def check_withdraw(self, desc, amount, category, trans_type, account):
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
            "type": trans_type, 
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
    
    def check_transfer(self, desc, amount, category, trans_type, current_account, trans_from, trans_to, accounts):
        if amount.strip() == "" or category == "Categories*" or trans_from == "Select an account" or trans_to == "Select an account" :
            return "missing_fields"
        
        if trans_from == trans_to:
            return "same_account"

        try:
            amount_float = float(amount)
            if amount_float <= 0:
                return "invalid_amount"
        except ValueError:
            return "invalid_amount"

        if desc.strip() == "":
            desc = f"{trans_from} transfered {amount} to {trans_to}."

        if trans_from == "first account":
            trans_from = accounts[0]
        elif trans_from == "second account":
            trans_from = accounts[1]
        else:
            trans_from = accounts[2]

        if trans_from[2] - amount_float < 0:
            return "not_enough_money"
        
        if trans_to == "first account":
            trans_to = accounts[0]
        elif trans_to == "second account":
            trans_to = accounts[1]
        else:
            trans_to = accounts[2]

        transaction_date = date.today().strftime('%Y-%m-%d')

        transaction_data_from = {
            "description": desc, 
            "amount": amount_float, 
            "date": transaction_date, 
            "type": trans_type, 
            "category": category, 
            "account_id": trans_from[0]
        }

        transaction_data_to = {
            "description": desc,
            "amount": amount_float,
            "date": transaction_date,
            "type": trans_type, 
            "category": category, 
            "account_id": trans_to[0]
        }

        new_balance_from = trans_from[2] - amount_float
        new_balance_to = trans_to[2] + amount_float

        self.master.data.update_account_funds(trans_from[0], new_balance_from)
        self.master.data.update_account_funds(trans_to[0], new_balance_to)

        self.master.data.create_transaction(transaction_data_from)
        self.master.data.create_transaction(transaction_data_to)

        return "success"

