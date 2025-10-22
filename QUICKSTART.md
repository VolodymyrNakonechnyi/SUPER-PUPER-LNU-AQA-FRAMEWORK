# Quick Start Guide - SUPER-PUPER-LNU-AQA-FRAMEWORK

## ⚡ 5-Minute Setup

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create Configuration File
```bash
# Create .env file in project root
echo "BROWSER=firefox" > .env
echo "HEADLESS=false" >> .env
echo "BASE_URL=https://testmoz.com" >> .env
```

### 3. Run Your First Test
```bash
# Run all 20 BDD scenarios
pytest tests/test_bdd_scenarios.py -v

# Or run just smoke tests
pytest tests/test_bdd_scenarios.py -v -m smoke
```

### 4. View Reports
```bash
# Reports are generated in reports/ directory
# Open in browser
reports/report.html
```

---

## 🚀 Common Commands

### Run BDD Tests
```bash
# All BDD scenarios
pytest tests/test_bdd_scenarios.py -v

# Smoke tests only (fast)
pytest tests/test_bdd_scenarios.py -v -m smoke

# Regression tests
pytest tests/test_bdd_scenarios.py -v -m regression

# Single scenario
pytest tests/test_bdd_scenarios.py::TestBDDHomepageScenarios::test_scenario_01 -v
```

### Run Unit Tests
```bash
# All framework unit tests (100+)
pytest tests/test_framework_components.py -v

# With coverage
pytest tests/test_framework_components.py --cov=framework --cov-report=html

# Specific test class
pytest tests/test_framework_components.py::TestBDDStep -v
```

### Run All Tests
```bash
pytest tests/ -v
pytest tests/ --html=reports/full_report.html --self-contained-html
```

### Use Different Browsers
```bash
# Set in .env
BROWSER=chrome    # or firefox, edge

# Or pass via CLI (requires modifying run script)
```

---

## 📊 What Gets Generated?

After running tests, you'll find:

```
reports/
├── report.html           # Main test report
├── bdd_tests.html        # BDD scenario results
├── framework_tests.html  # Unit test results
├── junit.xml             # JUnit format
└── allure-results/       # Allure report data

htmlcov/                  # Code coverage report
├── index.html
└── (coverage details)

screenshots/              # Failed test screenshots (auto-generated)
```

---

## 💡 Framework Overview

### BDD DSL (Custom Domain-Specific Language)
```python
# Write tests like this:
def test_homepage(driver):
    page = TestmozHomePage(driver)
    
    # Given
    page.open_testmoz()
    
    # When
    time.sleep(2)
    
    # Then
    assert page.is_main_heading_visible()
```

### Page Objects
```python
# Interact with pages cleanly
page = TestmozHomePage(driver)
page.click_build_a_test()
page.scroll_to_features_section()
assert page.get_features_count() > 0
```

### 20 BDD Test Scenarios
- ✅ 8 Homepage scenarios
- ✅ 12 Demo test scenarios
- ✅ Smoke and Regression marked
- ✅ Full coverage of requirements

### 100+ Unit Tests
- ✅ BDD framework component tests
- ✅ Configuration tests
- ✅ Integration tests
- ✅ High code coverage

---

## 🔧 Troubleshooting

### Browser not opening?
```bash
# Check if Firefox is installed
which geckodriver          # Mac/Linux
where geckodriver          # Windows

# If not found, install it
brew install geckodriver   # Mac
# Or download from: https://github.com/mozilla/geckodriver/releases
```

### Tests running too slowly?
```bash
# Try headless mode in .env
HEADLESS=true

# Or use Chrome instead of Firefox
BROWSER=chrome
```

### Elements not found?
```bash
# Increase timeouts in .env
EXPLICIT_WAIT=30
PAGE_LOAD_TIMEOUT=40
```

---

## 📈 Next Steps

1. **Explore BDD Scenarios**
   - Check `tests/test_bdd_scenarios.py`
   - Review 20 different test scenarios

2. **Review Unit Tests**
   - Check `tests/test_framework_components.py`
   - 100+ tests covering all components

3. **Create Your Tests**
   - Add tests to `tests/` directory
   - Use Page Objects from `pages/`
   - Follow Given-When-Then pattern

4. **Extend Framework**
   - Add new Page Objects
   - Create custom locators
   - Define new step definitions

---

## 📚 Documentation

- **README.md** - Full documentation
- **FRAMEWORK_GUIDE.md** - Detailed architecture guide
- **QUICKSTART.md** - This file

---

## ✅ Verification Checklist

- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] .env file created
- [ ] Can run `pytest tests/test_bdd_scenarios.py -v`
- [ ] HTML report generated in `reports/`
- [ ] No browser errors in console

---

## 🎓 Learning Path

1. **Beginners**: Start with Smoke Tests
   ```bash
   pytest tests/test_bdd_scenarios.py -v -m smoke
   ```

2. **Intermediate**: Read Framework Guide
   - Understand BDD DSL
   - Review Page Objects
   - Study test structure

3. **Advanced**: Create Custom Tests
   - Add new page objects
   - Write custom scenarios
   - Extend framework

---

## 🆘 Help & Support

**Issue**: Import errors
**Solution**: Run `pip install -r requirements.txt` again

**Issue**: Pytest not found
**Solution**: Run `pip install pytest`

**Issue**: Tests fail on Windows
**Solution**: Use Firefox (set `BROWSER=firefox` in .env)

---

## 🚀 You're Ready!

```bash
# Start with smoke tests
pytest tests/test_bdd_scenarios.py -v -m smoke

# Then explore everything
pytest tests/ -v

# Generate full report
pytest tests/ --html=reports/report.html --self-contained-html
```

**Happy Testing! 🎉**
