import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')  # Замените на более сложный ключ
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/db_name')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
