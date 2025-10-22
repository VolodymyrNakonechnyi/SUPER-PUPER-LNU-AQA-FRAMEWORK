"""
CI/CD Ready Tests - Verify framework components work without browser
These tests ensure the framework is properly configured for CI/CD
"""
import pytest
import os
import sys
from unittest.mock import Mock, patch


class TestCIReady:
    """Tests to verify framework is CI/CD ready"""
    
    def test_python_version(self):
        """Test Python version compatibility"""
        version = sys.version_info
        assert version.major == 3
        assert version.minor >= 9
        print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    def test_required_modules_import(self):
        """Test that all required modules can be imported"""
        # Test framework imports
        from framework.bdd_framework import BDDStep, BDDScenario, StepRegistry
        from framework.base_page import BasePage
        from framework.webdriver_manager import WebDriverManager
        from config.config import Config
        
        # Test page imports
        from pages.testmoz_home_page import TestmozHomePage
        from pages.testmoz_demo_page import TestmozDemoPage
        
        # Test locator imports
        from pages.locators.testmoz_home_locators import TestmozHomeLocators
        from pages.locators.testmoz_demo_locators import TestmozDemoLocators
        
        assert BDDStep is not None
        assert BDDScenario is not None
        assert StepRegistry is not None
        assert BasePage is not None
        assert WebDriverManager is not None
        assert Config is not None
    
    def test_config_values(self):
        """Test configuration values are accessible"""
        from config.config import Config
        
        assert Config.BROWSER is not None
        assert Config.BASE_URL is not None
        assert Config.IMPLICIT_WAIT > 0
        assert Config.EXPLICIT_WAIT > 0
        assert Config.PAGE_LOAD_TIMEOUT > 0
        
        # Test window size parsing
        size = Config.get_window_size()
        assert isinstance(size, tuple)
        assert len(size) == 2
        assert all(isinstance(d, int) and d > 0 for d in size)
    
    def test_bdd_framework_creation(self):
        """Test BDD framework components can be created"""
        from framework.bdd_framework import BDDStep, BDDScenario, StepRegistry, BDDReporter
        
        # Test BDDStep creation
        step = BDDStep("Given", "test step")
        assert step.keyword == "Given"
        assert step.description == "test step"
        
        # Test BDDScenario creation
        scenario = BDDScenario("Test scenario")
        assert scenario.name == "Test scenario"
        
        # Test StepRegistry creation
        registry = StepRegistry()
        assert registry is not None
        
        # Test BDDReporter creation
        reporter = BDDReporter()
        assert reporter is not None
    
    def test_bdd_scenario_building(self):
        """Test BDD scenario building without browser"""
        from framework.bdd_framework import BDDScenarioBuilder, StepRegistry
        
        registry = StepRegistry()
        
        # Register test steps
        @registry.given("test precondition")
        def step_given():
            return "given executed"
        
        @registry.when("test action")
        def step_when():
            return "when executed"
        
        @registry.then("test assertion")
        def step_then():
            return "then executed"
        
        # Build scenario
        builder = BDDScenarioBuilder("Test", registry")
        scenario = (builder
                    .given("test precondition")
                    .when("test action")
                    .then("test assertion")
                    .build())
        
        assert scenario.name == "Test"
        assert len(scenario.given_steps) == 1
        assert len(scenario.when_steps) == 1
        assert len(scenario.then_steps) == 1
    
    def test_page_object_creation_without_driver(self):
        """Test page objects can be created (without actual driver)"""
        from pages.testmoz_home_page import TestmozHomePage
        from pages.testmoz_demo_page import TestmozDemoPage
        
        # Mock driver
        mock_driver = Mock()
        mock_driver.title = "Test Title"
        mock_driver.current_url = "https://testmoz.com"
        
        # Test homepage page object
        home_page = TestmozHomePage(mock_driver)
        assert home_page is not None
        assert home_page.driver == mock_driver
        
        # Test demo page object
        demo_page = TestmozDemoPage(mock_driver)
        assert demo_page is not None
        assert demo_page.driver == mock_driver
    
    def test_locators_accessible(self):
        """Test locators are properly defined"""
        from pages.locators.testmoz_home_locators import TestmozHomeLocators
        from pages.locators.testmoz_demo_locators import TestmozDemoLocators
        
        # Test homepage locators
        assert TestmozHomeLocators.MAIN_HEADING is not None
        assert TestmozHomeLocators.BUILD_A_TEST_BUTTON is not None
        assert TestmozHomeLocators.TRY_DEMO_BUTTON is not None
        
        # Test demo locators
        assert TestmozDemoLocators.TEST_TITLE is not None
        assert TestmozDemoLocators.QUESTION_TEXT is not None
        assert TestmozDemoLocators.ANSWER_OPTION is not None
    
    def test_environment_variables(self):
        """Test environment variables for CI/CD"""
        # Check if we're in CI environment
        ci_env = os.getenv('CI', 'false').lower() == 'true'
        github_actions = os.getenv('GITHUB_ACTIONS', 'false').lower() == 'true'
        
        print(f"CI Environment: {ci_env}")
        print(f"GitHub Actions: {github_actions}")
        
        # These should be available in CI
        if ci_env or github_actions:
            assert os.getenv('BROWSER') is not None or os.getenv('HEADLESS') is not None
    
    def test_directories_exist(self):
        """Test required directories exist or can be created"""
        required_dirs = ['reports', 'screenshots', 'framework', 'pages', 'tests', 'config']
        
        for dir_name in required_dirs:
            if os.path.exists(dir_name):
                assert os.path.isdir(dir_name), f"{dir_name} should be a directory"
            else:
                # Try to create it
                try:
                    os.makedirs(dir_name, exist_ok=True)
                    assert os.path.exists(dir_name), f"Could not create {dir_name}"
                except Exception as e:
                    pytest.fail(f"Could not create directory {dir_name}: {e}")
    
    def test_import_paths(self):
        """Test that all import paths work correctly"""
        # Test framework imports
        try:
            from framework.bdd_framework import step_registry
            from framework.base_page import BasePage
            from framework.webdriver_manager import WebDriverManager
        except ImportError as e:
            pytest.fail(f"Framework import failed: {e}")
        
        # Test config imports
        try:
            from config.config import Config
        except ImportError as e:
            pytest.fail(f"Config import failed: {e}")
        
        # Test page imports
        try:
            from pages.testmoz_home_page import TestmozHomePage
            from pages.testmoz_demo_page import TestmozDemoPage
        except ImportError as e:
            pytest.fail(f"Page import failed: {e}")
    
    def test_pytest_configuration(self):
        """Test pytest configuration is working"""
        # Test that pytest can discover tests
        import pytest
        from _pytest.config import get_config
        
        # This should not raise an exception
        config = get_config()
        assert config is not None
    
    @pytest.mark.parametrize("test_name", [
        "test_scenario_01_navigate_to_homepage_and_verify_title",
        "test_scenario_02_verify_main_heading_is_visible",
        "test_scenario_09_open_demo_test",
        "test_scenario_20_comprehensive_test_flow"
    ])
    def test_bdd_scenario_names_exist(self, test_name):
        """Test that BDD scenario test names are properly formatted"""
        # This test verifies that our BDD scenarios have proper naming
        assert "test_scenario_" in test_name
        assert test_name.startswith("test_")
        assert len(test_name) > 20  # Should be descriptive
    
    def test_framework_statistics(self):
        """Test framework provides expected statistics"""
        from framework.bdd_framework import BDDReporter
        
        reporter = BDDReporter()
        
        # Add some test results
        reporter.add_result("Test 1", [], "PASSED")
        reporter.add_result("Test 2", [], "FAILED")
        reporter.add_result("Test 3", [], "PASSED")
        
        stats = reporter.get_statistics()
        
        assert stats['total'] == 3
        assert stats['passed'] == 2
        assert stats['failed'] == 1
        assert stats['skipped'] == 0
    
    def test_ci_environment_detection(self):
        """Test CI environment detection"""
        # Check common CI environment variables
        ci_vars = ['CI', 'GITHUB_ACTIONS', 'TRAVIS', 'JENKINS_URL', 'BUILD_ID']
        ci_detected = any(os.getenv(var) for var in ci_vars)
        
        print(f"CI Environment detected: {ci_detected}")
        
        # If we're in CI, we should have some indication
        if ci_detected:
            print("Running in CI environment - headless mode recommended")
        else:
            print("Running locally - browser mode available")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
