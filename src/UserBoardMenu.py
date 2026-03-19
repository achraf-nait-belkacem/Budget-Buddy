import customtkinter as ctk
from src.Ui import Ui

class UserBoardMenu(Ui):
    def __init__(self, master, actual_user):
        super().__init__()
        self.master = master
        self.user = actual_user

    def menu(self):
        self.master.clear_frame()

        self.accounts = self.master.data.get_accounts(self.user["id"])

        self.current_account_index = 0
        self.current_account_label = 1

        self.actual_account = self.accounts[self.current_account_index][0]

        self.master.current_frame = ctk.CTkFrame(self.master, width= 300, height= 590)
        self.transaction_frame = ctk.CTkFrame(self.master, width=480, height=280)
        self.graphic_frame = ctk.CTkFrame(self.master, width=480, height=280)
        self.transaction_menu_frame = ctk.CTkFrame(self.transaction_frame, width=460, height=220, fg_color="transparent")

        self.btn_withdraw = ctk.CTkButton(self.transaction_frame, text="Withdraw", command=self.on_click_withdraw)
        self.btn_deposit = ctk.CTkButton(self.transaction_frame, text="Deposit", command=self.on_click_deposit)
        self.btn_transaction = ctk.CTkButton(self.transaction_frame, text="Transaction", command=self.on_click_transaction)
        self.btn_quit = ctk.CTkButton(self.transaction_menu_frame, text="Quit", command=self.on_click_quit)

        self.accounts_label = ctk.CTkLabel(self.transaction_frame, text=f"Actual account : {self.current_account_label}")

        self.btn_create_account = ctk.CTkButton(self.transaction_frame, text="Create account", command=self.on_click_create_account)
        self.btn_change_account = ctk.CTkButton(self.transaction_frame, text="Change account", command=self.on_click_change_account)

        


        self.master.current_frame.place(relx=0.195, rely=0.5, anchor= ctk.CENTER)
        self.transaction_frame.place(relx=0.695, rely=0.75, anchor=ctk.CENTER)
        self.graphic_frame.place(relx=0.695, rely=0.245, anchor=ctk.CENTER)
        self.transaction_menu_frame.place(relx=0.5, rely=0.57, anchor=ctk.CENTER)

        self.btn_withdraw.place(relx=0.20, rely= 0.1, anchor=ctk.CENTER)
        self.btn_deposit.place(relx=0.50, rely= 0.1, anchor=ctk.CENTER)
        self.btn_transaction.place(relx=0.80, rely= 0.1, anchor=ctk.CENTER)

        self.accounts_label.place(relx = 0.5,rely = 0.2, anchor = ctk.CENTER)
        self.btn_change_account.place(relx = 0.65, rely = 0.3, anchor= ctk.CENTER)
        self.btn_create_account.place(relx = 0.35, rely = 0.3, anchor = ctk.CENTER)

    def on_click_withdraw(self):
        self.btn_withdraw.configure(state="disabled")
        self.btn_deposit.configure(state="normal")
        self.btn_transaction.configure(state="normal")

        self.transaction_menu_frame.configure(fg_color="gray20")
        self.btn_quit.place(relx=0.5, rely= 0.9, anchor=ctk.CENTER)
        self.hide_account_menu()

    def on_click_deposit(self):
        self.btn_deposit.configure(state="disabled")
        self.btn_withdraw.configure(state="normal")
        self.btn_transaction.configure(state="normal")

        self.transaction_menu_frame.configure(fg_color="gray20")
        self.btn_quit.place(relx=0.5, rely= 0.9, anchor=ctk.CENTER)
        self.hide_account_menu()

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
        
        self.accounts_label.place(relx = 0.5, rely = 0.2, anchor = ctk.CENTER)
        self.btn_create_account.place(relx = 0.35, rely = 0.3, anchor = ctk.CENTER)
        self.btn_change_account.place(relx = 0.65, rely = 0.3, anchor= ctk.CENTER)
    
    def on_click_change_account(self):
        self.current_account_index += 1
        self.current_account_label += 1

        if self.current_account_index >= len(self.accounts):
            self.current_account_label = 1
            self.current_account_index = 0
        self.accounts_label.configure(text=f"Actual account : {self.current_account_label}")
        self.actual_account = self.accounts[self.current_account_index][0]
        

    def on_click_create_account(self):
        check = self.master.data.create_account(self.user["id"])
        if check:
            account_created_label_error = ctk.CTkLabel(self.master.current_frame, text="You have the maximum amount of account", text_color="red")
            account_created_label_error.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)
            account_created_label_error.after(3000, account_created_label_error.place_forget)
        else: 
            account_created_label = ctk.CTkLabel(self.master.current_frame, text="Account created with success !", text_color="green")
            account_created_label.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)
            account_created_label.after(3000, account_created_label.place_forget)
            self.accounts = self.master.data.get_accounts(self.user["id"])

    def hide_account_menu(self):
        self.accounts_label.place_forget()
        self.btn_create_account.place_forget()
        self.btn_change_account.place_forget()