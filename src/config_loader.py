
import os
import yaml

class Settings:
    def __init__(self):
        self.load_settings()
    
    def load_settings(self):
        config_path = os.path.join('config', 'settings.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            self.config = {}
            
    def __iter__(self):
        return iter(self.config.items())
            
    def get(self, key, default=None):
        return self.config.get(key, default)

settings = Settings()
