"""
Locators for Testmoz Demo Test Page
Contains selectors for test interface, questions, answers, and results
"""
from selenium.webdriver.common.by import By


class TestmozDemoLocators:
    """Locators for Testmoz Demo Test Page"""
    
    # Test container
    TEST_CONTAINER = (By.CSS_SELECTOR, "[class*='test-container']")
    TEST_TITLE = (By.XPATH, "//h1 | //h2[contains(text(), 'Untitled Test')] | //div[@class*='title']")
    
    # Questions and answers
    QUESTION_TEXT = (By.XPATH, "//div[contains(@class, 'question')] | //p[@class*='question']")
    QUESTION_COUNTER = (By.XPATH, "//span[contains(text(), 'Question')] | //div[@class*='progress']")
    ANSWER_OPTION = (By.XPATH, "//label | //div[@class*='answer'] | //input[@type='radio']/following-sibling::*")
    
    # Navigation buttons
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')] | //button[@id*='next']")
    PREV_BUTTON = (By.XPATH, "//button[contains(text(), 'Previous')] | //button[@id*='prev']")
    FINISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Finish')] | //button[contains(text(), 'Submit')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Submit')] | //button[contains(text(), 'Finish')]")
    RETAKE_BUTTON = (By.XPATH, "//button[contains(text(), 'Retake')] | //button[contains(text(), 'Try Again')]")
    SHARE_BUTTON = (By.XPATH, "//button[contains(text(), 'Share')] | //a[contains(text(), 'Share')]")
    
    # Progress indicators
    PROGRESS_BAR = (By.XPATH, "//div[@class*='progress-bar'] | //div[@class*='progress']")
    PROGRESS_TEXT = (By.XPATH, "//span[@class*='progress-text'] | //p[contains(text(), 'Question')]")
    
    # Results page
    RESULTS_PAGE_INDICATOR = (By.XPATH, "//h1[contains(text(), 'Results')] | //div[@class*='results']")
    SCORE_DISPLAY = (By.XPATH, "//span[@class*='score'] | //div[contains(text(), '%')] | //h2[contains(text(), 'Score')]")
    RESULTS_MESSAGE = (By.XPATH, "//p[@class*='message'] | //div[@class*='message']")
    CORRECT_ANSWERS = (By.XPATH, "//li[@class*='correct'] | //div[@class*='correct']")
    INCORRECT_ANSWERS = (By.XPATH, "//li[@class*='incorrect'] | //div[@class*='incorrect']")
    RESULTS_TITLE = (By.XPATH, "//h1[contains(text(), 'Results')] | //h2[contains(text(), 'Test Complete')]")
    
    # Demo specific selectors (for Testmoz demo test)
    DEMO_TITLE = (By.XPATH, "//h1 | //h2")
    START_BUTTON = (By.XPATH, "//button[contains(text(), 'Start')] | //button[contains(text(), 'Begin')]")
    RADIO_OPTIONS = (By.XPATH, "//input[@type='radio']")
    CHECKBOX_OPTIONS = (By.XPATH, "//input[@type='checkbox']")
    TEXT_INPUT = (By.XPATH, "//input[@type='text']")
    TEXTAREA = (By.XPATH, "//textarea")
    PREVIOUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Previous')]")
