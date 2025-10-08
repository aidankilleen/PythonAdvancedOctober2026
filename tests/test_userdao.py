import os
import sqlite3
import pytest

from User import User
from UserDAO import UserDAO

DB_FILE = "testdatabase.db"

@pytest.fixture(scope="session", autouse=True)
def setup_database():

    # delete db if it exists
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    conn = sqlite3.connect(DB_FILE)

    cursor = conn.cursor()

    sql = """
    CREATE TABLE "users" (
	"id"	INTEGER UNIQUE,
	"name"	TEXT,
	"email"	TEXT,
	"active"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
)
    """
    cursor.execute(sql)

    sql = "INSERT INTO users (id, name, email, active) VALUES(1, 'Alice', 'alice@gmail.com', True)"

    cursor.execute(sql)

    conn.commit()
    conn.close()

    yield

    # delete the database
    #if os.path.exists(DB_FILE):
    #    os.remove(DB_FILE)




@pytest.fixture
def dao():
    dao = UserDAO(DB_FILE)
    try:
        yield dao
    finally:
        dao.close()


def test_sample():

    print("testing the get all users function")

    #raise ValueError("invalid value")
    v = 10

def test_get_all_users():
    assert 1 == 1

def test_open_dao(dao):
    #dao = UserDAO()
    assert dao != None
    users = dao.get_all()

    assert len(users) > 0
    #dao.close()

def test_add_user(dao):
    new_user = User(-1, "New User", "new.user@gmail.com", True)
    added_user = dao.add(new_user)

    assert added_user.id != -1

def test_add_user_with_apostrophe(dao):

    new_user = User(-1, "John O'Sullivan", "jono@gmail.com", False)
    added_user = dao.add(new_user)

    assert added_user.id != -1

def test_sql_injection(dao):

    new_user = User(-1, "'','',0); delete from users where name='New User';", "jono@gmail.com", False)
    added_user = dao.add(new_user)

    assert added_user.id != -1


def test_delete(dao):

    original_count = len(dao.get_all())
    new_user = User(-1, "John O'Sullivan", "jono@gmail.com", False)
    added_user = dao.add(new_user)

    intermediate_count = len(dao.get_all())

    assert original_count == intermediate_count - 1

    dao.delete(added_user.id)

    final_count = len(dao.get_all())

    assert original_count == final_count

def test_get_by_id_exists(dao):

    user = dao.get_by_id(1)
    assert user.name == "Alice"
    

def test_get_by_id_not_exists(dao):
    # this verifies that a LookupError is raised
    with pytest.raises(LookupError):
        user = dao.get_by_id(9999)


def test_update(dao):

    # get a user
    user_to_update = dao.get_by_id(1)
    # update the user
    user_to_update.name = "CHANGED"

    dao.update(user_to_update)

    # get the user again
    updated_user = dao.get_by_id(1)

    # verify changes
    assert updated_user.name == "CHANGED"

    user_to_update.name = "Alice"
    dao.update(user_to_update)
