from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.config import Config
import os
import platform
import shutil


class WebDriverManager:
    @staticmethod
    def find_driver_in_path(driver_name):
        """Find driver in system PATH"""
        return shutil.which(driver_name)
    
    @staticmethod
    def create_driver():
        """Create and configure WebDriver instance"""
        browser = Config.BROWSER.lower()
        
        if browser == 'chrome':
            options = ChromeOptions()
            if Config.HEADLESS:
                options.add_argument('--headless')
            options.add_argument(f'--window-size={Config.WINDOW_SIZE}')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-web-security')
            options.add_argument('--allow-running-insecure-content')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--disable-background-timer-throttling')
            options.add_argument('--disable-backgrounding-occluded-windows')
            options.add_argument('--disable-renderer-backgrounding')
            options.add_argument('--disable-features=TranslateUI')
            options.add_argument('--disable-ipc-flooding-protection')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            
            # Try to find chromedriver in PATH first
            driver_path = WebDriverManager.find_driver_in_path('chromedriver')
            if driver_path:
                service = ChromeService(driver_path)
            else:
                # Use webdriver-manager as fallback
                try:
                    # Try to get compatible ChromeDriver version
                    driver_path = ChromeDriverManager().install()
                    service = ChromeService(driver_path)
                    print(f"Using ChromeDriver from webdriver-manager: {driver_path}")
                except Exception as e:
                    print(f"WebDriver Manager failed: {e}")
                    # Try without service as last resort
                    service = None
            
            try:
                if service:
                    driver = webdriver.Chrome(service=service, options=options)
                else:
                    driver = webdriver.Chrome(options=options)
                print("Chrome driver created successfully")
            except Exception as e:
                print(f"Chrome failed: {e}")
                print("Attempting fallback to Firefox...")
                # Fallback to Firefox
                return WebDriverManager._create_firefox_driver()
            
        elif browser == 'firefox':
            return WebDriverManager._create_firefox_driver()
            
        elif browser == 'edge':
            options = EdgeOptions()
            if Config.HEADLESS:
                options.add_argument('--headless')
            options.add_argument(f'--window-size={Config.WINDOW_SIZE}')
            
            # Try to find edgedriver in PATH first
            driver_path = WebDriverManager.find_driver_in_path('msedgedriver')
            if driver_path:
                service = EdgeService(driver_path)
            else:
                service = None
            
            try:
                if service:
                    driver = webdriver.Edge(service=service, options=options)
                else:
                    driver = webdriver.Edge(options=options)
            except Exception as e:
                print(f"Edge failed: {e}")
                # Fallback to Firefox
                return WebDriverManager._create_firefox_driver()
            
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        # Configure timeouts
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        return driver
    
    @staticmethod
    def _create_firefox_driver():
        """Create Firefox driver with fallback options"""
        options = FirefoxOptions()
        if Config.HEADLESS:
            options.add_argument('--headless')
        
        # Add CI/CD specific options
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-web-security')
        options.add_argument('--allow-running-insecure-content')
        
        # Set window size
        options.add_argument(f'--width={Config.get_window_size()[0]}')
        options.add_argument(f'--height={Config.get_window_size()[1]}')
        
        # Try to find geckodriver in PATH first
        driver_path = WebDriverManager.find_driver_in_path('geckodriver')
        
        if not driver_path:
            # Use webdriver-manager as fallback
            try:
                driver_path = GeckoDriverManager().install()
            except Exception as e:
                print(f"WebDriver Manager failed: {e}")
                driver_path = None
        
        try:
            if driver_path:
                service = FirefoxService(driver_path)
                driver = webdriver.Firefox(service=service, options=options)
            else:
                # Try without service (use system geckodriver)
                driver = webdriver.Firefox(options=options)
        except Exception as e:
            print(f"Firefox failed: {e}")
            # Last resort - try Chrome without service
            try:
                chrome_options = ChromeOptions()
                if Config.HEADLESS:
                    chrome_options.add_argument('--headless')
                chrome_options.add_argument(f'--window-size={Config.WINDOW_SIZE}')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                driver = webdriver.Chrome(options=chrome_options)
                print("Using Chrome as fallback")
            except Exception as chrome_e:
                print(f"All browsers failed. Chrome error: {chrome_e}")
                raise Exception("No working browser found. Please install Chrome, Firefox, or Edge with their respective drivers.")
        
        # Configure timeouts
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        return driver