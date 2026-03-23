import mysql.connector
import bcrypt
import os
from dotenv import load_dotenv

class DataManagement:
    def __init__(self, master):
        load_dotenv()

        self.db = mysql.connector.connect(
                                            host = os.getenv("DB_HOST", "localhost"),
                                            user = os.getenv("DB_USER"),
                                            password = os.getenv("DB_PASSWORD"),
                                            database = os.getenv("DB_NAME"),
                                            port = int(os.getenv("DB_PORT", "3306"))
                                        )
        self.master = master

    def create_user(self, user_data: dict):
        """
        Creates a user row from raw user_data coming from the UI/auth layer.
        Hashes the password using a fresh bcrypt salt per registration.
        """
        bytes = user_data["password"].encode("UTF-8")
        password_hash = bcrypt.hashpw(bytes, bcrypt.gensalt())
        user_data["password"] = password_hash

        create_user_cursor = self.db.cursor()
        create_user = (
            "INSERT INTO user(name, last_name, email, password) "
            "VALUES(%(name)s, %(last_name)s, %(email)s, %(password)s)"
        )
        create_user_cursor.execute(create_user, user_data)
        self.db.commit()
        create_user_cursor.close()

    def submit_register(self, user_data:dict):
        self.create_user(user_data)
        self.apply_current_user(user_data)
        self.create_account(self.master.actual_user["id"])
        

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
            self.apply_current_user(user_data)
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
    
    def check_max_account(self, id):
        check_max_account_cursor = self.db.cursor(buffered=True)
        request = "SELECT COUNT(*) FROM account WHERE user_id = %(id)s"
        check_max_account_cursor.execute(request, {"id": id})
        fetch = check_max_account_cursor.fetchone()
        check_max_account_cursor.close()

        number_of_accounts = fetch[0]

        if number_of_accounts >= 3:
            return True
        else:
            return False

    def create_account(self, id):
        if self.check_max_account(id):
            return True
        else : 
            create_account_cursor = self.db.cursor(buffered=True)
            request = "INSERT INTO account(user_id, funds) VALUES(%(id)s, 0)"
            create_account_cursor.execute(request, {"id": id})
            self.db.commit()
            create_account_cursor.close()

    def apply_current_user(self, user_data):
        user_db_infos = self.return_infos(user_data["email"])
        self.master.actual_user = {"id": user_db_infos[0], "name": user_db_infos[1], "last_name": user_db_infos[2], "email": user_db_infos[3]}

    def get_accounts(self, user_id):
        get_accounts_cursor = self.db.cursor()
        request = "SELECT * FROM account WHERE user_id = %(user_id)s ORDER BY id ASC"
        get_accounts_cursor.execute(request, {"user_id": user_id})

        accounts_list = get_accounts_cursor.fetchall()
        get_accounts_cursor.close()
        return accounts_list

    def update_account_funds(self, account_id, new_balance):
        update_account_cursor = self.db.cursor()
        request = "UPDATE account SET funds = %(new_balance)s WHERE id = %(account_id)s"

        update_account_cursor.execute(request, {"new_balance" : new_balance, "account_id": account_id})
        self.db.commit()
        update_account_cursor.close()

    def create_transaction(self, transaction_data):
        create_transaction_cursor = self.db.cursor()
        request = "INSERT INTO transaction (description, amount, date, type, category, account_id) VALUES (%(description)s, %(amount)s, %(date)s, %(type)s, %(category)s, %(account_id)s)"

        create_transaction_cursor.execute(request, transaction_data)
        self.db.commit()
        create_transaction_cursor.close()

    def get_transactions(self, account_id: int):
        """
        Returns transaction rows for a given account, newest first.
        Each row is:
        (id, date, type, category, amount, description)
        """
        cursor = self.db.cursor(buffered=True)
        request = """
            SELECT id, date, type, category, amount, description
            FROM transaction
            WHERE account_id = %(account_id)s
            ORDER BY date DESC, id DESC
        """
        cursor.execute(request, {"account_id": account_id})
        rows = cursor.fetchall()
        cursor.close()
        return rows
