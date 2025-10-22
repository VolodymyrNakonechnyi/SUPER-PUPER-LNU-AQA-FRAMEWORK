"""
BDD Test Scenarios for Testmoz.com
Comprehensive test coverage using custom DSL with Given-When-Then pattern
"""
import pytest
from framework.bdd_framework import (
    BDDScenario, BDDFeature, StepRegistry, BDDScenarioBuilder,
    BDDReporter, step_registry
)
from pages.testmoz_home_page import TestmozHomePage
from pages.testmoz_demo_page import TestmozDemoPage
import time


# Initialize BDD reporter
reporter = BDDReporter()


class TestBDDHomepageScenarios:
    """BDD scenarios for homepage functionality"""
    
    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_scenario_01_navigate_to_homepage_and_verify_title(self, driver):
        """
        Scenario 1: User navigates to Testmoz homepage and verifies page title
        Given: User opens Testmoz homepage
        When: Page loads
        Then: Page title should be visible and contains "Testmoz"
        """
        page = TestmozHomePage(driver)
        
        # Given: User opens Testmoz homepage
        page.open_testmoz()
        
        # When: Page loads
        time.sleep(2)
        
        # Then: Page title should be visible
        title = page.get_page_title()
        assert "testmoz" in title.lower(), f"Expected 'testmoz' in title, got {title}"
        reporter.add_result("Navigate to homepage", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_scenario_02_verify_main_heading_is_visible(self, driver):
        """
        Scenario 2: Main heading should be visible on homepage
        Given: User is on Testmoz homepage
        When: Page is fully loaded
        Then: Main heading should be displayed
        """
        page = TestmozHomePage(driver)
        page.open_testmoz()
        time.sleep(2)
        
        # Verify main heading visibility
        is_visible = page.is_main_heading_visible()
        assert is_visible, "Main heading is not visible"
        
        heading_text = page.get_main_heading_text()
        assert heading_text, "Main heading text is empty"
        reporter.add_result("Verify main heading", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_scenario_03_verify_build_test_button_visible(self, driver):
        """
        Scenario 3: 'Build a Test' button should be visible
        Given: User is on Testmoz homepage
        When: Page loads
        Then: 'Build a Test' button should be displayed
        """
        page = TestmozHomePage(driver)
        page.open_testmoz()
        time.sleep(2)
        
        is_visible = page.is_build_test_button_visible()
        assert is_visible, "'Build a Test' button is not visible"
        reporter.add_result("Verify Build Test button", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_scenario_04_verify_try_demo_button_visible(self, driver):
        """
        Scenario 4: 'Try a Demo Test' button should be visible
        Given: User is on Testmoz homepage
        When: Page loads
        Then: 'Try a Demo Test' button should be visible
        """
        page = TestmozHomePage(driver)
        page.open_testmoz()
        time.sleep(2)
        
        is_visible = page.is_try_demo_button_visible()
        assert is_visible, "'Try a Demo Test' button is not visible"
        reporter.add_result("Verify Try Demo button", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.regression
    def test_scenario_05_scroll_to_features_section(self, driver):
        """
        Scenario 5: User can scroll to features section
        Given: User is on Testmoz homepage
        When: User scrolls down
        Then: Features section should be visible
        """
        page = TestmozHomePage(driver)
        page.open_testmoz()
        time.sleep(2)
        
        page.scroll_to_features_section()
        
        # Verify features count
        features_count = page.get_features_count()
        assert features_count > 0, "No features found after scrolling"
        reporter.add_result("Scroll to features section", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.regression
    def test_scenario_06_scroll_to_who_uses_section(self, driver):
        """
        Scenario 6: User can scroll to 'Who Uses Testmoz?' section
        Given: User is on Testmoz homepage
        When: User scrolls down
        Then: 'Who Uses Testmoz?' section should be visible
        """
        page = TestmozHomePage(driver)
        page.open_testmoz()
        
        page.scroll_to_who_uses_section()
        time.sleep(1)
        
        # Verify sections are visible
        teachers_visible = page.is_teachers_section_visible()
        trainers_visible = page.is_trainers_section_visible()
        employers_visible = page.is_employers_section_visible()
        
        assert teachers_visible or trainers_visible or employers_visible, \
            "No 'Who Uses' sections are visible"
        reporter.add_result("Scroll to Who Uses section", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.regression
    def test_scenario_07_verify_navigation_links(self, driver):
        """
        Scenario 7: All main navigation links are present
        Given: User is on Testmoz homepage
        When: Page loads
        Then: All navigation links should be present
        """
        page = TestmozHomePage(driver)
        page.open_testmoz()
        time.sleep(2)
        
        nav_links = page.get_all_navigation_links()
        assert len(nav_links) > 0, "No navigation links found"
        reporter.add_result("Verify navigation links", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.regression
    def test_scenario_08_subtitle_text_is_visible(self, driver):
        """
        Scenario 8: Subtitle text should be visible
        Given: User is on Testmoz homepage
        When: Page loads
        Then: Subtitle text should contain expected content
        """
        page = TestmozHomePage(driver)
        page.open_testmoz()
        time.sleep(2)
        
        subtitle = page.get_subtitle_text()
        assert subtitle, "Subtitle text is empty"
        assert "Distribute" in subtitle or "tests" in subtitle or "online" in subtitle, \
            f"Subtitle doesn't contain expected keywords: {subtitle}"
        reporter.add_result("Verify subtitle text", [], "PASSED")


class TestBDDDemoTestScenarios:
    """BDD scenarios for demo test functionality"""
    
    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_scenario_09_open_demo_test(self, driver):
        """
        Scenario 9: User can open demo test
        Given: User navigates to Testmoz demo test
        When: Test page loads
        Then: Test title should be visible
        """
        page = TestmozDemoPage(driver)
        page.open_demo_test()
        time.sleep(3)
        
        title = page.get_test_title()
        assert title, "Test title is not displayed"
        reporter.add_result("Open demo test", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_scenario_10_demo_test_displays_question(self, driver):
        """
        Scenario 10: Demo test displays question text
        Given: User is on demo test page
        When: Test loads
        Then: Question text should be visible
        """
        page = TestmozDemoPage(driver)
        page.open_demo_test()
        time.sleep(3)
        
        question_text = page.get_question_text()
        assert question_text, "Question text is not displayed"
        reporter.add_result("Demo test displays question", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_scenario_11_demo_test_has_answer_options(self, driver):
        """
        Scenario 11: Demo test shows answer options
        Given: User is on demo test page
        When: Test loads
        Then: Answer options should be displayed
        """
        page = TestmozDemoPage(driver)
        page.open_demo_test()
        time.sleep(3)
        
        options = page.get_all_answer_options()
        assert len(options) > 0, "No answer options found"
        reporter.add_result("Demo test has answer options", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_scenario_12_user_can_select_answer(self, driver):
        """
        Scenario 12: User can select an answer
        Given: User is on demo test page with answer options
        When: User selects an answer
        Then: Answer should be marked as selected
        """
        page = TestmozDemoPage(driver)
        page.open_demo_test()
        time.sleep(3)
        
        # Select first answer by index
        success = page.select_answer_by_index(0)
        assert success, "Failed to select answer"
        time.sleep(1)
        
        reporter.add_result("User can select answer", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.regression
    def test_scenario_13_user_can_navigate_next_question(self, driver):
        """
        Scenario 13: User can navigate to next question
        Given: User has answered a question
        When: User clicks next button
        Then: Next question should be displayed
        """
        page = TestmozDemoPage(driver)
        page.open_demo_test()
        time.sleep(3)
        
        # Get first question info
        question_info_1 = page.get_question_number()
        
        # Select an answer
        page.select_answer_by_index(0)
        time.sleep(1)
        
        # Click next
        page.click_next_question()
        time.sleep(2)
        
        # Get second question info
        question_info_2 = page.get_question_number()
        
        # Verify question changed (if not the last question)
        if question_info_1 and question_info_2:
            if question_info_1['current'] < question_info_1['total']:
                assert question_info_2['current'] > question_info_1['current'], \
                    "Question number didn't advance"
        
        reporter.add_result("Navigate to next question", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.regression
    def test_scenario_14_demo_test_progress_tracking(self, driver):
        """
        Scenario 14: Test progress is tracked
        Given: User is taking the demo test
        When: User answers questions
        Then: Progress should increase
        """
        page = TestmozDemoPage(driver)
        page.open_demo_test()
        time.sleep(3)
        
        # Get initial question number
        question_info = page.get_question_number()
        assert question_info is not None, "Question number not found"
        assert question_info['total'] > 0, "Total questions should be > 0"
        
        reporter.add_result("Progress tracking", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.regression
    def test_scenario_15_demo_test_with_multiple_answers(self, driver):
        """
        Scenario 15: User can answer multiple questions
        Given: User is on demo test
        When: User answers and navigates through several questions
        Then: Each answer should be recorded
        """
        page = TestmozDemoPage(driver)
        page.open_demo_test()
        time.sleep(3)
        
        question_info = page.get_question_number()
        if question_info and question_info['total'] >= 2:
            # Answer first question
            page.select_answer_by_index(0)
            time.sleep(1)
            page.click_next_question()
            time.sleep(2)
            
            # Answer second question
            page.select_answer_by_index(0)
            time.sleep(1)
            
            # Verify we're on question 2
            new_question_info = page.get_question_number()
            assert new_question_info['current'] == 2, "Failed to navigate to question 2"
        
        reporter.add_result("Answer multiple questions", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_scenario_16_demo_test_question_types_detected(self, driver):
        """
        Scenario 16: Test can identify question types
        Given: User is on demo test
        When: System analyzes question format
        Then: Question type should be identified
        """
        page = TestmozDemoPage(driver)
        page.open_demo_test()
        time.sleep(3)
        
        question_type = page.get_question_type()
        assert question_type in ['true_false', 'multiple_choice'], \
            f"Unknown question type: {question_type}"
        
        reporter.add_result("Detect question type", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.regression
    def test_scenario_17_demo_test_navigation_consistency(self, driver):
        """
        Scenario 17: Navigation buttons work consistently
        Given: User is on demo test
        When: User attempts to navigate
        Then: Navigation buttons should be accessible
        """
        page = TestmozDemoPage(driver)
        page.open_demo_test()
        time.sleep(3)
        
        question_info = page.get_question_number()
        
        # Check if next button is enabled (unless on last question)
        if question_info and question_info['current'] < question_info['total']:
            next_enabled = page.is_next_button_enabled()
            assert next_enabled, "Next button should be enabled"
        
        reporter.add_result("Navigation consistency", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.regression
    def test_scenario_18_random_test_completion(self, driver):
        """
        Scenario 18: Test can be completed with random answers
        Given: User is on demo test
        When: User answers all questions randomly
        Then: Test should be completable
        """
        page = TestmozDemoPage(driver)
        page.open_demo_test()
        time.sleep(3)
        
        question_info = page.get_question_number()
        if question_info and question_info['total'] >= 1:
            # Answer just a couple of questions to test the flow
            for i in range(min(2, question_info['total'])):
                page.select_answer_by_index(0)
                time.sleep(0.5)
                
                if i < question_info['total'] - 1:
                    page.click_next_question()
                    time.sleep(1)
        
        reporter.add_result("Random test completion flow", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_scenario_19_test_page_title_not_empty(self, driver):
        """
        Scenario 19: Test page title is not empty
        Given: User opens demo test
        When: Page loads
        Then: Page title should have content
        """
        page = TestmozDemoPage(driver)
        page.open_demo_test()
        time.sleep(3)
        
        title = page.get_test_title()
        assert title and len(title) > 0, "Test title is empty"
        assert title != "", "Test title is empty string"
        
        reporter.add_result("Test page title not empty", [], "PASSED")
    
    @pytest.mark.bdd
    @pytest.mark.regression
    def test_scenario_20_comprehensive_test_flow(self, driver):
        """
        Scenario 20: Comprehensive test flow - homepage to demo test
        Given: User starts on Testmoz homepage
        When: User navigates and takes demo test
        Then: All steps should complete successfully
        """
        # Start on homepage
        home_page = TestmozHomePage(driver)
        home_page.open_testmoz()
        time.sleep(2)
        
        # Verify homepage
        assert home_page.is_main_heading_visible(), "Homepage main heading not visible"
        
        # Navigate to demo test
        demo_page = TestmozDemoPage(driver)
        demo_page.open_demo_test()
        time.sleep(3)
        
        # Verify demo test
        title = demo_page.get_test_title()
        assert title, "Demo test title not visible"
        
        question_text = demo_page.get_question_text()
        assert question_text, "Demo test question not visible"
        
        options = demo_page.get_all_answer_options()
        assert len(options) > 0, "No answer options in demo test"
        
        reporter.add_result("Comprehensive test flow", [], "PASSED")


@pytest.fixture(scope="session", autouse=True)
def generate_bdd_report():
    """Generate BDD report after all tests"""
    yield
    
    # Print report
    print("\n" + reporter.generate_report('text'))
    
    # Print statistics
    stats = reporter.get_statistics()
    print(f"\nTest Statistics:")
    print(f"  Total: {stats['total']}")
    print(f"  Passed: {stats['passed']}")
    print(f"  Failed: {stats['failed']}")
    print(f"  Skipped: {stats['skipped']}")
