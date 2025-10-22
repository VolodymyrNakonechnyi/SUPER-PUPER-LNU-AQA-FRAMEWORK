from framework.base_page import BasePage
from pages.locators.testmoz_demo_locators import TestmozDemoLocators


class TestmozDemoPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_demo_title(self):
        """Get demo test title"""
        if self.is_element_present(TestmozDemoLocators.DEMO_TITLE):
            return self.get_text(TestmozDemoLocators.DEMO_TITLE)
        return ""
    
    def click_start_test(self):
        """Click start button to begin demo test"""
        self.click_element(TestmozDemoLocators.START_BUTTON)
    
    def get_current_question_text(self):
        """Get current question text"""
        if self.is_element_present(TestmozDemoLocators.QUESTION_TEXT):
            return self.get_text(TestmozDemoLocators.QUESTION_TEXT)
        return ""
    
    def get_current_question_number(self):
        """Get current question number"""
        if self.is_element_present(TestmozDemoLocators.QUESTION_NUMBER):
            return self.get_text(TestmozDemoLocators.QUESTION_NUMBER)
        return ""
    
    def select_radio_option(self, option_index):
        """Select radio button option by index"""
        options = self.find_elements(TestmozDemoLocators.RADIO_OPTIONS)
        if option_index < len(options):
            options[option_index].click()
    
    def select_checkbox_option(self, option_index):
        """Select checkbox option by index"""
        options = self.find_elements(TestmozDemoLocators.CHECKBOX_OPTIONS)
        if option_index < len(options):
            options[option_index].click()
    
    def enter_text_answer(self, text):
        """Enter text in text input or textarea"""
        if self.is_element_present(TestmozDemoLocators.TEXT_INPUT):
            self.send_keys(TestmozDemoLocators.TEXT_INPUT, text)
        elif self.is_element_present(TestmozDemoLocators.TEXTAREA):
            self.send_keys(TestmozDemoLocators.TEXTAREA, text)
    
    def click_next_question(self):
        """Click next button to go to next question"""
        if self.is_element_present(TestmozDemoLocators.NEXT_BUTTON):
            self.click_element(TestmozDemoLocators.NEXT_BUTTON)
            return True
        return False
    
    def click_previous_question(self):
        """Click previous button to go to previous question"""
        if self.is_element_present(TestmozDemoLocators.PREVIOUS_BUTTON):
            self.click_element(TestmozDemoLocators.PREVIOUS_BUTTON)
            return True
        return False
    
    def click_submit_test(self):
        """Click submit button to finish test"""
        if self.is_element_present(TestmozDemoLocators.SUBMIT_BUTTON):
            self.click_element(TestmozDemoLocators.SUBMIT_BUTTON)
            return True
        return False
    
    def get_progress_text(self):
        """Get progress text (e.g., 'Question 1 of 5')"""
        if self.is_element_present(TestmozDemoLocators.PROGRESS_TEXT):
            return self.get_text(TestmozDemoLocators.PROGRESS_TEXT)
        return ""
    
    def is_progress_bar_visible(self):
        """Check if progress bar is visible"""
        return self.is_element_visible(TestmozDemoLocators.PROGRESS_BAR)
    
    def get_available_answer_options(self):
        """Get count of available answer options"""
        radio_count = len(self.find_elements(TestmozDemoLocators.RADIO_OPTIONS))
        checkbox_count = len(self.find_elements(TestmozDemoLocators.CHECKBOX_OPTIONS))
        text_input_count = len(self.find_elements(TestmozDemoLocators.TEXT_INPUT))
        textarea_count = len(self.find_elements(TestmozDemoLocators.TEXTAREA))
        
        return {
            'radio_options': radio_count,
            'checkbox_options': checkbox_count,
            'text_inputs': text_input_count,
            'textareas': textarea_count
        }
    
    def is_results_page_loaded(self):
        """Check if results page is loaded"""
        return self.is_element_visible(TestmozDemoLocators.RESULTS_TITLE)
    
    def get_test_score(self):
        """Get test score from results page"""
        if self.is_element_present(TestmozDemoLocators.SCORE_DISPLAY):
            return self.get_text(TestmozDemoLocators.SCORE_DISPLAY)
        return ""
    
    def get_correct_answers_count(self):
        """Get count of correct answers"""
        correct_elements = self.find_elements(TestmozDemoLocators.CORRECT_ANSWERS)
        return len(correct_elements)
    
    def get_incorrect_answers_count(self):
        """Get count of incorrect answers"""
        incorrect_elements = self.find_elements(TestmozDemoLocators.INCORRECT_ANSWERS)
        return len(incorrect_elements)
    
    def is_test_started(self):
        """Check if test has started (question is visible)"""
        return self.is_element_visible(TestmozDemoLocators.QUESTION_TEXT)
    
    def can_navigate_to_next(self):
        """Check if next button is available"""
        return self.is_element_present(TestmozDemoLocators.NEXT_BUTTON)
    
    def can_navigate_to_previous(self):
        """Check if previous button is available"""
        return self.is_element_present(TestmozDemoLocators.PREVIOUS_BUTTON)
