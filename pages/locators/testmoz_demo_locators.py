"""
Locators for Testmoz Demo Test Page
Contains selectors for test interface, questions, answers, and results
"""
from selenium.webdriver.common.by import By


class TestmozDemoLocators:
    """Locators for Testmoz Demo Test Page"""
    
    # Test container
    TEST_CONTAINER = (By.CSS_SELECTOR, "[class*='test-container']")
    TEST_TITLE = (By.XPATH, "//h1")
    
    # Questions and answers
    QUESTION_TEXT = (By.XPATH, "//div[contains(@class, 'question')]")
    QUESTION_COUNTER = (By.XPATH, "//span[contains(text(), 'Question')]")
    ANSWER_OPTION = (By.XPATH, "//label")
    
    # Navigation buttons
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")
    PREV_BUTTON = (By.XPATH, "//button[contains(text(), 'Previous')]")
    FINISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Finish')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Submit')]")
    RETAKE_BUTTON = (By.XPATH, "//button[contains(text(), 'Retake')]")
    SHARE_BUTTON = (By.XPATH, "//button[contains(text(), 'Share')]")
    
    # Progress indicators
    PROGRESS_BAR = (By.XPATH, "//div[@class*='progress-bar']")
    PROGRESS_TEXT = (By.XPATH, "//span[@class*='progress-text']")
    
    # Results page
    RESULTS_PAGE_INDICATOR = (By.XPATH, "//h1[contains(text(), 'Results')]")
    SCORE_DISPLAY = (By.XPATH, "//span[@class*='score']")
    RESULTS_MESSAGE = (By.XPATH, "//p[@class*='message']")
    CORRECT_ANSWERS = (By.XPATH, "//li[@class*='correct']")
    INCORRECT_ANSWERS = (By.XPATH, "//li[@class*='incorrect']")
    RESULTS_TITLE = (By.XPATH, "//h1[contains(text(), 'Results')]")
    
    # Demo specific selectors (for Testmoz demo test)
    DEMO_TITLE = (By.XPATH, "//h1")
    START_BUTTON = (By.XPATH, "//button[contains(text(), 'Start')]")
    RADIO_OPTIONS = (By.XPATH, "//input[@type='radio']")
    CHECKBOX_OPTIONS = (By.XPATH, "//input[@type='checkbox']")
    TEXT_INPUT = (By.XPATH, "//input[@type='text']")
    TEXTAREA = (By.XPATH, "//textarea")
    PREVIOUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Previous')]")
