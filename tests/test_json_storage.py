import unittest
import tempfile
from pathlib import Path
from storage.json_storage import JsonStorage

class TestJsonStorage(unittest.TestCase):
    #作成テスト
    def test_file_creation_and_load(self):
        # 一次ファイルができる
        with tempfile.TemporaryDirectory() as tmpdir: # テスト用の場所
            file_path = Path(tmpdir) / "test.json"
            #ファイルの作成の確認
            storage = JsonStorage(file_path)
            self.assertEqual(storage.load(),[]) #中身がからか

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) /"test.json"
            storage = JsonStorage(file_path)
            data = [{"name":"Alice"},{"name":"Bob"}] #簡単なデータ
            storage.save(data)
            loaded = storage.load()
            self.assertEqual(loaded,data)

    if __name__ == "__main__":
        unittest
