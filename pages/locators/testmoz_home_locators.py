from selenium.webdriver.common.by import By


class TestmozHomeLocators:
    """Locators for Testmoz Homepage"""
    
    # Main content sections
    MAIN_HEADING = (By.XPATH, "//h1[contains(text(), 'Easily create tests')]")
    SUBTITLE_TEXT = (By.XPATH, "//h2[contains(text(), 'Distribute your tests online')]")
    
    # Navigation links
    HOME_LINK = (By.LINK_TEXT, "Home")
    FEATURES_LINK = (By.LINK_TEXT, "Features")
    PRICING_LINK = (By.LINK_TEXT, "Pricing")
    FAQS_LINK = (By.LINK_TEXT, "FAQs")
    
    # Main buttons
    BUILD_A_TEST_BUTTON = (By.LINK_TEXT, "Build a Test")
    TRY_DEMO_BUTTON = (By.LINK_TEXT, "Try a Demo Test")
    WATCH_DEMO_BUTTON = (By.LINK_TEXT, "Watch a Demo")
    LOGIN_SIGNUP_BUTTON = (By.LINK_TEXT, "Login/Sign Up")
    
    # Features section
    FEATURES_HEADING = (By.XPATH, "//h1[contains(text(), 'Testmoz is (very) simple')]")
    STEP_1_HEADING = (By.XPATH, "//h2[contains(text(), '1 Adjust a few settings')]")
    STEP_2_HEADING = (By.XPATH, "//h2[contains(text(), '2 Add your questions')]")
    STEP_3_HEADING = (By.XPATH, "//h2[contains(text(), '3 Distribute the URL')]")
    
    # Results section
    RESULTS_HEADING = (By.XPATH, "//h1[contains(text(), 'And when the results are in')]")
    
    # Who uses section
    WHO_USES_HEADING = (By.XPATH, "//h1[contains(text(), 'Who uses Testmoz?')]")
    TEACHERS_SECTION = (By.XPATH, "//h2[contains(text(), 'Teachers')]")
    TRAINERS_SECTION = (By.XPATH, "//h2[contains(text(), 'Trainers')]")
    EMPLOYERS_SECTION = (By.XPATH, "//h2[contains(text(), 'Employers')]")
    
    # Features list
    FEATURES_LIST = (By.XPATH, "//ul/li")
    
    # Generic elements
    HEADER_TITLE = (By.TAG_NAME, "h1")
    SUBTITLE = (By.TAG_NAME, "h2")
