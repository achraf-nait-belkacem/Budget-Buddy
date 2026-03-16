import customtkinter as ctk
from src.Ui import Ui

class RegisterMenu(Ui):
    def __init__(self, master):
        super().__init__()
        self.master = master
        
    def menu(self):
        self.master.clear_frame()


        self.master.current_frame = ctk.CTkFrame(self.master, width= 200, height= 250)

        frame = self.master.current_frame

        self.name = ctk.CTkEntry(frame,placeholder_text="Enter your name")
        self.last_name = ctk.CTkEntry(frame, placeholder_text="Enter your last name")
        self.email = ctk.CTkEntry(frame, placeholder_text="Enter your email")
        self.password = ctk.CTkEntry(frame, placeholder_text="Enter your password")
        self.button_post = ctk.CTkButton(frame, text="Register")

        frame.place(x=300, y=300)
        self.name.place(x = 30, y= 20)
        self.last_name.place(x = 30, y = 60)
        self.email.place(x = 30, y=100)
        self.password.place(x = 30, y = 140)
        self.button_post.place(x = 30, y= 210)