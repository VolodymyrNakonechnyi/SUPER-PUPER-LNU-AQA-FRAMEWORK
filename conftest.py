import pytest
import os
from datetime import datetime
from framework.webdriver_manager import WebDriverManager


def pytest_configure(config):
    """Configure pytest with custom settings"""
    # Create reports directory if it doesn't exist
    os.makedirs('reports', exist_ok=True)
    os.makedirs('screenshots', exist_ok=True)


def pytest_runtest_setup(item):
    """Setup before each test"""
    print(f"\n=== Starting test: {item.name} ===")


def pytest_runtest_teardown(item, nextitem):
    """Teardown after each test"""
    print(f"=== Finished test: {item.name} ===")


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
    report.title = "Selenium Test Report"
