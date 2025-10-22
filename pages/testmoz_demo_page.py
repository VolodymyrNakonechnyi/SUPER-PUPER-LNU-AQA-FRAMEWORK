"""
Page Object for Testmoz Demo Test Page
Handles test interaction, answering questions, and viewing results
"""
from framework.base_page import BasePage
from pages.locators.testmoz_demo_locators import TestmozDemoLocators
import time


class TestmozDemoPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_demo_test(self):
        """Open demo test page"""
        self.open_url("https://testmoz.com/101555")
    
    def get_test_title(self):
        """Get test title"""
        return self.get_text(TestmozDemoLocators.TEST_TITLE)
    
    def get_question_text(self):
        """Get current question text"""
        return self.get_text(TestmozDemoLocators.QUESTION_TEXT)
    
    def get_question_number(self):
        """Get current question number"""
        try:
            text = self.get_text(TestmozDemoLocators.QUESTION_COUNTER)
            # Extract number from text like "Question 1 of 5"
            import re
            match = re.search(r'(\d+)\s+of\s+(\d+)', text)
            if match:
                return {'current': int(match.group(1)), 'total': int(match.group(2))}
        except:
            return None
    
    def get_all_answer_options(self):
        """Get all available answer options"""
        options = self.find_elements(TestmozDemoLocators.ANSWER_OPTION)
        return [opt.text for opt in options]
    
    def select_answer(self, answer_text):
        """Select an answer by text"""
        options = self.find_elements(TestmozDemoLocators.ANSWER_OPTION)
        for option in options:
            if answer_text in option.text:
                option.click()
                return True
        return False
    
    def select_answer_by_index(self, index):
        """Select an answer by index"""
        options = self.find_elements(TestmozDemoLocators.ANSWER_OPTION)
        if 0 <= index < len(options):
            options[index].click()
            return True
        return False
    
    def click_next_question(self):
        """Click next question button"""
        self.click_element(TestmozDemoLocators.NEXT_BUTTON)
        time.sleep(1)  # Wait for page to load
    
    def click_previous_question(self):
        """Click previous question button"""
        self.click_element(TestmozDemoLocators.PREV_BUTTON)
        time.sleep(1)
    
    def click_finish_test(self):
        """Click finish test button"""
        self.click_element(TestmozDemoLocators.FINISH_BUTTON)
        time.sleep(2)  # Wait for results to load
    
    def click_submit_test(self):
        """Click submit test button"""
        self.click_element(TestmozDemoLocators.SUBMIT_BUTTON)
        time.sleep(2)
    
    def is_answer_selected(self, answer_index):
        """Check if an answer is selected"""
        try:
            options = self.find_elements(TestmozDemoLocators.ANSWER_OPTION)
            if 0 <= answer_index < len(options):
                return 'selected' in options[answer_index].get_attribute('class').lower()
        except:
            pass
        return False
    
    def get_results_score(self):
        """Get test results score"""
        try:
            score_text = self.get_text(TestmozDemoLocators.SCORE_DISPLAY)
            # Extract score (e.g., "Your score: 80%")
            import re
            match = re.search(r'(\d+)', score_text)
            if match:
                return int(match.group(1))
        except:
            return None
    
    def get_results_message(self):
        """Get results message"""
        return self.get_text(TestmozDemoLocators.RESULTS_MESSAGE)
    
    def is_on_results_page(self):
        """Check if on results page"""
        return self.is_element_visible(TestmozDemoLocators.RESULTS_PAGE_INDICATOR)
    
    def click_retake_test(self):
        """Click retake test button"""
        self.click_element(TestmozDemoLocators.RETAKE_BUTTON)
        time.sleep(1)
    
    def click_share_test(self):
        """Click share results button"""
        self.click_element(TestmozDemoLocators.SHARE_BUTTON)
    
    def get_progress_percentage(self):
        """Get test progress percentage"""
        try:
            progress = self.get_attribute(TestmozDemoLocators.PROGRESS_BAR, 'style')
            # Extract percentage from "width: 50%"
            import re
            match = re.search(r'(\d+)', progress)
            if match:
                return int(match.group(1))
        except:
            return 0
    
    def is_next_button_enabled(self):
        """Check if next button is enabled"""
        try:
            return 'disabled' not in self.find_element(TestmozDemoLocators.NEXT_BUTTON).get_attribute('class').lower()
        except:
            return False
    
    def is_previous_button_enabled(self):
        """Check if previous button is enabled"""
        try:
            return 'disabled' not in self.find_element(TestmozDemoLocators.PREV_BUTTON).get_attribute('class').lower()
        except:
            return False
    
    def answer_all_questions_randomly(self):
        """Answer all questions with random selections"""
        import random
        while True:
            question_info = self.get_question_number()
            if question_info:
                options = self.get_all_answer_options()
                if options:
                    random_answer = random.choice(options)
                    self.select_answer(random_answer)
                
                # Check if it's the last question
                if question_info['current'] >= question_info['total']:
                    break
                
                # Click next
                self.click_next_question()
            else:
                break
    
    def get_question_type(self):
        """Get type of current question (multiple choice, true/false, etc)"""
        options_count = len(self.get_all_answer_options())
        if options_count == 2:
            option_texts = self.get_all_answer_options()
            if 'true' in option_texts[0].lower() and 'false' in option_texts[1].lower():
                return 'true_false'
        return 'multiple_choice'
