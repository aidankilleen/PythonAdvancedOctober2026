import pytest

from User import User
from UserDAO import UserDAO

@pytest.fixture
def dao():
    dao = UserDAO()
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
