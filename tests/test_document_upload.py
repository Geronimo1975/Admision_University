import unittest
from src.document_upload import app
from io import BytesIO

class TestDocumentUpload(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config["TESTING"] = True

    def test_upload_document(self):
        data = {"file": (BytesIO(b"Test file content"), "test.pdf")}
        response = self.app.post("/upload", content_type="multipart/form-data", data=data)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()