# UserDAO.py

from dataclasses import dataclass
import sqlite3

from User import User


@dataclass
class UserDAO:
    conn: sqlite3.Connection
    file_name: str = "./users.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.file_name)
        pass
    
    def get_all(self):
        
        cur = self.conn.cursor()
        sql = "SELECT * FROM users"
        res = cur.execute(sql)
        users = []
        for user in res:
            users.append(User(user[0], user[1], user[2], user[3]))
        
        cur.close()
        return users

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    dao = UserDAO()

    users = dao.get_all()

    for user in users:
        print (user)

    dao.close()
    #print (users)

