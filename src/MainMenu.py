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

        self.button_login.place(x = 30, y = 40)
        self.button_register.place(x = 30, y = 80)
        self.current_frame.place(x=300, y=300)

