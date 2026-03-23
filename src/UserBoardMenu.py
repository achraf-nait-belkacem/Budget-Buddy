import customtkinter as ctk
from src.Ui import Ui

class UserBoardMenu:
    def __init__(self, master, actual_user):
        self.master = master
        self.categories = [
            "Household & Services", "Home Improvements", "Food & Drinks", 
            "Transport", "Shopping", "Leisure", "Health & Beauty", "Other"
        ]
        self.user = actual_user

    def menu(self):
        self.master.clear_frame()

        self.accounts = self.master.data.get_accounts(self.user["id"])

        self.current_account_index = 0
        self.current_account_label = 1

        self.actual_account = self.accounts[self.current_account_index]

        self.master.current_frame = ctk.CTkFrame(self.master, width= 300, height= 590)
        self.transaction_frame = ctk.CTkFrame(self.master, width=480, height=280)
        self.graphic_frame = ctk.CTkFrame(self.master, width=480, height=280)
        self.transaction_menu_frame = ctk.CTkFrame(self.transaction_frame, width=460, height=220, fg_color="transparent")

        self.btn_withdraw = ctk.CTkButton(self.transaction_frame, text="Withdraw", command=self.on_click_withdraw)
        self.btn_deposit = ctk.CTkButton(self.transaction_frame, text="Deposit", command=self.on_click_deposit)
        self.btn_transaction = ctk.CTkButton(self.transaction_frame, text="Transaction", command=self.on_click_transaction)
        self.btn_quit = ctk.CTkButton(self.transaction_menu_frame, text="Quit", command=self.on_click_quit)

        self.accounts_label = ctk.CTkLabel(self.transaction_frame, text=f"Actual account : {self.current_account_label}")
        self.funds_label = ctk.CTkLabel(self.transaction_frame, text=f"Actual funds : {self.actual_account[2]}")

        self.btn_create_account = ctk.CTkButton(self.transaction_frame, text="Create account", command=self.on_click_create_account)
        self.btn_change_account = ctk.CTkButton(self.transaction_frame, text="Change account", command=self.on_click_change_account)
        
        self.error_label = ctk.CTkLabel(self.transaction_menu_frame, text="", text_color="red")
        self.transaction_label = ctk.CTkLabel(self.transaction_menu_frame, text="")
        self.category_option = ctk.CTkOptionMenu(self.transaction_menu_frame, values=self.categories)
        self.category_option.set("Categories*")
        self.desc = ctk.CTkEntry(self.transaction_menu_frame, placeholder_text="Enter a description")
        self.btn_validate = ctk.CTkButton(self.transaction_menu_frame, text="")
        self.amount_entry = ctk.CTkEntry(self.transaction_menu_frame, placeholder_text="Amount* (ex: 50.00)")

        self.master.current_frame.place(relx=0.195, rely=0.5, anchor= ctk.CENTER)
        self.transaction_frame.place(relx=0.695, rely=0.75, anchor=ctk.CENTER)
        self.graphic_frame.place(relx=0.695, rely=0.245, anchor=ctk.CENTER)
        self.transaction_menu_frame.place(relx=0.5, rely=0.57, anchor=ctk.CENTER)

        self.btn_withdraw.place(relx=0.20, rely= 0.1, anchor=ctk.CENTER)
        self.btn_deposit.place(relx=0.50, rely= 0.1, anchor=ctk.CENTER)
        self.btn_transaction.place(relx=0.80, rely= 0.1, anchor=ctk.CENTER)

        self.accounts_label.place(relx = 0.35,rely = 0.2, anchor = ctk.CENTER)
        self.funds_label.place(relx = 0.65,rely = 0.2, anchor = ctk.CENTER)
        self.btn_change_account.place(relx = 0.65, rely = 0.3, anchor= ctk.CENTER)
        self.btn_create_account.place(relx = 0.35, rely = 0.3, anchor = ctk.CENTER)

    def on_click_withdraw(self):
        self.btn_withdraw.configure(state="disabled")
        self.btn_deposit.configure(state="normal")
        self.btn_transaction.configure(state="normal")

        self.transaction_menu_frame.configure(fg_color="gray20")
        self.btn_quit.place(relx=0.5, rely= 0.9, anchor=ctk.CENTER)
        self.hide_account_menu()

        self.transaction_label.configure(text="Withdraw menu")
        self.transaction_label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
        self.category_option.place(relx=0.6, rely=0.45, anchor=ctk.CENTER)
        self.desc.place(relx= 0.3, rely= 0.3, anchor=ctk.CENTER)
        self.amount_entry.place(relx=0.3, rely=0.6, anchor=ctk.CENTER)
        self.btn_validate.configure(command=self.on_withdraw_validate_click, text="Confirm withdraw")
        self.btn_validate.place(relx=0.3, rely=0.7, anchor=ctk.CENTER)

    def on_click_deposit(self):
        self.btn_deposit.configure(state="disabled")
        self.btn_withdraw.configure(state="normal")
        self.btn_transaction.configure(state="normal")

        self.transaction_menu_frame.configure(fg_color="gray20")
        self.btn_quit.place(relx=0.5, rely= 0.9, anchor=ctk.CENTER)
        self.hide_account_menu()

        self.transaction_label.configure(text="Deposit menu")
        self.transaction_label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
        self.category_option.place(relx=0.6, rely=0.45, anchor=ctk.CENTER)
        self.desc.place(relx= 0.3, rely= 0.3, anchor=ctk.CENTER)
        self.amount_entry.place(relx=0.3, rely=0.6, anchor=ctk.CENTER)
        self.btn_validate.configure(command=self.on_deposit_validate_click, text="Confirm deposit")
        self.btn_validate.place(relx=0.3, rely=0.7, anchor=ctk.CENTER)
        

    def on_click_transaction(self):
        self.btn_transaction.configure(state="disabled")
        self.btn_withdraw.configure(state="normal")
        self.btn_deposit.configure(state="normal")

        self.transaction_menu_frame.configure(fg_color="gray20")
        self.btn_quit.place(relx=0.5, rely= 0.9, anchor=ctk.CENTER)
        self.hide_account_menu()

    def on_click_quit(self):
        self.btn_transaction.configure(state="normal")
        self.btn_withdraw.configure(state="normal")
        self.btn_deposit.configure(state="normal")

        self.transaction_menu_frame.configure(fg_color="transparent")
        self.btn_quit.place_forget()
        
        self.accounts_label.place(relx = 0.35, rely = 0.2, anchor = ctk.CENTER)
        self.funds_label.place(relx= 0.65, rely= 0.2, anchor=ctk.CENTER)
        self.btn_create_account.place(relx = 0.35, rely = 0.3, anchor = ctk.CENTER)
        self.btn_change_account.place(relx = 0.65, rely = 0.3, anchor= ctk.CENTER)

        self.transaction_label.place_forget()
        self.category_option.place_forget()
        self.desc.place_forget()
        self.amount_entry.place_forget()
        self.btn_validate.place_forget()
    
    def on_click_change_account(self):
        self.current_account_index += 1
        self.current_account_label += 1

        if self.current_account_index >= len(self.accounts):
            self.current_account_label = 1
            self.current_account_index = 0

        self.actual_account = self.accounts[self.current_account_index]
        self.accounts_label.configure(text=f"Actual account : {self.current_account_label}")
        self.funds_label.configure(text=f"Actual funds : {self.actual_account[2]}")
        
        

    def on_click_create_account(self):
        check = self.master.data.create_account(self.user["id"])
        if check:
            account_created_label_error = ctk.CTkLabel(self.transaction_frame, text="You have the maximum amount of account", text_color="red")
            account_created_label_error.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
            account_created_label_error.after(3000, account_created_label_error.place_forget)
        else: 
            account_created_label = ctk.CTkLabel(self.transaction_frame, text="Account created with success !", text_color="green")
            account_created_label.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
            account_created_label.after(3000, account_created_label.place_forget)
            self.accounts = self.master.data.get_accounts(self.user["id"])

    def hide_account_menu(self):
        self.accounts_label.place_forget()
        self.funds_label.place_forget()
        self.btn_create_account.place_forget()
        self.btn_change_account.place_forget()

    def on_withdraw_validate_click(self):
        result = self.master.transaction.check_withdraw(self.desc.get(), self.amount_entry.get(), self.category_option.get(), "withdraw", self.actual_account)
        self.error_label.place(relx = 0.5, rely = 0.1, anchor= ctk.CENTER)

        match result:
            case "missing_fields":
                self.error_label.configure(text_color = "red", text="There is missing fields. Please try again.")
                self.error_label.after(3000, self.error_label.place_forget)

            case "invalid_amount":
                self.error_label.configure(text_color = "red", text="The amount you entered is invalid. Please try again")
                self.error_label.after(3000, self.error_label.place_forget)
            
            case "not_enough_money":
                self.error_label.configure(text_color = "red", text="Your account doesn't have enough money.")
                self.error_label.after(3000, self.error_label.place_forget)

            case "success":
                self.accounts = self.master.data.get_accounts(self.user["id"])
                self.actual_account = self.accounts[self.current_account_index]
                self.funds_label.configure(text=f"Actual funds : {self.actual_account[2]}")
                self.error_label.configure(text_color = "green", text = "Your withdraw has been completed !")
                self.error_label.after(3000, self.error_label.place_forget)

            case _:
                self.error_label.configure(text_color = "red", text="")
                self.master.current_frame.configure(width= 300)

    def on_deposit_validate_click(self):
        result = self.master.transaction.check_deposit(self.desc.get(), self.amount_entry.get(), self.category_option.get(), "deposit", self.actual_account)
        self.error_label.place(relx = 0.5, rely = 0.1, anchor= ctk.CENTER)

        match result:
            case "missing_fields":
                self.error_label.configure(text_color = "red", text="There is missing fields. Please try again.")
                self.error_label.after(3000, self.error_label.place_forget)

            case "invalid_amount":
                self.error_label.configure(text_color = "red", text="The amount you entered is invalid. Please try again")
                self.error_label.after(3000, self.error_label.place_forget)

            case "success":
                self.accounts = self.master.data.get_accounts(self.user["id"])
                self.actual_account = self.accounts[self.current_account_index]
                self.funds_label.configure(text=f"Actual funds : {self.actual_account[2]}")
                self.error_label.configure(text_color = "green", text = "Your deposit has been completed !")
                self.error_label.after(3000, self.error_label.place_forget)

            case _:
                self.error_label.configure(text_color = "red", text="")
                self.master.current_frame.configure(width= 300)

