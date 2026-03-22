import customtkinter as ctk
from src.Ui import Ui
from src.LoginMenu import LoginMenu
from src.RegisterMenu import RegisterMenu
from src.Auth import Auth
from src.DataManagement import DataManagement
from src.MainMenu import MainMenu
from src.Transactions import Transactions
class App:
    def __init__(self):
        self.window = Ui()
        
        self.window.auth = Auth(self.window) 
        self.window.transaction = Transactions(self.window)
        self.data = DataManagement(self.window)
        self.actual_user = {}
        
        self.window.data = self.data
        self.window.actual_user = self.actual_user
        
        self.window.main_menu = MainMenu(self.window)
        self.window.login_menu = LoginMenu(self.window)
        self.window.register_menu = RegisterMenu(self.window)
        self.window.main_menu.menu()

    def run(self):
        self.window.mainloop()
        

