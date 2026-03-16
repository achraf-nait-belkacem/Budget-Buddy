import customtkinter as ctk

class Ui(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("800x600")
        self.title("Budget Buddy")
        self.current_frame = None

    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.current_frame = None

    def menu(self):
        pass