import unittest
from datetime import date
from models.routine_model import RoutineModel
# Userを参考に自分で記述した。 # idを追加した
class TestRoutineModel(unittest.TestCase):
    def test_init_default_values(self): #初期値のテスト
        routine = RoutineModel("tom","123")
        self.assertEqual(routine.name,"tom")
        self.assertEqual(routine.user_id,"123")
        self.assertIsInstance(routine.id,str)
        self.assertEqual(routine.done,False)
        self.assertEqual(routine.total_done,0)
        self.assertIsNone(routine.last_done)

    def test_init_with_argument(self): #引数を取る時のテスト ここで引数を取ったら後は要らない。
        routine = RoutineModel("tom","123",id = "1234",done = True,total_done=3,last_done=date(2026,1,1))
        self.assertEqual(routine.done,True)
        self.assertEqual(routine.total_done,3)
        self.assertEqual(routine.id,"1234")
        self.assertIsInstance(routine.last_done,date) #型の確認
        self.assertEqual(routine.last_done,date(2026,1,1))

    def test_to_dict(self):# model -> data
        routine = RoutineModel("tom","123")
        data = routine.to_dict()
        self.assertEqual(data["name"],"tom")
        self.assertEqual(data["user_id"],"123")
        self.assertIsInstance(data["id"],str)
        self.assertEqual(data["done"],False)
        self.assertEqual(data["total_done"],0)
        self.assertIsNone(data["last_done"])
    def test_to_dict_with_argument(self):# model -> data いらないらしい　重複
        routine = RoutineModel("tom","123",id = "1234",done = True,total_done=3,last_done=date(2026,1,1))
        data = routine.to_dict()
        self.assertEqual(data["name"],"tom")
        self.assertEqual(data["user_id"],"123")
        self.assertEqual(data["id"],"1234")
        self.assertEqual(data["done"],True)
        self.assertEqual(data["total_done"],3)
        self.assertIsInstance(data["last_done"],str)

    def test_from_dict(self):# data -> model
        data = {
            "name":"tom",
            "user_id":"123",
            "id":"1234",
            "done":False,
            "total_done":3,
            "last_done":None
        }
        routine = RoutineModel.from_dict(data)
        self.assertEqual(routine.name,"tom")
        self.assertEqual(routine.user_id,"123")
        self.assertEqual(routine.id,"1234")
        self.assertEqual(routine.done,False)
        self.assertEqual(routine.total_done,3)
        self.assertIsNone(routine.last_done)
    def test_from_dict_with_argument(self):# data -> model いらないらしい　重複
        data = {
            "name":"tom",
            "user_id":"123",
            "id":"1234",
            "done":True,
            "total_done":3,
            "last_done":"2026-01-01"
        }
        routine = RoutineModel.from_dict(data)
        self.assertEqual(routine.name,"tom")
        self.assertEqual(routine.user_id,"123")
        self.assertEqual(routine.id,"1234")
        self.assertEqual(routine.done,True)
        self.assertEqual(routine.total_done,3)
        self.assertIsInstance(routine.last_done,date)
        self.assertEqual(routine.last_done,date(2026,1,1))

    def test_round_trip(self):
        routine_1 = RoutineModel("tome","123")
        data = routine_1.to_dict()
        routine_2 = RoutineModel.from_dict(data)
        self.assertEqual(routine_1.name,routine_2.name)
        self.assertEqual(routine_1.user_id,routine_2.user_id)
        self.assertEqual(routine_1.id,routine_2.id)
        self.assertEqual(routine_1.done,routine_2.done)
        self.assertEqual(routine_1.total_done,routine_2.total_done)
        self.assertEqual(routine_1.last_done,routine_2.last_done)
