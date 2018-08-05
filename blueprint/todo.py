from flask import Blueprint, jsonify, current_app, request
from service.todo import TodoService

api = Blueprint('todo', __name__, url_prefix='/api/todo')


@api.route('/', methods=['POST'])
def create():
    data = request.json
    return jsonify(TodoService(current_app).create(data).to_dict())


@api.route('/all', methods=['GET'])
def get_all():
    data = TodoService(current_app).get_all()
    # data = {'data': 'test oks'}
    return jsonify(todos=[d.to_dict() for d in data])

@api.route('/done', methods=['GET'])
def get_done():
    data = TodoService(current_app).get_done()
    # data = {'data': 'test oks'}
    return jsonify(todos=[d.to_dict() for d in data])

@api.route('/doing', methods=['GET'])
def get_doing():
    data = TodoService(current_app).get_doing()
    # data = {'data': 'test oks'}
    return jsonify(todos=[d.to_dict() for d in data])


@api.route('/<int:todo_id>', methods=['POST'])
def update(todo_id):
    data = request.json
    return jsonify(TodoService(current_app).update(todo_id, data).to_dict())


@api.route('/<int:todo_id>', methods=['DELETE'])
def delete(todo_id):
    return jsonify(TodoService(current_app).delete(todo_id))
