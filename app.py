from flask import Flask, request, render_template
from datetime import timedelta
from view.user import user
from libs import config
from libs.db_sql import *

app = Flask(__name__)
app.config['SECRET_KEY'] ='adkaldmskmdkdkd'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config.from_object(config)
app.register_blueprint(user)
db.init_app(app)
db.create_all(app=app)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500


if __name__ == '__main__':
    app.run()
