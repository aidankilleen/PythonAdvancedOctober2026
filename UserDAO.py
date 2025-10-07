# UserDAO.py

from dataclasses import dataclass
import sqlite3

from User import User


@dataclass
class UserDAO:
    conn: sqlite3.Connection
    file_name: str 

    def __init__(self, file_name = "./users.db"):
        self.file_name = file_name
        self.conn = sqlite3.connect(self.file_name)
        pass
    
    def get_all(self):
        cur = self.conn.cursor()
        sql = "SELECT * FROM users"
        res = cur.execute(sql)
        users = []
        for user in res:
            id, name, email, active = user
            users.append(User(id, name, email, active))
        
        cur.close()
        return users

    def add(self, user):

        sql = f"""INSERT INTO users 
                (name, email, active) 
                VALUES(?,?,?)"""

        params = (user.name, user.email, 1 if user.active else 0)

        cur = self.conn.cursor()
        cur.execute(sql, params)
        user.id = cur.lastrowid
        cur.close()
        self.conn.commit()
        return user
    
    def delete(self, id):
        sql = "DELETE FROM users WHERE id=?"
        params = (id,) # create a tuple with a single item
        self.conn.execute(sql, params)
        self.conn.commit()
        

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    dao = UserDAO("./users.db")

    new_user = User(-1, "New User", "new.user@gmail.com", True)
    added_user = dao.add(new_user)

    print (added_user) # id should not be -1

    users = dao.get_all()

    for user in users:
        print (user)

    dao.close()
    #print (users)

