import customtkinter as ctk
from src.Ui import Ui
from src.Auth import Auth

class UserBoardMenu(Ui):
    def __init__(self, master, actual_user:dict):
        super().__init__()
        self.master = master
        self.actual_user = actual_user

    def menu(self):
        self.master.clear_frame()

        self.current_frame = ctk.CTkFrame(self, width= 200, height= 150)

        self.current_frame.place(relx=0.5, rely=0.5, anchor= ctk.CENTER)