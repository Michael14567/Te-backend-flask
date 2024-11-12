from flask import Fask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Инициализация расширений
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализация расширений с приложением
    db.init_app(app)
    migrate.init_app(app, db)

    # Регистрация blueprint для аутентификации и других маршрутов
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
