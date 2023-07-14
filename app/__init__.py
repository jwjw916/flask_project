from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # ORM에 대한 설정
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)


    from .views import basic_views, answer_views, question_views, auth_views
    app.register_blueprint(basic_views.fisa)
    app.register_blueprint(answer_views.ans)
    app.register_blueprint(question_views.ques)
    app.register_blueprint(auth_views.auth_user)

    from .filter import datetime, datetime2
    app.jinja_env.filters['datetime'] = datetime
    app.jinja_env.filters['datetime2'] = datetime2

    return app
