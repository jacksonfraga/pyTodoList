from flask import send_from_directory, Blueprint

web_app = Blueprint('web_server', __name__)

#route para prover "home"
@web_app.route('/')
def index():
    return send_from_directory('templates', 'index.html')
