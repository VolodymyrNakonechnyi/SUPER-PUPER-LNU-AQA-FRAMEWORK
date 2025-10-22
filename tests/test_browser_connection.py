import pytest
from framework.webdriver_manager import WebDriverManager


class TestBrowserConnection:
    """Test browser connection without complex operations"""
    
    @pytest.fixture(scope="function")
    def setup(self):
        """Setup and teardown for each test"""
        driver = WebDriverManager.create_driver()
        yield driver
        driver.quit()
    
    def test_browser_opens(self, setup):
        """Test that browser opens successfully"""
        driver = setup
        assert driver is not None
        # Firefox shows about:blank, Chrome shows data:,
        assert driver.current_url in ["data:,", "about:blank"]
    
    def test_browser_navigates_to_google(self, setup):
        """Test basic navigation to Google"""
        driver = setup
        driver.get("https://www.google.com")
        
        # Verify we're on Google
        assert "google" in driver.current_url.lower()
        assert "Google" in driver.title
    
    def test_browser_navigates_to_testmoz(self, setup):
        """Test navigation to Testmoz"""
        driver = setup
        driver.get("https://testmoz.com")
        
        # Verify we're on Testmoz
        assert "testmoz" in driver.current_url.lower()
        assert "Testmoz" in driver.title
    
    def test_browser_can_find_elements(self, setup):
        """Test that browser can find elements"""
        driver = setup
        driver.get("https://www.google.com")
        
        # Try to find search box
        search_box = driver.find_element("name", "q")
        assert search_box is not None
        assert search_box.is_displayed()
    
    def test_browser_can_interact_with_elements(self, setup):
        """Test basic interaction with elements"""
        driver = setup
        driver.get("https://www.google.com")
        
        # Find and interact with search box
        search_box = driver.find_element("name", "q")
        search_box.send_keys("test automation")
        
        # Verify text was entered
        assert "test automation" in search_box.get_attribute("value")
    
    def test_browser_window_management(self, setup):
        """Test window management"""
        driver = setup
        driver.get("https://www.google.com")
        
        # Test window size
        size = driver.get_window_size()
        assert size['width'] > 0
        assert size['height'] > 0
        
        # Test window position
        position = driver.get_window_position()
        assert position['x'] >= 0
        assert position['y'] >= 0
