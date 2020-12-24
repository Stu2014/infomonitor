from flask import Flask,request
from datetime import timedelta
from view.user import user
from libs import config
from libs.db_sql import *

app = Flask(__name__)
app.config['SECRET_KEY'] ='adkaldmskmdkdkd'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config.from_object(config)
db.init_app(app)
db.create_all(app=app)
app.register_blueprint(user)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
