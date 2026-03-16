import mysql.connector

class DataManagement:
    def __init__(self):
        self.db = mysql.connector.connect(
                                            host = "localhost",
                                            user = "root",
                                            password = "Metallica13!",
                                            database = "budget_buddy",
                                            port = 3308
                                        )
        