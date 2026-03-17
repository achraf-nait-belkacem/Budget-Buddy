from src.DataManagement import DataManagement
import customtkinter as ctk
class Auth:
    def __init__(self):
        self.data = DataManagement()
    
    def submit_register(self, name:ctk.CTkEntry, last_name:ctk.CTkEntry, email:ctk.CTkEntry, password:ctk.CTkEntry):

        user_infos = {"name":name.get(), "last_name":last_name.get(), "email":email.get(), "password":password.get()}

        user_names = [user_infos["name"], user_infos["last_name"]]

        for info in user_infos.values():

            info = info.replace(" ", "")
            if info == "":
                return "error"
        
        if any(c.isalnum() for c in user_names):
            if not user_infos["password"].isalnum():
                if "@" in user_infos["email"]:
                    for k in user_infos["password"]:
                        if k.isupper():
                            break
                        else:
                            return "password_upper_error"
                    if len(user_infos["password"]) < 8:
                        return "password_length_error"
                    
                    else:
                        print("Inscription réussie !")
                        return None
                    
                else:
                    return "email_special_character_error"
            else: 
                return "password_special_char_error"
