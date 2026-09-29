import sqlite3
import os

class UserDatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        """Creates the users table if it does not already exist."""
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            address TEXT,
            mobile TEXT,
            email TEXT
        );
        """
        with self.conn:
            self.conn.execute(query)

    def find_user(self, username):
        """Queries the database for given username using a parameterized query."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, username, address, mobile, email FROM users WHERE username = ?",
            (username,)
        )
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "username": row[1],
                "address": row[2],
                "mobile": row[3],
                "email": row[4]
            }
        return None

    def add_or_update_user(self, username, address, mobile, email):
        """Inserts a new user or updates an existing user record."""
        existing_user = self.find_user(username)
        cursor = self.conn.cursor()
        
        if existing_user:
            cursor.execute(
                "UPDATE users SET address = ?, mobile = ?, email = ? WHERE username = ?",
                (address, mobile, email, username)
            )
            self.conn.commit()
            return "UPDATED"
        else:
            cursor.execute(
                "INSERT INTO users (username, address, mobile, email) VALUES (?, ?, ?, ?)",
                (username, address, mobile, email)
            )
            self.conn.commit()
            return "INSERTED"

    def list_all_users(self):
        """Returns all registered users ordered alphabetically by username."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, username, address, mobile, email FROM users ORDER BY username ASC")
        rows = cursor.fetchall()
        return [
            {
                "id": row[0],
                "username": row[1],
                "address": row[2],
                "mobile": row[3],
                "email": row[4]
            }
            for row in rows
        ]

    def close(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()


# Example Walkthrough
if __name__ == "__main__":
    db_file = os.path.join(os.path.dirname(__file__), "company.db")
    if os.path.exists(db_file):
        os.remove(db_file)

    db = UserDatabaseManager(db_file)

    # Insert new user
    status1 = db.add_or_update_user("arham_k", "Pune, MH", "9876543210", "arham@cdac.in")
    print(status1)  # Output: INSERTED

    # Search user
    user_info = db.find_user("arham_k")
    print(user_info["email"])  # Output: arham@cdac.in

    # Update existing user
    status2 = db.add_or_update_user("arham_k", "Bengaluru, KA", "9876543210", "arham@cdac.in")
    print(status2)  # Output: UPDATED

    db.close()
