import pytest
import os
from datetime import datetime
from framework.webdriver_manager import WebDriverManager


def pytest_configure(config):
    """Configure pytest with custom settings"""
    # Create reports directory if it doesn't exist
    os.makedirs('reports', exist_ok=True)
    os.makedirs('screenshots', exist_ok=True)
    
    # Register custom markers
    config.addinivalue_line("markers", "bdd: mark test as BDD scenario")
    config.addinivalue_line("markers", "smoke: mark test as smoke test")
    config.addinivalue_line("markers", "regression: mark test as regression test")
    config.addinivalue_line("markers", "unit: mark test as unit test")
    config.addinivalue_line("markers", "integration: mark test as integration test")


def pytest_runtest_setup(item):
    """Setup before each test"""
    print(f"\n{'='*50}")
    print(f"Starting test: {item.name}")
    print(f"{'='*50}")


def pytest_runtest_teardown(item, nextitem):
    """Teardown after each test"""
    print(f"{'='*50}")
    print(f"Finished test: {item.name}")
    print(f"{'='*50}\n")


@pytest.fixture(scope="session")
def browser_config():
    """Browser configuration fixture"""
    return {
        'browser': 'firefox',
        'headless': False,
        'window_size': '1920,1080'
    }


@pytest.fixture(scope="function")
def driver():
    """WebDriver fixture for each test"""
    driver = WebDriverManager.create_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_with_screenshot(driver):
    """WebDriver fixture with automatic screenshot on failure"""
    yield driver
    
    # Take screenshot on test failure
    if hasattr(pytest.current_test, 'failed') and pytest.current_test.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"failed_test_{timestamp}.png"
        driver.save_screenshot(f"screenshots/{screenshot_name}")
        print(f"Screenshot saved: {screenshot_name}")


def pytest_html_report_title(report):
    """Customize HTML report title"""
    report.title = "SUPER-PUPER-LNU-AQA-FRAMEWORK Test Report"
