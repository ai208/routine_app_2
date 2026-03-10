# model データ構造の定義
# 2
from datetime import date
class RoutineModel:
    def __init__(self,name,user_id,done = False,total_done = 0, last_done = None):
        self.name = name
        self.user_id = user_id
        self.done = done
        self.total_done = total_done
        self.last_done = last_done
    def to_dict(self):#自身(cls)をdata(json)へ
        return {
            "name":self.name,
            "user_id":self.user_id,
            "done":self.done,
            "total_done":self.total_done,
            "last_done": self.last_done.isoformat() if self.last_done else None
        }
    @classmethod
    def from_dict(cls,data):#data →　cls
        last_done = date.fromisoformat(data["last_done"]) if data.get("last_done") else None
        return cls(
            name = data["name"],
            user_id = data["user_id"],
            done = data.get("done"),
            total_done = data["total_done"],
            last_done = last_done,
        )