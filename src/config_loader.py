
import os
import yaml

class Settings:
    def __init__(self):
        self.load_settings()
    
    def load_settings(self):
        config_path = os.path.join('config', 'settings.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                settings = yaml.safe_load(f)
                for key, value in settings.items():
                    setattr(self, key, value)
        else:
            self.app = {"name": "Admission System", "secret_key": "dev-key"}
            self.database = {"uri": "sqlite:///instance/admission_system.db"}

settings = Settings()
