from fastapi import UploadFile
from .BaseController import BaseController
from helpers.config import get_settings, Settings

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale=1024*1024  # 1MB
    def validate_file(self, file: UploadFile):
        if file.content_type not in self.settings.FILE_ALLOWED_TYPES:
            return False
        if file.size > self.settings.FILE_MAX_SIZE*self.size_scale:
            return False
        return True