from flask import Flask
from .api import bp as api_bp

def create_app() -> Flask:
    app = Flask(__name__)
    
    app.json.sort_keys=False
    app.config["JASON_SORT_KEYS"] = False

    app.register_blueprint(api_bp)
    return app

#para `flask run`

app=create_app()
