"""
Модели базы данных для бота
"""

from datetime import datetime

# Временные структуры данных
# Позже заменим на реальную БД

users_db = {}
requests_db = {}
premium_db = {}

class User:
    def __init__(self, user_id, username, first_name):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.join_date = datetime.now()
        self.requests_today = 0
        self.total_requests = 0
        self.is_premium = False
        self.premium_until = None
        self.referrals = 0
        self.bonus_requests = 0

def get_user(user_id):
    """Получить пользователя из базы"""
    return users_db.get(user_id)

def create_user(user_id, username, first_name):
    """Создать нового пользователя"""
    user = User(user_id, username, first_name)
    users_db[user_id] = user
    return user

def can_make_request(user_id):
    """Проверить, может ли пользователь сделать запрос"""
    user = get_user(user_id)
    if not user:
        return False
    
    if user.is_premium:
        return True
    
    return user.requests_today < 3

def register_request(user_id):
    """Зарегистрировать запрос пользователя"""
    user = get_user(user_id)
    if user:
        user.requests_today += 1
        user.total_requests += 1
        return True
    return False
