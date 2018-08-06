from persistence.todo import TodoPersistence


class TodoService:
    def __init__(self, app):
        self.app = app

    def validate(self, data):
        if data['description'] is None:
            raise ValueError('Descrição não informada.')
        if data['description'] == '':
            raise ValueError('Descrição não pode ser vazia.')
        if len(data['description']) > 255:
            raise ValueError('Descrição não pode conter mais que 255 caracteres')

    def create(self, data):
        self.validate(data)
        item = TodoPersistence(self.app).create(data)
        return item

    def get_all(self):
        return TodoPersistence(self.app).get_all()

    def get_done(self):
        return TodoPersistence(self.app).get_all({'done': True})

    def get_doing(self):
        return TodoPersistence(self.app).get_all({'done': False})

    def update(self, todo_id, data):
        self.validate(data)
        if data['todo_id'] != todo_id:
            raise ValueError('Identificador informado não corresponde ao requisitado.')
        return TodoPersistence(self.app).update(todo_id, data)

    def delete(self, todo_id):
        return TodoPersistence(self.app).delete(todo_id)
