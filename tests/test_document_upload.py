
import unittest
import os
from src.document_upload import app
from werkzeug.datastructures import FileStorage

class TestDocumentUpload(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['UPLOAD_FOLDER'] = 'src/uploads'

    def test_upload_document(self):
        test_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'test.pdf')
        with open(test_file_path, 'rb') as test_file:
            file = FileStorage(
                stream=test_file,
                filename='test.pdf',
                content_type='application/pdf'
            )
            response = self.app.post('/upload', 
                data={'file': file},
                content_type='multipart/form-data'
            )
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
