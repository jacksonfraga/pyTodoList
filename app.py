from flask import Flask
from blueprint.todo import api
from persistence.create_engine import init_db
from persistence.create_db import create_db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

app.register_blueprint(api)
init_db(app)

if __name__ == '__main__':
    create_db()
    app.run(debug=True)