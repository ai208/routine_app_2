import unittest
from models.user_model import UserModel
from repositories.user_repository import UserRepository
# repository → storage なので storageが必要

# ダミーデータを作成する 
class FakeStorage:
    def __init__(self):
        self.data = {}
    def load(self):
        return self.data
    def save(self,data):
        self.data = data


class TestUserRepository(unittest.TestCase):
    def test_add_and_get(self):
        storage = FakeStorage()
        repo = UserRepository(storage)

        repo.add(UserModel("Alice",id = "1"))
        user= repo.get_by_id("1") # id = str
        self.assertEqual(user.username, "Alice")
    def test_update(self):
        storage = FakeStorage()
        repo = UserRepository(storage)
        repo.add(UserModel("tom",id = "1"))
        user_1 = UserModel("alice",id="1")
        repo.update(user_id ="1",user=user_1)
        user_2 = repo.get_by_id("1")
        self.assertEqual(user_1.username,user_2.username)
    #全部消えないことも確認する。
    def test_delete(self):
        storage = FakeStorage()
        repo = UserRepository(storage)
        repo.add(UserModel("tom",id = "1"))
        repo.add(UserModel("tom",id = "2"))
        repo.delete("1")
        user_1 = repo.get_by_id("1")
        user_2 = repo.get_by_id("2")
        self.assertIsNone(user_1)
        self.assertEqual(user_2.username,"tom")
    # load save も忘れない　storage.dataの方と比較する
    def test_load(self):
        storage = FakeStorage()
        storage.data = {
            "1":UserModel("tom",id = "1"),
            "2":UserModel("ann",id = "2"),
        }
        repo = UserRepository(storage)
        user_1 = repo.get_by_id("1")
        user_2 = repo.get_by_id("2")
        self.assertEqual(storage.data["1"].username,user_1.username)
        self.assertEqual(storage.data["2"].username,user_2.username)
    # saveも storage.dataとの比較
    def test_save(self):
        storage= FakeStorage()
        repo = UserRepository(storage)
        user_1 = UserModel("ann",id = "1")
        repo.add(user_1)
        user_2 = repo.get_by_id("1")
        self.assertEqual(storage.data["1"].username,user_1.username)
        self.assertEqual(storage.data["1"].username,user_2.username)
