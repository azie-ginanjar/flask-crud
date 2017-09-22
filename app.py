from flask import Flask
from flask_appconfig import AppConfig

from models.user import db

app = Flask(__name__)
config = AppConfig()
default_config = "default_config"
config.init_app(app, default_settings=default_config)
db.init_app(app)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
