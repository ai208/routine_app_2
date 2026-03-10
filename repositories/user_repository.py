# jsonの読み書き
# service → repositroy → storage 
# 役割 : CRUD → save 開いた時に、　loadする
# 3

class UserRepository:
    def __init__(self,storage):
        self.storage = storage
        self.users = {} # 何もない
        self.load() # 読み取る
    # 読み取りでroutineを作る
    def load(self):
        self.users = self.storage.load()
    #保存
    def save(self):
        self.storage.save(self.users)
    # CRUD
    # create
    def add(self,user):
        self.users[user.id] = user
        self.save()
    # read
    def get_by_id(self,user_id): #オブジェクトで返す
        return self.users.get(user_id) or None
    # update
    def update(self,user_id,user):
        self.users[user_id] = user
        self.save()
    # delete
    def delete(self,user_id):
        del self.users[user_id]
        self.save()