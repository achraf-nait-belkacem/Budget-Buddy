import customtkinter as ctk
from src.Ui import Ui
from src.LoginMenu import LoginMenu
from src.RegisterMenu import RegisterMenu

class MainMenu(Ui):
    def __init__(self):
        super().__init__()
        self.login_menu = LoginMenu(master=self)
        self.register_menu = RegisterMenu(master=self)
        
        self.menu()

    def menu(self):
        self.clear_frame()

        self.current_frame = ctk.CTkFrame(self, width= 200, height= 150)
        self.button_login = ctk.CTkButton(self.current_frame, text="login", command=self.login_menu.menu)
        self.button_register = ctk.CTkButton(self.current_frame, text="register", command=self.register_menu.menu) 

        self.current_frame.place(relx=0.5, rely=0.5, anchor= ctk.CENTER)
        self.button_login.place(relx = 0.5, y = 50, anchor= ctk.CENTER)
        self.button_register.place(relx = 0.5, y = 100, anchor= ctk.CENTER)
        

