import os
import yaml
from flask import Flask
from flask_migrate import Migrate
from app import db 

def create_app():
    # --- load config
    cfg_path = os.path.join('app', 'config', 'app.yml')
    with open(cfg_path, 'r') as f:
        cfg = yaml.safe_load(f)

    db_cfg = cfg['database']
    DB_URI = f"{db_cfg['dialect']}+{db_cfg['driver']}://{db_cfg['username']}:{db_cfg['password']}@{db_cfg['host']}:{db_cfg['port']}/{db_cfg['database']}"

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = cfg.get('app', {}).get('debug', False)

    # Прив'язуємо db до Flask
    db.init_app(app)
    migrate = Migrate(app, db)

    # Імпортуємо моделі після створення db
    from app.my_project.auth.domain import models
    app.config['DEBUG'] = True

    # Регіструємо маршрути
    from app.my_project.auth.route.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api')
    # Додайте це в run.py перед if __name__ == '__main__':

    @app.route('/')
    def index():
        return "Привіт! Сервер працює, але це API. Використовуйте /staff або /student"
    return app
    
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
