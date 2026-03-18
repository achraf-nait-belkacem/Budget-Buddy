import mysql.connector
import bcrypt

class DataManagement:
    def __init__(self, master):
        self.db = mysql.connector.connect(
                                            host = "localhost",
                                            user = "root",
                                            password = "Metallica13!",
                                            database = "budget_buddy",
                                            port = 3308
                                        )
        self.salt = bcrypt.gensalt()
        self.master = master
    def submit_register(self, user_data:dict):
        bytes = user_data["password"].encode("UTF-8")
        hash = bcrypt.hashpw(bytes, self.salt)
        user_data["password"] = hash

        submit_register_cursor = self.db.cursor()
        create_user = "INSERT INTO user(name, last_name, email, password) VALUES(%(name)s, %(last_name)s, %(email)s, %(password)s)"
        submit_register_cursor.execute(create_user, user_data)

        self.db.commit()
        submit_register_cursor.close()
        
        user_db_infos = self.return_infos(user_data["email"])
        self.master.actual_user = {"id": user_db_infos[0], "name": user_db_infos[1], "last_name": user_db_infos[2], "email": user_db_infos[3]}
        

    def return_infos(self, user_email):
        fetch_infos_cursor = self.db.cursor(buffered=True)
        fetch_infos = "SELECT id, name, last_name, email FROM user WHERE email = %(email)s"
        fetch_infos_cursor.execute(fetch_infos, {"email": user_email})

        user_db_infos = fetch_infos_cursor.fetchone()
        fetch_infos_cursor.close()
        return user_db_infos

    def submit_login(self, user_data:dict):
        submit_login_cursor = self.db.cursor(buffered=True)
        password_request = "SELECT password FROM user WHERE email = %(email)s"
        email = user_data["email"]
        submit_login_cursor.execute(password_request, {"email": email})

        password = submit_login_cursor.fetchone()

        hached_password = password[0]
        submit_login_cursor.close()
        bytes = user_data["password"].encode("UTF-8")
        hached_password_bytes = hached_password.encode("UTF-8")

        if bcrypt.checkpw(bytes, hached_password_bytes):
            user_db_infos = self.return_infos(user_data["email"])
            self.master.actual_user = {"id": user_db_infos[0], "name": user_db_infos[1], "last_name": user_db_infos[2], "email": user_db_infos[3]}
            return True
        else:
            return False
        
    def check_email(self, user_email):
        check_email_cursor = self.db.cursor(buffered=True)
        email_request = "SELECT email FROM user WHERE email = %(email)s"
        check_email_cursor.execute(email_request, {"email": user_email})

        email = check_email_cursor.fetchone()

        check_email_cursor.close()
        if email is None:
            return False
        else:
            return True