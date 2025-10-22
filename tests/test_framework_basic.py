import pytest
import os
from config.config import Config


class TestFrameworkBasic:
    """Basic tests to verify framework setup without browser"""
    
    def test_config_loading(self):
        """Test that configuration loads correctly"""
        assert Config.BROWSER is not None
        assert Config.HEADLESS is not None
        assert Config.WINDOW_SIZE is not None
        assert Config.IMPLICIT_WAIT is not None
        assert Config.EXPLICIT_WAIT is not None
        assert Config.PAGE_LOAD_TIMEOUT is not None
        assert Config.BASE_URL is not None
    
    def test_config_values(self):
        """Test configuration values are reasonable"""
        assert Config.IMPLICIT_WAIT > 0
        assert Config.EXPLICIT_WAIT > 0
        assert Config.PAGE_LOAD_TIMEOUT > 0
        assert "http" in Config.BASE_URL
        assert Config.BROWSER in ["chrome", "firefox", "edge"]
    
    def test_directories_creation(self):
        """Test that required directories can be created"""
        # Test reports directory
        os.makedirs(Config.REPORTS_DIR, exist_ok=True)
        assert os.path.exists(Config.REPORTS_DIR)
        
        # Test screenshots directory
        os.makedirs(Config.SCREENSHOTS_DIR, exist_ok=True)
        assert os.path.exists(Config.SCREENSHOTS_DIR)
    
    def test_window_size_parsing(self):
        """Test window size parsing"""
        window_size = Config.get_window_size()
        assert len(window_size) == 2
        assert window_size[0] > 0  # width
        assert window_size[1] > 0  # height
    
    def test_environment_variables(self):
        """Test environment variable handling"""
        # Test that we can set and get environment variables
        test_var = "TEST_FRAMEWORK_VAR"
        test_value = "test_value_123"
        
        os.environ[test_var] = test_value
        assert os.getenv(test_var) == test_value
        
        # Clean up
        del os.environ[test_var]
    
    def test_imports_work(self):
        """Test that all framework imports work"""
        try:
            from framework.webdriver_manager import WebDriverManager
            from framework.base_page import BasePage
            from pages.testmoz_home_page import TestmozHomePage
            from pages.testmoz_demo_page import TestmozDemoPage
            assert True  # If we get here, imports work
        except ImportError as e:
            pytest.fail(f"Import failed: {e}")
    
    def test_page_object_structure(self):
        """Test that page objects have required methods"""
        from pages.testmoz_home_page import TestmozHomePage
        from pages.testmoz_demo_page import TestmozDemoPage
        
        # Check that TestmozHomePage has required methods
        required_home_methods = [
            'open_testmoz', 'get_main_heading_text', 'click_build_a_test',
            'click_try_demo', 'is_main_heading_visible'
        ]
        
        for method in required_home_methods:
            assert hasattr(TestmozHomePage, method), f"TestmozHomePage missing method: {method}"
        
        # Check that TestmozDemoPage has required methods
        required_demo_methods = [
            'get_demo_title', 'click_start_test', 'get_current_question_text',
            'select_radio_option', 'click_next_question'
        ]
        
        for method in required_demo_methods:
            assert hasattr(TestmozDemoPage, method), f"TestmozDemoPage missing method: {method}"
    
    def test_base_page_methods(self):
        """Test that BasePage has required methods"""
        from framework.base_page import BasePage
        
        required_methods = [
            'open_url', 'find_element', 'find_elements', 'click_element',
            'send_keys', 'get_text', 'is_element_present', 'is_element_visible',
            'take_screenshot', 'get_current_url', 'get_page_title'
        ]
        
        for method in required_methods:
            assert hasattr(BasePage, method), f"BasePage missing method: {method}"
    
    def test_webdriver_manager_structure(self):
        """Test that WebDriverManager has required methods"""
        from framework.webdriver_manager import WebDriverManager
        
        assert hasattr(WebDriverManager, 'create_driver'), "WebDriverManager missing create_driver method"
        assert callable(WebDriverManager.create_driver), "create_driver should be callable"
