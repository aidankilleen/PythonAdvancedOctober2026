# UserDAO.py
# UserDAO.py

from dataclasses import dataclass
import sqlite3
from contextlib import closing
from typing import Iterable, Optional, List, cast

from User import User


@dataclass
class UserDAO:
    conn: sqlite3.Connection
    file_name: str

    def __init__(self, file_name: str = "./users.db"):
        self.file_name = file_name
        self.conn = sqlite3.connect(self.file_name)
        self.conn.row_factory = sqlite3.Row            # dict-like rows
        self.conn.execute("PRAGMA foreign_keys = ON")  # safe default

    # ---------- helpers ----------
    def _row_to_user(self, row: sqlite3.Row) -> User:
        """Map a DB row to a User."""
        try:
            return User(
                id=row["id"],
                name=row["name"],
                email=row["email"],
                active=bool(row["active"]),
            )
        except (KeyError, TypeError, IndexError):
            return User(row[0], row[1], row[2], bool(row[3]))

    # ---------- reads ----------
    def get_all(self) -> List[User]:
        sql = "SELECT id, name, email, active FROM users ORDER BY id"
        with closing(self.conn.execute(sql)) as cur:
            return [self._row_to_user(r) for r in cur.fetchall()]

    def get_by_id(self, user_id: int) -> Optional[User]:
        sql = "SELECT id, name, email, active FROM users WHERE id = ?"
        with closing(self.conn.execute(sql, (user_id,))) as cur:
            row = cur.fetchone()
            return self._row_to_user(row) if row else None

    def get_by_email(self, email: str) -> Optional[User]:
        sql = "SELECT id, name, email, active FROM users WHERE email = ?"
        with closing(self.conn.execute(sql, (email,))) as cur:
            row = cur.fetchone()
            return self._row_to_user(row) if row else None

    def count(self) -> int:
        with closing(self.conn.execute("SELECT COUNT(*) FROM users")) as cur:
            return int(cur.fetchone()[0])

    # ---------- writes ----------
    def insert(self, user: User) -> User:
        """
        Insert a user (lets DB assign id via AUTOINCREMENT).
        Returns the new row id.
        """
        sql = "INSERT INTO users (name, email, active) VALUES (?, ?, ?)"
        with self.conn:
            cur = self.conn.execute(sql, (user.name, user.email, int(user.active)))
            user.id = cast(int, cur.lastrowid)
            return user

    def insert_many(self, users: Iterable[User]) -> int:
        """Bulk insert; returns number of rows inserted."""
        sql = "INSERT INTO users (name, email, active) VALUES (?, ?, ?)"
        users_list = list(users)
        params = [(u.name, u.email, int(u.active)) for u in users_list]
        with self.conn:
            self.conn.executemany(sql, params)
        return len(users_list)

    def update(self, user: User) -> bool:
        """Update an existing user by id. Returns True if exactly one row was updated."""
        sql = "UPDATE users SET name = ?, email = ?, active = ? WHERE id = ?"
        with self.conn:
            cur = self.conn.execute(sql, (user.name, user.email, int(user.active), user.id))
            return cur.rowcount == 1

    def set_active(self, user_id: int, active: bool) -> bool:
        """Toggle a user's active flag. Returns True if a row was updated."""
        sql = "UPDATE users SET active = ? WHERE id = ?"
        with self.conn:
            cur = self.conn.execute(sql, (int(active), user_id))
            return cur.rowcount == 1

    def delete(self, user_id: int) -> bool:
        """Delete by id. Returns True if a row was deleted."""
        sql = "DELETE FROM users WHERE id = ?"
        with self.conn:
            cur = self.conn.execute(sql, (user_id,))
            return cur.rowcount == 1

    # ---------- paging ----------
    def get_all_paged(self, limit: int, offset: int = 0) -> List[User]:
        sql = """
            SELECT id, name, email, active
            FROM users
            ORDER BY id
            LIMIT ? OFFSET ?
        """
        with closing(self.conn.execute(sql, (limit, offset))) as cur:
            return [self._row_to_user(r) for r in cur.fetchall()]

    # ---------- lifecycle ----------
    def close(self) -> None:
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()


if __name__ == "__main__":
    with UserDAO() as dao:
        print("Total users:", dao.count())
        for u in dao.get_all():
            print(u)
