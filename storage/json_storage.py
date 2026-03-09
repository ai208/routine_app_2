# 汎用的なjson の読み取り、書き込みの関数　両方で共通している
# 1
import json
from  pathlib import Path

class JsonStorage:
    def __init__(self,file_path):
        super().__init__()
        self.file_path = Path(file_path)
        if not self.file_path.exists(): #存在しない時は、空をファイルを作る
            self.file_path.write_text("[]")
    def load(self):
        with open (self.file_path,"r",encoding="utf-8") as f:
            return json.load(f)
    def save(self,data):
        with open(self.file_path, "w",encoding="utf-8") as f:
            json.dump(data,f,indent=2)