import customtkinter as ctk
from src.Ui import Ui
from src.UserBoardMenu import UserBoardMenu

class LoginMenu:
    def __init__(self, master):
        self.master = master

    def menu(self):
        self.master.clear_frame()

        self.master.current_frame = ctk.CTkFrame(self.master, width= 300, height= 150)

        frame = self.master.current_frame

        self.error_label = ctk.CTkLabel(frame, text="", text_color="red")
        self.email = ctk.CTkEntry(frame, placeholder_text="Enter your email")
        self.password = ctk.CTkEntry(frame, placeholder_text="Enter your password")
        self.btn_submit = ctk.CTkButton(frame, text="Login", command= self.on_login_click)
        self.btn_register = ctk.CTkButton(frame, text="Register", command=self.master.register_menu.menu)
        
        frame.place(relx=0.5, rely=0.5, anchor= ctk.CENTER)
        self.error_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
        self.email.place(relx = 0.5, y=50, anchor=ctk.CENTER)
        self.password.place(relx = 0.5, y = 85, anchor=ctk.CENTER)
        self.btn_submit.place(relx = 0.25, y= 130, anchor= ctk.CENTER)
        self.btn_register.place(relx = 0.75, y= 130, anchor= ctk.CENTER)

    def on_login_click(self):
        resultat = self.master.auth.check_login_errors(self.email, self.password)

        match resultat:
            case "error":
                self.error_label.configure(text="Please enter correct information")
                self.master.current_frame.configure(width= 300)

            case "incorrect_email":
                self.error_label.configure(text="Email not recognised. Please try again")
                self.master.current_frame.configure(width= 350)

            case "incorrect_password":
                self.error_label.configure(text="Password not recognised. Please try again")
                self.master.current_frame.configure(width= 350)

            case "success":
                self.user_board_menu = UserBoardMenu(self.master, self.master.actual_user)
                self.user_board_menu.menu()
                
            case _:
                self.error_label.configure(text="")
                self.master.current_frame.configure(width= 300)