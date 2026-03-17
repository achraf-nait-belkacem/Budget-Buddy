import customtkinter as ctk
from src.Ui import Ui

class LoginMenu(Ui):
    def __init__(self, master):
        super().__init__()
        self.master = master

    def menu(self):
        self.master.clear_frame()

        self.master.current_frame = ctk.CTkFrame(self.master, width= 300, height= 150)

        frame = self.master.current_frame

        self.btn_submit = ctk.CTkButton(frame, text="Login")
        self.btn_register = ctk.CTkButton(frame, text="Register", command=self.master.register_menu.menu)
        
        frame.place(relx=0.5, rely=0.5, anchor= ctk.CENTER)
        self.btn_submit.place(relx = 0.25, y= 130, anchor= ctk.CENTER)
        self.btn_register.place(relx = 0.75, y= 130, anchor= ctk.CENTER)