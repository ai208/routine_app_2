import unittest
from datetime import date
from models.user_model import UserModel
# AIに教えてもらいながら記述した。
# testを使ってエラーを見つけることができた。
class TestUserModel(unittest.TestCase):
    def test_init_default_values(self):
        user = UserModel("alice")
        self.assertEqual(user.username, "alice")
        self.assertIsInstance(user.id,str)
        self.assertEqual(user.login_streak,1)
        self.assertIsInstance(user.last_login,date)
    def test_init_with_arguments(self):
        user = UserModel("tom",last_login=date(2026,1,1))
        # self.assertEqual(user.username,"tom") #さっき行ったから重複している。
        # self.assertIsInstance(user.id,str)
        # self.assertEqual(user.login_streak,1)
        self.assertEqual(user.last_login,date(2026,1,1))
    def test_to_dict(self):
        user = UserModel("alice")
        data = user.to_dict()
        self.assertEqual(data["username"],"alice")
        self.assertIsInstance(data["last_login"],str)
    def test_from_dict(self):
        data = {
            "id":"123",
            "username":"tom",
            "login_streak":1,
            "last_login":"2026-01-01",
        }
        user = UserModel.from_dict(data)
        self.assertEqual(user.id,"123")
        self.assertEqual(user.username,"tom")
        self.assertEqual(user.login_streak,1)
        self.assertIsInstance(user.last_login,date)
        self.assertEqual(user.last_login,date(2026,1,1))
    def test_from_dict_last_login(self):
        date_now = date.today() #date型
        data = {
            "id":"123",
            "username":"tom",
            "login_streak":1,
            "last_login":date_now.isoformat(),# date型をstr でる。
        }
        user = UserModel.from_dict(data)
        self.assertEqual(user.last_login,date_now)
    def test_from_dict_last_login(self):
        date_now = date.today() #date型
        data = {
            "id":"123",
            "username":"tom",
            "login_streak":1,
            "last_login":None,# date型をstr でる。
        }
        user = UserModel.from_dict(data)
        self.assertEqual(user.last_login,date_now)
        # self.assertIsNone(user.last_login) #間違い
    def test_round_trip(self):
        user1 = UserModel("tom")
        data = user1.to_dict()
        user2 = UserModel.from_dict(data)
        self.assertEqual(user1.username,user2.username)
        self.assertEqual(user1.id,user2.id)
        self.assertEqual(user1.login_streak,user2.login_streak)
        self.assertEqual(user1.last_login,user2.last_login)