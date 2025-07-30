import unittest
import shutil
import os
from app import app

class CMSTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.data_path = os.path.join(os.path.dirname(__file__), "data")
        os.makedirs(self.data_path, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.data_path, ignore_errors=True)

    def admin_session(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'admin'

            return c

    def create_document(self, name, content=""):
        with open(os.path.join(self.data_path, name), 'w') as file:
            file.write(content)

    def test_index(self):
        self.create_document("about.md")
        self.create_document("changes.txt")

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertIn("about.md", response.get_data(as_text=True))
        self.assertIn("changes.txt", response.get_data(as_text=True))

    def test_file_content(self):
        self.create_document("history.txt", "Python 0.9.0")

        with self.client.get("/history.txt") as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/plain; charset=utf-8")
            self.assertIn("Python 0.9.0", response.get_data(as_text=True))

    def test_document_not_found(self):
        imagined_file = "imaginary_file.txt"

        with self.client.get(f"/{imagined_file}") as response:
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.content_type, "text/html; charset=utf-8")

        with self.client.get(response.headers['Location']) as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/html; charset=utf-8")
            self.assertIn(f'{imagined_file} does not exist', response.get_data(as_text=True))

        with self.client.get("/") as response:
            self.assertNotIn(imagined_file, response.get_data(as_text=True))

    def test_viewing_markdown(self):
        self.create_document("about.md", "#Python is")

        with self.client.get('/about.md') as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/html; charset=utf-8")
            self.assertIn("<h1>Python is", response.get_data(as_text=True))

    def test_editing_document(self):
        self.create_document("changes.txt", "some content")

        client = self.admin_session()
        response = client.get('/changes.txt/edit')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertIn('<textarea', response.get_data(as_text=True))
        self.assertIn('<button type', response.get_data(as_text=True))
        self.assertIn('some content', response.get_data(as_text=True))

    def test_updating_document(self):
        self.create_document("changes.txt", "some content")

        client = self.admin_session()
        response = client.post('/changes.txt', data={'content': 'new content'})
        self.assertEqual(response.status_code, 302)

        follow_response = client.get(response.headers['Location'])
        self.assertIn('changes.txt has been updated',
                      follow_response.get_data(as_text=True))

        with client.get('/changes.txt') as content_response:
            self.assertEqual(content_response.status_code, 200)
            self.assertIn('new content', content_response.get_data(as_text=True))

    def test_view_new_document_form(self):
        client = self.admin_session()
        response = client.get("/new_document")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<input', response.get_data(as_text=True))
        self.assertIn('<button type', response.get_data(as_text=True))

    def test_create_new_document(self):
        client = self.admin_session()
        response = client.post("/create_document",
                                    data={"filename": "text.txt"},
                                    follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("text.txt has been created", response.get_data(as_text=True))

        response = self.client.get("/")
        self.assertIn("text.txt", response.get_data(as_text=True))

    def test_create_new_document_without_filename(self):
        client = self.admin_session()
        response = client.post("/create_document",
                                    data={"filename": ""},
                                    follow_redirects=True)

        self.assertEqual(response.status_code, 422)
        self.assertIn("A name is required", response.get_data(as_text=True))

    def test_create_new_document_with_taken_name(self):
        client = self.admin_session()
        filename = "text.txt"
        self.create_document(filename)
        response = client.post("/create_document",
                                data={"filename": "text.txt"},
                                follow_redirects=True)

        self.assertEqual(response.status_code, 422)
        self.assertIn(f"{filename} already exists", response.get_data(as_text=True))

    def test_delete_document(self):
        self.create_document("text.txt")

        client = self.admin_session()
        response = client.post(f"/text.txt/delete",
                                    follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('text.txt has been deleted', response.get_data(as_text=True))

        response = client.get("/")
        self.assertNotIn('text.txt', response.get_data(as_text=True))

    def test_sign_in_page(self):
        response = self.client.get("/users/signin")
        self.assertEqual(response.status_code, 200)
        self.assertIn("<form method", response.get_data(as_text=True))
        self.assertIn("<button type", response.get_data(as_text=True))

    def test_sign_in_success(self):
        response = self.client.post("/users/signin",
                                    data={
                                        "username": "admin",
                                        "password": "secret"
                                    },
                                    follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome!", response.get_data(as_text=True))
        self.assertIn("Signed in as admin", response.get_data(as_text=True))

    def test_sign_in_fail(self):
        response = self.client.post("/users/signin",
                                    data={
                                        "username": "admin",
                                        "password": "secret1"
                                    },
                                    follow_redirects=True)
        self.assertEqual(response.status_code, 422)
        self.assertIn("Invalid credentials", response.get_data(as_text=True))

    def test_sign_out(self):
        self.client.post("/users/signin",
                         data={
                             'username': 'admin',
                             'password': 'secret'
                         },
                         follow_redirects=True)

        response = self.client.post("/users/signout",
                                    follow_redirects=True)
        self.assertIn('You have been signed out',
                      response.get_data(as_text=True))
        self.assertIn('Sign In', response.get_data(as_text=True))

if __name__ == "main":
    unittest.main()