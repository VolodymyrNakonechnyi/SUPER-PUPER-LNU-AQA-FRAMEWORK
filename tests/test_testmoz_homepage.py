import pytest
from framework.webdriver_manager import WebDriverManager
from pages.testmoz_home_page import TestmozHomePage


class TestTestmozHomepage:
    
    @pytest.fixture(scope="function")
    def setup(self):
        """Setup and teardown for each test"""
        driver = WebDriverManager.create_driver()
        yield driver
        driver.quit()
    
    def test_testmoz_homepage_loads(self, setup):
        """Test that Testmoz homepage loads correctly"""
        driver = setup
        testmoz_page = TestmozHomePage(driver)
        
        testmoz_page.open_testmoz()
        
        # Verify page title
        assert "Testmoz" in driver.title
        
        # Verify main heading is visible
        assert testmoz_page.is_main_heading_visible()
        
        # Verify main heading text
        main_heading = testmoz_page.get_main_heading_text()
        assert "Easily create tests" in main_heading
    
    def test_main_elements_are_visible(self, setup):
        """Test that main page elements are visible"""
        driver = setup
        testmoz_page = TestmozHomePage(driver)
        
        testmoz_page.open_testmoz()
        
        # Verify key buttons are visible
        assert testmoz_page.is_build_test_button_visible()
        assert testmoz_page.is_try_demo_button_visible()
        
        # Verify subtitle is present
        subtitle = testmoz_page.get_subtitle_text()
        assert "Distribute your tests online" in subtitle
    
    def test_navigation_links(self, setup):
        """Test navigation links functionality"""
        driver = setup
        testmoz_page = TestmozHomePage(driver)
        
        testmoz_page.open_testmoz()
        
        # Get navigation links
        nav_links = testmoz_page.get_all_navigation_links()
        
        # Verify expected navigation links are present
        expected_links = ["Home", "Features", "Pricing", "FAQs"]
        for link in expected_links:
            assert link in nav_links
    
    def test_features_section_content(self, setup):
        """Test features section content"""
        driver = setup
        testmoz_page = TestmozHomePage(driver)
        
        testmoz_page.open_testmoz()
        
        # Scroll to features section
        testmoz_page.scroll_to_features_section()
        
        # Verify features are listed
        features_count = testmoz_page.get_features_count()
        assert features_count > 0  # Should have multiple features listed
    
    def test_who_uses_section(self, setup):
        """Test 'Who uses Testmoz?' section"""
        driver = setup
        testmoz_page = TestmozHomePage(driver)
        
        testmoz_page.open_testmoz()
        
        # Scroll to who uses section
        testmoz_page.scroll_to_who_uses_section()
        
        # Verify all user types are visible
        assert testmoz_page.is_teachers_section_visible()
        assert testmoz_page.is_trainers_section_visible()
        assert testmoz_page.is_employers_section_visible()
    
    def test_build_a_test_button_click(self, setup):
        """Test 'Build a Test' button functionality"""
        driver = setup
        testmoz_page = TestmozHomePage(driver)
        
        testmoz_page.open_testmoz()
        
        # Click Build a Test button
        testmoz_page.click_build_a_test()
        
        # Verify URL changed (should redirect to test creation page)
        current_url = driver.current_url
        assert "testmoz.com" in current_url
    
    def test_try_demo_button_click(self, setup):
        """Test 'Try a Demo Test' button functionality"""
        driver = setup
        testmoz_page = TestmozHomePage(driver)
        
        testmoz_page.open_testmoz()
        
        # Click Try a Demo Test button
        testmoz_page.click_try_demo()
        
        # Verify URL changed (should redirect to demo test)
        current_url = driver.current_url
        assert "testmoz.com" in current_url
    
    def test_page_responsiveness(self, setup):
        """Test page responsiveness by checking elements are still visible after scrolling"""
        driver = setup
        testmoz_page = TestmozHomePage(driver)
        
        testmoz_page.open_testmoz()
        
        # Verify main elements are visible initially
        assert testmoz_page.is_main_heading_visible()
        assert testmoz_page.is_build_test_button_visible()
        
        # Scroll down and verify elements are still accessible
        testmoz_page.scroll_to_features_section()
        
        # Scroll back to top
        driver.execute_script("window.scrollTo(0, 0);")
        
        # Verify main elements are still visible
        assert testmoz_page.is_main_heading_visible()
        assert testmoz_page.is_build_test_button_visible()
    
    def test_page_title_and_meta(self, setup):
        """Test page title and basic meta information"""
        driver = setup
        testmoz_page = TestmozHomePage(driver)
        
        testmoz_page.open_testmoz()
        
        # Verify page title
        title = testmoz_page.get_page_title()
        assert "Testmoz" in title
        
        # Verify current URL
        current_url = driver.current_url
        assert "testmoz.com" in current_url
