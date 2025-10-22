# SUPER-PUPER-LNU-AQA-FRAMEWORK - Comprehensive Guide

## 📚 Table of Contents
1. [Framework Architecture](#framework-architecture)
2. [BDD Framework Implementation](#bdd-framework-implementation)
3. [Page Object Model](#page-object-model)
4. [Test Scenarios](#test-scenarios)
5. [Unit Tests](#unit-tests)
6. [CI/CD Integration](#cicd-integration)
7. [Extensibility Guide](#extensibility-guide)

---

## Framework Architecture

### Directory Structure Overview

```
framework/
├── base_page.py              # Base class for all page objects
├── webdriver_manager.py      # WebDriver initialization with fallbacks
└── bdd_framework.py          # Custom BDD DSL implementation

pages/
├── testmoz_home_page.py      # Homepage page object
├── testmoz_demo_page.py      # Demo test page object
└── locators/
    ├── testmoz_home_locators.py
    └── testmoz_demo_locators.py

tests/
├── test_bdd_scenarios.py     # 20 BDD test scenarios
├── test_framework_components.py # 100+ unit tests
└── ... (other test files)

config/
└── config.py                 # Environment-based configuration
```

### Core Components

1. **BasePage** - Foundation for all page objects
2. **WebDriverManager** - Robust browser initialization
3. **BDD Framework** - Custom DSL with Given-When-Then pattern
4. **Page Objects** - Testmoz-specific page interactions
5. **Locators** - Centralized element selectors

---

## BDD Framework Implementation

### Architecture

The custom BDD DSL is implemented with the following components:

#### 1. **BDDStep** - Atomic Test Step
```python
class BDDStep:
    keyword: str          # "Given", "When", "Then"
    description: str      # Step description
    func: Callable        # Step implementation
```

#### 2. **BDDScenario** - Test Scenario Container
```python
class BDDScenario:
    name: str
    given_steps: List[BDDStep]
    when_steps: List[BDDStep]
    then_steps: List[BDDStep]
    background_steps: List[BDDStep]
    data_table: Dict[str, Any]
```

#### 3. **StepRegistry** - Step Definition Registry
```python
class StepRegistry:
    given_steps: Dict[str, Callable]
    when_steps: Dict[str, Callable]
    then_steps: Dict[str, Callable]
    scenario_context: Dict[str, Any]
```

#### 4. **BDDScenarioBuilder** - Fluent API for Building Scenarios
```python
builder = BDDScenarioBuilder("Scenario Name", registry)
scenario = (builder
    .given("step description")
    .when("step description")
    .then("step description")
    .with_data({"key": "value"})
    .build())
```

#### 5. **BDDReporter** - Test Results Tracking and Reporting
```python
reporter = BDDReporter()
reporter.add_result(scenario_name, steps, "PASSED|FAILED|SKIPPED")
report = reporter.generate_report('text|json')
stats = reporter.get_statistics()
```

### Example Usage

```python
from framework.bdd_framework import StepRegistry, BDDScenarioBuilder
from pages.testmoz_home_page import TestmozHomePage

# Step 1: Create registry
registry = StepRegistry()

# Step 2: Define steps
@registry.given("user is on Testmoz homepage")
def step_open_homepage():
    page = TestmozHomePage(driver)
    page.open_testmoz()

@registry.when("user looks for main heading")
def step_check_heading():
    page = TestmozHomePage(driver)
    page.is_main_heading_visible()

@registry.then("main heading should be visible")
def step_verify_heading():
    assert page.is_main_heading_visible()

# Step 3: Build scenario using fluent API
scenario = (BDDScenarioBuilder("Homepage test", registry)
    .given("user is on Testmoz homepage")
    .when("user looks for main heading")
    .then("main heading should be visible")
    .build())

# Step 4: Execute scenario
scenario.execute()
```

### Key Features

✅ **Given-When-Then Pattern** - Gherkin-inspired syntax
✅ **Fluent API** - Chainable builder pattern
✅ **Step Registry** - Centralized step management
✅ **Context Management** - Pass data between steps
✅ **Scenario Builder** - Easy scenario construction
✅ **Flexible Reporting** - Text, JSON, HTML formats
✅ **Background Steps** - Common preconditions
✅ **Data Tables** - Parametrized test data

---

## Page Object Model

### Base Page Class

All page objects inherit from `BasePage` which provides:

```python
# Navigation
open_url(url)
go_back()
go_forward()
refresh_page()

# Element Interaction
find_element(locator)
click_element(locator)
send_keys(locator, text)
get_text(locator)
get_attribute(locator, attribute)

# Waits and Visibility
wait_for_element_visible(locator, timeout)
wait_for_element_clickable(locator, timeout)
is_element_present(locator)
is_element_visible(locator)

# Advanced
select_dropdown_by_text(locator, text)
hover_element(locator)
scroll_to_element(locator)
switch_to_frame(locator)
take_screenshot(filename)
```

### Testmoz Home Page

```python
class TestmozHomePage(BasePage):
    # Basic operations
    open_testmoz()
    get_page_title()
    get_main_heading_text()
    
    # Button interactions
    click_build_a_test()
    click_try_demo()
    click_watch_demo()
    click_login_signup()
    
    # Navigation
    click_features_link()
    click_pricing_link()
    click_faqs_link()
    
    # Visibility checks
    is_main_heading_visible()
    is_build_test_button_visible()
    is_try_demo_button_visible()
    
    # Content checks
    get_features_count()
    get_all_navigation_links()
    
    # Scrolling
    scroll_to_features_section()
    scroll_to_who_uses_section()
```

### Testmoz Demo Page

```python
class TestmozDemoPage(BasePage):
    # Test navigation
    open_demo_test()
    click_next_question()
    click_previous_question()
    click_finish_test()
    click_submit_test()
    
    # Question and answers
    get_test_title()
    get_question_text()
    get_question_number()
    get_all_answer_options()
    select_answer(answer_text)
    select_answer_by_index(index)
    
    # Progress and status
    get_progress_percentage()
    is_next_button_enabled()
    is_previous_button_enabled()
    get_question_type()
    
    # Results
    is_on_results_page()
    get_results_score()
    get_results_message()
    
    # Advanced
    answer_all_questions_randomly()
```

### Locators

Locators are centralized in `locators/` directory:

```python
from selenium.webdriver.common.by import By

class TestmozHomeLocators:
    MAIN_HEADING = (By.XPATH, "//h1[contains(text(), 'Easily create tests')]")
    BUILD_A_TEST_BUTTON = (By.LINK_TEXT, "Build a Test")
    TRY_DEMO_BUTTON = (By.LINK_TEXT, "Try a Demo Test")
    # ... more locators
```

---

## Test Scenarios

### 20 BDD Test Scenarios

#### Category 1: Homepage Scenarios (Smoke & Regression)

| # | Scenario | Type | Status |
|---|----------|------|--------|
| 1 | Navigate to homepage and verify title | Smoke | ✅ |
| 2 | Verify main heading is visible | Smoke | ✅ |
| 3 | Verify 'Build a Test' button visible | Smoke | ✅ |
| 4 | Verify 'Try Demo Test' button visible | Smoke | ✅ |
| 5 | Scroll to features section | Regression | ✅ |
| 6 | Scroll to 'Who Uses Testmoz?' section | Regression | ✅ |
| 7 | Verify navigation links present | Regression | ✅ |
| 8 | Verify subtitle text is visible | Regression | ✅ |

#### Category 2: Demo Test Scenarios (Smoke & Regression)

| # | Scenario | Type | Status |
|---|----------|------|--------|
| 9 | Open demo test | Smoke | ✅ |
| 10 | Demo test displays question | Smoke | ✅ |
| 11 | Demo test shows answer options | Smoke | ✅ |
| 12 | User can select answer | Smoke | ✅ |
| 13 | User can navigate to next question | Regression | ✅ |
| 14 | Test progress is tracked | Regression | ✅ |
| 15 | User can answer multiple questions | Regression | ✅ |
| 16 | Detect question types | Smoke | ✅ |
| 17 | Navigation buttons work consistently | Regression | ✅ |
| 18 | Random test completion | Regression | ✅ |
| 19 | Test page title not empty | Smoke | ✅ |
| 20 | Comprehensive flow (homepage → demo) | Regression | ✅ |

### Running BDD Scenarios

```bash
# All BDD scenarios
pytest tests/test_bdd_scenarios.py -v -m bdd

# Smoke tests only
pytest tests/test_bdd_scenarios.py -v -m smoke

# Regression tests only
pytest tests/test_bdd_scenarios.py -v -m regression

# Specific scenario
pytest tests/test_bdd_scenarios.py::TestBDDHomepageScenarios::test_scenario_01 -v
```

---

## Unit Tests

### Test Coverage (100+ Tests)

#### BDD Framework Tests (60+ tests)

**BDDStep Tests**
- Creation and initialization
- Function assignment
- String representation

**BDDScenario Tests**
- Scenario creation
- Adding Given/When/Then steps
- Fluent API
- Getting all steps
- Data table management

**BDDFeature Tests**
- Feature creation
- Scenario management
- Fluent API

**StepRegistry Tests**
- Step registration (Given/When/Then)
- Context storage and retrieval
- Context clearing
- Step matching (exact and pattern)
- Decorator functionality

**BDDScenarioBuilder Tests**
- Builder creation
- Fluent API
- Data table integration
- Scenario building

**BDDReporter Tests**
- Reporter creation
- Adding results
- Statistics calculation
- Text report generation
- JSON report generation

**Integration Tests**
- Complete scenario flow
- Feature with multiple scenarios
- BDD with reporter

#### Configuration Tests (5 tests)
- Configuration defaults
- Base URL validation
- Window size parsing
- Directory configuration

### Running Unit Tests

```bash
# All unit tests
pytest tests/test_framework_components.py -v

# Specific test class
pytest tests/test_framework_components.py::TestBDDStep -v

# With coverage
pytest tests/test_framework_components.py --cov=framework --cov-report=html
```

---

## CI/CD Integration

### GitHub Actions Workflow

The project includes automated CI/CD pipeline (`.github/workflows/bdd-tests.yml`):

#### Jobs

1. **Test Job**
   - Runs on Python 3.9, 3.10, 3.11
   - Executes framework unit tests
   - Runs BDD scenarios
   - Generates coverage reports
   - Uploads artifacts

2. **Security Scan Job**
   - Bandit vulnerability scanning
   - Dependency safety checking

3. **Lint Job**
   - Flake8 code linting
   - Pylint checking

#### Triggers

- Push to `main` or `develop` branches
- Pull requests
- Daily scheduled runs (2 AM UTC)

#### Artifacts Generated

- Test reports (HTML, JUnit XML)
- Coverage reports (HTML)
- Security scan results

### Setting Up CI/CD

```bash
# GitHub Actions automatically runs on push
git push origin main

# View results in Actions tab
# https://github.com/your-repo/SUPER-PUPER-LNU-AQA-FRAMEWORK/actions
```

---

## Extensibility Guide

### Adding New Test Scenarios

1. **Create new test class in `tests/test_bdd_scenarios.py`:**

```python
class TestCustomScenarios:
    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_scenario_custom(self, driver):
        """Scenario description"""
        page = YourPageObject(driver)
        
        # Given
        page.open_url()
        
        # When
        page.perform_action()
        
        # Then
        assert page.verify_result()
        reporter.add_result("Scenario name", [], "PASSED")
```

2. **Follow Given-When-Then pattern**
3. **Use Page Objects for interactions**
4. **Add reporter tracking**

### Adding New Page Objects

1. **Create locators in `pages/locators/`:**

```python
from selenium.webdriver.common.by import By

class CustomPageLocators:
    ELEMENT_1 = (By.XPATH, "//selector")
    ELEMENT_2 = (By.CSS_SELECTOR, "selector")
```

2. **Create page object in `pages/`:**

```python
from framework.base_page import BasePage
from pages.locators.custom_locators import CustomPageLocators

class CustomPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def perform_action(self):
        self.click_element(CustomPageLocators.ELEMENT_1)
    
    def verify_result(self):
        return self.is_element_visible(CustomPageLocators.ELEMENT_2)
```

### Adding New Step Definitions

```python
from framework.bdd_framework import step_registry

@step_registry.given("custom precondition")
def step_custom_given():
    # Implementation
    pass

@step_registry.when("custom action")
def step_custom_when():
    # Implementation
    pass

@step_registry.then("custom assertion")
def step_custom_then():
    # Implementation
    pass
```

### Customizing Configuration

Edit `.env` file:

```env
# Browser
BROWSER=chrome              # firefox, chrome, edge
HEADLESS=true              # true for headless mode

# Timeouts
EXPLICIT_WAIT=30
PAGE_LOAD_TIMEOUT=40

# Custom
BASE_URL=https://custom-site.com
```

---

## Performance Considerations

### Best Practices

1. **Use explicit waits** instead of implicit waits
2. **Reuse page objects** across tests
3. **Minimize page loads** where possible
4. **Use headless mode** for CI/CD
5. **Parallelize tests** with `pytest-xdist`

### Running Tests in Parallel

```bash
pytest tests/ -n auto  # Auto-detect CPU count
pytest tests/ -n 4     # Run on 4 processes
```

---

## Troubleshooting

### Common Issues

**Issue**: Tests running slowly
**Solution**: Use headless mode, increase timeouts, check network

**Issue**: Flaky tests
**Solution**: Use explicit waits, check element stability, review locators

**Issue**: Driver issues
**Solution**: Check system drivers, use fallbacks, review logs

---

## Summary

This comprehensive BDD framework provides:

✅ **Custom DSL** for readable, maintainable tests
✅ **20 BDD Scenarios** for core functionality
✅ **100+ Unit Tests** for framework validation
✅ **100% Page Object Pattern** implementation
✅ **CI/CD Integration** with GitHub Actions
✅ **Extensive Documentation** and examples
✅ **Scalable Architecture** for future expansion

The framework successfully demonstrates:
- Proper separation of concerns (Page Objects, Locators, Tests)
- Comprehensive test coverage
- Professional reporting and CI/CD
- Educational best practices in automated testing

---

**Happy Testing! 🚀**
