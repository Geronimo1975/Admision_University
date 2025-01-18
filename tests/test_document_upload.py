<<<<<<< HEAD

import unittest
from src.document_upload import *  # Import your document_upload module

class TestDocumentUpload(unittest.TestCase):
    def test_file_upload(self):
        # Add your test logic here
        pass

    def test_file_validation(self):
        # Add your test logic here
        pass
=======
import pytest
from document_upload import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_upload_document(client):
    data = {"file": (b"Test file content", "test.pdf")}
    response = client.post("/upload", content_type="multipart/form-data", data=data)
    assert response.status_code == 200
>>>>>>> 484d55e (Update)
