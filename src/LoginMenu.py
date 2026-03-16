import customtkinter as ctk
from src.Ui import Ui

class LoginMenu(Ui):
    def __init__(self, master):
        super().__init__()
        self.master = master

    def menu(self):
        self.clear_frame()

        self.master.current_frame = ctk.CTkFrame(self.master, width= 200, height= 150)

        frame = self.master.current_frame

        self.button_test = ctk.CTkButton(frame, text="Youhou")
        
        frame.place(x=300, y=300)
        self.button_test.place(x = 30, y= 50)