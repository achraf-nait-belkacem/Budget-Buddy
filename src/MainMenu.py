from src.Ui import Ui
import customtkinter as ctk

class MainMenu:
    def __init__(self, master):
        self.master = master

    def menu(self):
        self.master.clear_frame()

        self.master.current_frame = ctk.CTkFrame(self.master, width= 200, height= 150)

        frame = self.master.current_frame

        self.button_login = ctk.CTkButton(frame, text="login", command=self.master.login_menu.menu)
        self.button_register = ctk.CTkButton(frame, text="register", command=self.master.register_menu.menu) 

        frame.place(relx=0.5, rely=0.5, anchor= ctk.CENTER)
        self.button_login.place(relx = 0.5, y = 50, anchor= ctk.CENTER)
        self.button_register.place(relx = 0.5, y = 100, anchor= ctk.CENTER)