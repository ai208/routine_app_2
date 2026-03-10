# モデル　データ構造の定義　
# 2
import uuid
from datetime import date
class UserModel:
    def __init__(self,username, id = None,login_streak=1,last_login = None):
        self.id = id or str(uuid.uuid4())
        self.username =username
        self.login_streak = login_streak
        self.last_login = last_login or date.today()
    def to_dict(self): # self → data(json)
        return {
            "id":self.id,
            "username":self.username,
            "login_streak":self.login_streak,
            "last_login":self.last_login.isoformat() #dateはstr にする必要がある
        }
    @classmethod
    def from_dict(cls,data): # data →　cls #data.get出来たら
        last_login = date.fromisoformat(data["last_login"]) if data.get("last_login") else None #日を変更する
        return cls(
            id = data.get("id"),#key がないときは、None
            username = data["username"], #必ずある場合 #テストで気づいた
            login_streak = data.get("login_streak",1), #key がないときは 1(None)
            last_login = last_login
        )