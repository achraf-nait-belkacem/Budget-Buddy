import customtkinter as ctk
from src.Ui import Ui
from src.Auth import Auth

class RegisterMenu(Ui):
    def __init__(self, master):
        super().__init__()
        self.auth = Auth()
        self.master = master
        
    def menu(self):
        self.master.clear_frame()


        self.master.current_frame = ctk.CTkFrame(self.master, width= 250, height= 250)

        frame = self.master.current_frame

        

        self.name = ctk.CTkEntry(frame,placeholder_text="Enter your name")
        self.last_name = ctk.CTkEntry(frame, placeholder_text="Enter your last name")
        self.email = ctk.CTkEntry(frame, placeholder_text="Enter your email")
        self.password = ctk.CTkEntry(frame, placeholder_text="Enter your password")

        self.error_label = ctk.CTkLabel(frame, text="", text_color="red")

        self.button_post = ctk.CTkButton(frame, text="Register", command= self.on_register_click)

        frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.error_label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
        self.name.place(relx = 0.5, y= 60, anchor=ctk.CENTER)
        self.last_name.place(relx = 0.5, y = 100, anchor=ctk.CENTER)
        self.email.place(relx = 0.5, y=140, anchor=ctk.CENTER)
        self.password.place(relx = 0.5, y = 180, anchor=ctk.CENTER)
        self.button_post.place(relx = 0.5, y= 230, anchor=ctk.CENTER)

    def on_register_click(self):
        resultat = self.auth.submit_register(self.name, self.last_name, self.email, self.password)

        match resultat:
            case "error":
                self.error_label.configure(text="Please enter correct information")
                self.master.current_frame.configure(width= 300)
            
            case "email_special_character_error":

                self.error_label.configure(text="Please enter a correct email")
                self.master.current_frame.configure(width= 300)

            case "password_special_char_error":
                self.error_label.configure(text="Enter at least one special character in the password")
                self.master.current_frame.configure(width= 350)

            case "password_upper_error":
                self.error_label.configure(text="Enter at least one upper character in the password")
                self.master.current_frame.configure(width= 350)

            case "password_length_error":
                self.error_label.configure(text="Enter at least a password with 8 or more characters")
                self.master.current_frame.configure(width= 350)
            case _:
                self.error_label.configure(text="")
                self.master.current_frame.configure(width= 250)