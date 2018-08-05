import unittest
from app import todo_app


class TestHome(unittest.TestCase):

    def setUp(self):
        client = todo_app.test_client()
        self.response = client.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    # def test_content(self):
    #     self.assertIn('Jackson Fraga', self.response.data.decode('utf-8'))


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = todo_app.test_client()
        self.last_id = ""

    def test_get(self):
        response = self.client.get('/api/todo/')
        self.assertEqual(200, response.status_code)

    def test_create(self):
        todo_description = 'learn math'
        data_todo = {
            'description': todo_description
        }
        response = self.post('/api/todo/', json=data_todo)
        data_response = response.get_json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(todo_description, data_response['description'])
        self.last_id = data_response['id']


if __name__ == '__main__':
    unittest.main()
