from flask import Flask
from blueprint.todo import api
from persistence.create_db import create_db
from infrastructure.frontend import web_app
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bbddd2acec8c7f:d38988f70b18b9e@us-cdbr-iron-east-01.cleardb.net/heroku_78038307a9708b3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:matramcs@127.0.0.1/todolist'

app.register_blueprint(api)

# blueprint para substituir Nginx no Heroku
app.register_blueprint(web_app)

if __name__ == '__main__':
    create_db(app)
    port = int(os.environ.get("PORT", 5555))
    app.run(debug=True, port=port)
