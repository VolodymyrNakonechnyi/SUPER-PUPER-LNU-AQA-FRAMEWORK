from selenium.webdriver.common.by import By


class TestmozDemoLocators:
    """Locators for Testmoz Demo Page"""
    
    # Demo test elements
    DEMO_TITLE = (By.TAG_NAME, "h1")
    START_BUTTON = (By.XPATH, "//button[contains(text(), 'Start') or contains(text(), 'Begin')]")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")
    PREVIOUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Previous')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Submit')]")
    
    # Question elements
    QUESTION_TEXT = (By.CLASS_NAME, "question")
    QUESTION_NUMBER = (By.CLASS_NAME, "question-number")
    
    # Answer options
    RADIO_OPTIONS = (By.CSS_SELECTOR, "input[type='radio']")
    CHECKBOX_OPTIONS = (By.CSS_SELECTOR, "input[type='checkbox']")
    TEXT_INPUT = (By.CSS_SELECTOR, "input[type='text']")
    TEXTAREA = (By.TAG_NAME, "textarea")
    
    # Progress indicators
    PROGRESS_BAR = (By.CLASS_NAME, "progress")
    PROGRESS_TEXT = (By.CLASS_NAME, "progress-text")
    
    # Results page
    RESULTS_TITLE = (By.XPATH, "//h1[contains(text(), 'Results') or contains(text(), 'Score')]")
    SCORE_DISPLAY = (By.CLASS_NAME, "score")
    CORRECT_ANSWERS = (By.CLASS_NAME, "correct")
    INCORRECT_ANSWERS = (By.CLASS_NAME, "incorrect")
