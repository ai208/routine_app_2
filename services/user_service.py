# ビジネスロジック
# controller → service → repository 
# repositoryのを受け取って、そこで、計算をする
# 4
from datetime import date,timedelta
class UserService:
    def __init__(self,repository,current_user_id): # 操作するid が必要 ログイン時か、デフォルトで
        super().__init__()
        self.repository = repository
        self.current_user = self.repository.get_by_id(current_user_id) 
        self.longest_login_streak = 0
        self.oldest_login_date = "3000-1-1"

    def user_login_info(self): #    すべてまとめる　repositoryの更新を一度に行う。
        user = self.current_user
        today = date.today()
        if user.last_login != today: #今日でない場合のみ更新する
            self._update_streak(user,today)
            self._update_oldest_login(user)
            user.last_login = today
            #repositoryの更新
            self.repository.update(user)
            self.repository.save()        
        
    def _update_streak(self,user,today):
        if user.last_login == today - timedelta(days =1): #一日差の時は更新する
            user.login_streak += 1
        else:
            user.login_streak = 1
        self.longest_login_streak = max(self.longest_login_streak,user.login_streak)
    def _update_oldest_login(self,user):
        self.oldest_login_date = min(self.oldest_login_date,user.login_date)