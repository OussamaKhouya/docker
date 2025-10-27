from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from .config import Config

db = SQLAlchemy()
cache = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    global cache
    cache = Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], db=0)

    from .routes import bp
    app.register_blueprint(bp)

    return app
