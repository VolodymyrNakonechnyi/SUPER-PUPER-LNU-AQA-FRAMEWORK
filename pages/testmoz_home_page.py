from framework.base_page import BasePage
from pages.locators.testmoz_home_locators import TestmozHomeLocators


class TestmozHomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_testmoz(self):
        """Open Testmoz homepage"""
        self.open_url("https://testmoz.com/")
    
    def get_page_title(self):
        """Get page title"""
        return self.driver.title
    
    def get_main_heading_text(self):
        """Get main heading text"""
        return self.get_text(TestmozHomeLocators.MAIN_HEADING)
    
    def get_subtitle_text(self):
        """Get subtitle text"""
        return self.get_text(TestmozHomeLocators.SUBTITLE_TEXT)
    
    def click_build_a_test(self):
        """Click 'Build a Test' button"""
        self.click_element(TestmozHomeLocators.BUILD_A_TEST_BUTTON)
    
    def click_try_demo(self):
        """Click 'Try a Demo Test' button"""
        self.click_element(TestmozHomeLocators.TRY_DEMO_BUTTON)
    
    def click_watch_demo(self):
        """Click 'Watch a Demo' button"""
        self.click_element(TestmozHomeLocators.WATCH_DEMO_BUTTON)
    
    def click_login_signup(self):
        """Click 'Login/Sign Up' button"""
        self.click_element(TestmozHomeLocators.LOGIN_SIGNUP_BUTTON)
    
    def click_features_link(self):
        """Click Features link in navigation"""
        self.click_element(TestmozHomeLocators.FEATURES_LINK)
    
    def click_pricing_link(self):
        """Click Pricing link in navigation"""
        self.click_element(TestmozHomeLocators.PRICING_LINK)
    
    def click_faqs_link(self):
        """Click FAQs link in navigation"""
        self.click_element(TestmozHomeLocators.FAQS_LINK)
    
    def is_main_heading_visible(self):
        """Check if main heading is visible"""
        return self.is_element_visible(TestmozHomeLocators.MAIN_HEADING)
    
    def is_build_test_button_visible(self):
        """Check if 'Build a Test' button is visible"""
        return self.is_element_visible(TestmozHomeLocators.BUILD_A_TEST_BUTTON)
    
    def is_try_demo_button_visible(self):
        """Check if 'Try a Demo Test' button is visible"""
        return self.is_element_visible(TestmozHomeLocators.TRY_DEMO_BUTTON)
    
    def get_features_count(self):
        """Get count of features listed"""
        features = self.find_elements(TestmozHomeLocators.FEATURES_LIST)
        return len(features)
    
    def scroll_to_features_section(self):
        """Scroll to features section"""
        self.scroll_to_element(TestmozHomeLocators.FEATURES_HEADING)
    
    def scroll_to_who_uses_section(self):
        """Scroll to 'Who uses Testmoz?' section"""
        self.scroll_to_element(TestmozHomeLocators.WHO_USES_HEADING)
    
    def is_teachers_section_visible(self):
        """Check if Teachers section is visible"""
        return self.is_element_visible(TestmozHomeLocators.TEACHERS_SECTION)
    
    def is_trainers_section_visible(self):
        """Check if Trainers section is visible"""
        return self.is_element_visible(TestmozHomeLocators.TRAINERS_SECTION)
    
    def is_employers_section_visible(self):
        """Check if Employers section is visible"""
        return self.is_element_visible(TestmozHomeLocators.EMPLOYERS_SECTION)
    
    def get_all_navigation_links(self):
        """Get all navigation links text"""
        nav_links = [
            TestmozHomeLocators.HOME_LINK,
            TestmozHomeLocators.FEATURES_LINK,
            TestmozHomeLocators.PRICING_LINK,
            TestmozHomeLocators.FAQS_LINK
        ]
        return [self.get_text(link) for link in nav_links if self.is_element_present(link)]
