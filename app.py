from flask import Flask
from blueprint.todo import api
from persistence.create_engine import init_db
from persistence.create_db import create_db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bbddd2acec8c7f:d38988f70b18b9e@us-cdbr-iron-east-01.cleardb.net/heroku_78038307a9708b3'

app.register_blueprint(api)
init_db(app)

if __name__ == '__main__':
    create_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
