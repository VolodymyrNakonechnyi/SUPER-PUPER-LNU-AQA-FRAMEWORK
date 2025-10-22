import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Browser settings
    BROWSER = os.getenv('BROWSER', 'firefox')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    WINDOW_SIZE = os.getenv('WINDOW_SIZE', '1920,1080')
    
    # Timeouts
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', '20'))
    PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30'))
    
    # Test data
    BASE_URL = os.getenv('BASE_URL', 'https://testmoz.com')
    
    # Reports
    SCREENSHOTS_DIR = 'screenshots'
    REPORTS_DIR = 'reports'
    
    @classmethod
    def get_window_size(cls):
        return tuple(map(int, cls.WINDOW_SIZE.split(',')))
