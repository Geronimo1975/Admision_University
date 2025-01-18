
import unittest
from flask import Flask
from src import db, create_app

class TestBase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SECRET_KEY'] = 'test-key'
        
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
        self.app_context.pop()
