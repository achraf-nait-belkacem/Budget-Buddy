from src.DataManagement import DataManagement
import customtkinter as ctk
class Auth:
    def __init__(self, master):
        self.master = master
    
    def check_register_errors(self, name:ctk.CTkEntry, last_name:ctk.CTkEntry, email:ctk.CTkEntry, password:ctk.CTkEntry):

        user_infos = {"name":name.get(), "last_name":last_name.get(), "email":email.get(), "password":password.get()}
        user_names = [user_infos["name"], user_infos["last_name"]]

        for info in user_infos.values():

            info = info.replace(" ", "")
            if info == "":
                return "error"
        
        if any(c.isalnum() for c in user_names):
            if not user_infos["password"].isalnum():
                if "@" in user_infos["email"]:
                    if any(k.isupper() for k in user_infos["password"]):
                        if len(user_infos["password"]) > 8:
                            if any(char.isdigit() for char in user_infos["password"]):
                                self.master.data.submit_register(user_infos)
                                return "success"
                            else:
                                return "pasword_num_error"
                        else:
                            return "password_length_error"
                    else:
                            return "password_upper_error"
                else:
                    return "email_special_character_error"
            else: 
                return "password_special_char_error"
            
    def check_login_errors(self, email:ctk.CTkEntry, password:ctk.CTkEntry):
        user_infos = {"email":email.get(), "password":password.get()}

        for info in user_infos.values():

            info = info.replace(" ", "")
            if info == "":
                return "error"
            
        if self.master.data.check_email(user_infos["email"]) is True:
            if self.master.data.submit_login(user_infos):
                return "success"
            else:
                return "incorrect_password"
        else:
            return "incorrect_email"
