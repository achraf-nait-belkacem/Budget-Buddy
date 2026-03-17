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
        
        frame.place(relx=0.5, rely=0.5, anchor= ctk.CENTER)
        self.button_test.place(relx = 0.5, y= 50, anchor= ctk.CENTER)