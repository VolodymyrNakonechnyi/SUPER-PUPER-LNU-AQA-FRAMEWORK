from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from config.config import Config
import time
import os


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.actions = ActionChains(driver)
    
    def open_url(self, url):
        """Open URL in browser"""
        self.driver.get(url)
    
    def find_element(self, locator):
        """Find single element with explicit wait"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Find multiple elements"""
        return self.driver.find_elements(*locator)
    
    def click_element(self, locator):
        """Click element with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        """Send keys to element"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from element"""
        element = self.find_element(locator)
        return element.text
    
    def get_attribute(self, locator, attribute):
        """Get attribute value from element"""
        element = self.find_element(locator)
        return element.get_attribute(attribute)
    
    def is_element_present(self, locator):
        """Check if element is present"""
        try:
            self.find_element(locator)
            return True
        except:
            return False
    
    def is_element_visible(self, locator):
        """Check if element is visible"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False
    
    def wait_for_element_visible(self, locator, timeout=None):
        """Wait for element to be visible"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator, timeout=None):
        """Wait for element to be clickable"""
        wait_time = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def select_dropdown_by_text(self, locator, text):
        """Select dropdown option by visible text"""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)
    
    def select_dropdown_by_value(self, locator, value):
        """Select dropdown option by value"""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_value(value)
    
    def hover_element(self, locator):
        """Hover over element"""
        element = self.find_element(locator)
        self.actions.move_to_element(element).perform()
    
    def scroll_to_element(self, locator):
        """Scroll to element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def take_screenshot(self, filename=None):
        """Take screenshot"""
        if not filename:
            timestamp = int(time.time())
            filename = f"screenshot_{timestamp}.png"
        
        # Create screenshots directory if it doesn't exist
        os.makedirs(Config.SCREENSHOTS_DIR, exist_ok=True)
        filepath = os.path.join(Config.SCREENSHOTS_DIR, filename)
        
        self.driver.save_screenshot(filepath)
        return filepath
    
    def switch_to_frame(self, locator):
        """Switch to iframe"""
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)
    
    def switch_to_default_content(self):
        """Switch back to default content"""
        self.driver.switch_to.default_content()
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
    
    def get_page_title(self):
        """Get page title"""
        return self.driver.title
    
    def refresh_page(self):
        """Refresh current page"""
        self.driver.refresh()
    
    def go_back(self):
        """Go back in browser history"""
        self.driver.back()
    
    def go_forward(self):
        """Go forward in browser history"""
        self.driver.forward()
