"""
Unit Tests for Framework Components
Tests BDD framework, configuration, and core functionality
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
from framework.bdd_framework import (
    BDDStep, BDDScenario, BDDFeature, StepRegistry,
    BDDScenarioBuilder, BDDReporter
)
from config.config import Config


class TestBDDStep:
    """Unit tests for BDDStep class"""
    
    def test_bdd_step_creation(self):
        """Test creating a BDD step"""
        step = BDDStep("Given", "user is on homepage")
        assert step.keyword == "Given"
        assert step.description == "user is on homepage"
    
    def test_bdd_step_with_function(self):
        """Test BDD step with function"""
        def mock_func():
            return True
        
        step = BDDStep("When", "user clicks button", mock_func)
        assert step.func == mock_func
        assert step.func() is True
    
    def test_bdd_step_repr(self):
        """Test BDD step string representation"""
        step = BDDStep("Then", "page should load")
        assert str(step) == "Then page should load"


class TestBDDScenario:
    """Unit tests for BDDScenario class"""
    
    def test_scenario_creation(self):
        """Test creating a BDD scenario"""
        scenario = BDDScenario("User logs in")
        assert scenario.name == "User logs in"
        assert len(scenario.given_steps) == 0
        assert len(scenario.when_steps) == 0
        assert len(scenario.then_steps) == 0
    
    def test_add_given_step(self):
        """Test adding Given step to scenario"""
        scenario = BDDScenario("Login test")
        step = BDDStep("Given", "user is on login page")
        scenario.add_given(step)
        
        assert len(scenario.given_steps) == 1
        assert scenario.given_steps[0] == step
    
    def test_add_when_step(self):
        """Test adding When step to scenario"""
        scenario = BDDScenario("Login test")
        step = BDDStep("When", "user enters credentials")
        scenario.add_when(step)
        
        assert len(scenario.when_steps) == 1
        assert scenario.when_steps[0] == step
    
    def test_add_then_step(self):
        """Test adding Then step to scenario"""
        scenario = BDDScenario("Login test")
        step = BDDStep("Then", "user is logged in")
        scenario.add_then(step)
        
        assert len(scenario.then_steps) == 1
        assert scenario.then_steps[0] == step
    
    def test_scenario_fluent_api(self):
        """Test fluent API for building scenarios"""
        scenario = BDDScenario("Login")
        result = scenario.add_given(BDDStep("Given", "step1")).add_when(BDDStep("When", "step2"))
        
        assert result is scenario
        assert len(scenario.given_steps) == 1
        assert len(scenario.when_steps) == 1
    
    def test_get_all_steps(self):
        """Test getting all steps from scenario"""
        scenario = BDDScenario("Test")
        given = BDDStep("Given", "precondition")
        when = BDDStep("When", "action")
        then = BDDStep("Then", "assertion")
        
        scenario.add_given(given).add_when(when).add_then(then)
        
        all_steps = scenario.get_all_steps()
        assert len(all_steps) == 3
        assert all_steps[0] == given
        assert all_steps[1] == when
        assert all_steps[2] == then
    
    def test_scenario_with_data_table(self):
        """Test scenario with data table"""
        scenario = BDDScenario("Search")
        data = {"query": "python", "expected_results": 100}
        scenario.set_data_table(data)
        
        assert scenario.data_table == data


class TestBDDFeature:
    """Unit tests for BDDFeature class"""
    
    def test_feature_creation(self):
        """Test creating a BDD feature"""
        feature = BDDFeature("User Authentication", "Test auth flow")
        assert feature.name == "User Authentication"
        assert feature.description == "Test auth flow"
        assert len(feature.scenarios) == 0
    
    def test_add_scenario_to_feature(self):
        """Test adding scenario to feature"""
        feature = BDDFeature("Login")
        scenario = BDDScenario("Successful login")
        feature.add_scenario(scenario)
        
        assert len(feature.scenarios) == 1
        assert feature.scenarios[0] == scenario
    
    def test_feature_fluent_api(self):
        """Test fluent API for features"""
        feature = BDDFeature("Auth")
        scenario1 = BDDScenario("Scenario 1")
        scenario2 = BDDScenario("Scenario 2")
        
        result = feature.add_scenario(scenario1).add_scenario(scenario2)
        
        assert result is feature
        assert len(feature.scenarios) == 2


class TestStepRegistry:
    """Unit tests for StepRegistry class"""
    
    def test_registry_creation(self):
        """Test creating step registry"""
        registry = StepRegistry()
        assert len(registry.given_steps) == 0
        assert len(registry.when_steps) == 0
        assert len(registry.then_steps) == 0
    
    def test_register_given_step(self):
        """Test registering Given step"""
        registry = StepRegistry()
        
        @registry.given("user is on homepage")
        def step_func():
            return True
        
        assert "user is on homepage" in registry.given_steps
        assert registry.given_steps["user is on homepage"]() is True
    
    def test_register_when_step(self):
        """Test registering When step"""
        registry = StepRegistry()
        
        @registry.when("user clicks button")
        def step_func():
            return True
        
        assert "user clicks button" in registry.when_steps
    
    def test_register_then_step(self):
        """Test registering Then step"""
        registry = StepRegistry()
        
        @registry.then("page loads successfully")
        def step_func():
            return True
        
        assert "page loads successfully" in registry.then_steps
    
    def test_context_storage(self):
        """Test storing and retrieving context"""
        registry = StepRegistry()
        registry.set_context("user_id", 123)
        registry.set_context("username", "john")
        
        assert registry.get_context("user_id") == 123
        assert registry.get_context("username") == "john"
    
    def test_context_clear(self):
        """Test clearing context"""
        registry = StepRegistry()
        registry.set_context("key", "value")
        registry.clear_context()
        
        assert registry.get_context("key") is None
    
    def test_match_exact_step(self):
        """Test exact step matching"""
        registry = StepRegistry()
        
        def mock_func():
            pass
        
        registry.given_steps["user is on homepage"] = mock_func
        
        result = registry.match_step("Given", "user is on homepage")
        assert result == mock_func
    
    def test_match_nonexistent_step(self):
        """Test matching nonexistent step"""
        registry = StepRegistry()
        result = registry.match_step("Given", "nonexistent step")
        assert result is None


class TestBDDScenarioBuilder:
    """Unit tests for BDDScenarioBuilder class"""
    
    def test_builder_creation(self):
        """Test creating scenario builder"""
        registry = StepRegistry()
        builder = BDDScenarioBuilder("Test Scenario", registry)
        
        assert builder.registry is registry
        assert builder.scenario.name == "Test Scenario"
    
    def test_builder_fluent_api(self):
        """Test builder fluent API"""
        registry = StepRegistry()
        builder = BDDScenarioBuilder("Test", registry)
        
        result = builder.given("step1").when("step2").then("step3")
        
        assert result is builder
        assert len(builder.scenario.given_steps) == 1
        assert len(builder.scenario.when_steps) == 1
        assert len(builder.scenario.then_steps) == 1
    
    def test_builder_with_data(self):
        """Test builder with data table"""
        registry = StepRegistry()
        builder = BDDScenarioBuilder("Test", registry)
        
        data = {"key": "value"}
        builder.with_data(data)
        
        assert builder.scenario.data_table == data
    
    def test_builder_build(self):
        """Test building scenario"""
        registry = StepRegistry()
        builder = BDDScenarioBuilder("Test", registry)
        
        scenario = builder.given("step1").when("step2").build()
        
        assert isinstance(scenario, BDDScenario)
        assert scenario.name == "Test"
        assert len(scenario.given_steps) == 1


class TestBDDReporter:
    """Unit tests for BDDReporter class"""
    
    def test_reporter_creation(self):
        """Test creating reporter"""
        reporter = BDDReporter()
        assert len(reporter.results) == 0
    
    def test_add_result(self):
        """Test adding result to reporter"""
        reporter = BDDReporter()
        steps = [BDDStep("Given", "step1"), BDDStep("Then", "step2")]
        
        reporter.add_result("Scenario 1", steps, "PASSED")
        
        assert len(reporter.results) == 1
        assert reporter.results[0]['scenario'] == "Scenario 1"
        assert reporter.results[0]['status'] == "PASSED"
    
    def test_add_multiple_results(self):
        """Test adding multiple results"""
        reporter = BDDReporter()
        
        reporter.add_result("Test 1", [], "PASSED")
        reporter.add_result("Test 2", [], "FAILED")
        reporter.add_result("Test 3", [], "PASSED")
        
        assert len(reporter.results) == 3
    
    def test_get_statistics(self):
        """Test getting test statistics"""
        reporter = BDDReporter()
        
        reporter.add_result("Test 1", [], "PASSED")
        reporter.add_result("Test 2", [], "PASSED")
        reporter.add_result("Test 3", [], "FAILED")
        reporter.add_result("Test 4", [], "SKIPPED")
        
        stats = reporter.get_statistics()
        
        assert stats['total'] == 4
        assert stats['passed'] == 2
        assert stats['failed'] == 1
        assert stats['skipped'] == 1
    
    def test_generate_text_report(self):
        """Test generating text report"""
        reporter = BDDReporter()
        reporter.add_result("Test", [], "PASSED")
        
        report = reporter.generate_report('text')
        
        assert "BDD TEST REPORT" in report
        assert "Test" in report
        assert "PASSED" in report
    
    def test_generate_json_report(self):
        """Test generating JSON report"""
        reporter = BDDReporter()
        reporter.add_result("Test", [], "PASSED")
        
        report = reporter.generate_report('json')
        
        assert "Test" in report
        assert "PASSED" in report
        assert "[" in report  # JSON array format


class TestConfig:
    """Unit tests for configuration"""
    
    def test_config_defaults(self):
        """Test configuration defaults"""
        assert Config.BROWSER in ['firefox', 'chrome', 'edge']
        assert Config.IMPLICIT_WAIT > 0
        assert Config.EXPLICIT_WAIT > 0
        assert Config.PAGE_LOAD_TIMEOUT > 0
    
    def test_config_base_url(self):
        """Test base URL configuration"""
        assert "testmoz" in Config.BASE_URL.lower()
    
    def test_get_window_size(self):
        """Test window size parsing"""
        size = Config.get_window_size()
        assert isinstance(size, tuple)
        assert len(size) == 2
        assert all(isinstance(d, int) and d > 0 for d in size)
    
    def test_screenshots_directory(self):
        """Test screenshots directory is configured"""
        assert Config.SCREENSHOTS_DIR is not None
        assert len(Config.SCREENSHOTS_DIR) > 0
    
    def test_reports_directory(self):
        """Test reports directory is configured"""
        assert Config.REPORTS_DIR is not None
        assert len(Config.REPORTS_DIR) > 0


class TestBDDIntegration:
    """Integration tests for BDD framework"""
    
    def test_complete_scenario_flow(self):
        """Test complete scenario flow"""
        registry = StepRegistry()
        
        # Register steps
        call_order = []
        
        @registry.given("initial state")
        def step1():
            call_order.append("given")
        
        @registry.when("action occurs")
        def step2():
            call_order.append("when")
        
        @registry.then("result is verified")
        def step3():
            call_order.append("then")
        
        # Build scenario
        builder = BDDScenarioBuilder("Test", registry)
        scenario = (builder
                    .given("initial state")
                    .when("action occurs")
                    .then("result is verified")
                    .build())
        
        # Execute scenario
        scenario.execute()
        
        # Verify execution order
        assert call_order == ["given", "when", "then"]
    
    def test_feature_with_multiple_scenarios(self):
        """Test feature with multiple scenarios"""
        feature = BDDFeature("Authentication")
        
        scenario1 = BDDScenario("Login success")
        scenario2 = BDDScenario("Login failure")
        scenario3 = BDDScenario("Password reset")
        
        feature.add_scenario(scenario1).add_scenario(scenario2).add_scenario(scenario3)
        
        scenarios = feature.get_scenarios()
        assert len(scenarios) == 3
        assert scenarios[0].name == "Login success"
        assert scenarios[2].name == "Password reset"
    
    def test_bdd_with_reporter(self):
        """Test BDD framework with reporter"""
        reporter = BDDReporter()
        registry = StepRegistry()
        
        # Create and report scenario
        scenario = BDDScenario("Test scenario")
        scenario.add_given(BDDStep("Given", "precondition"))
        scenario.add_when(BDDStep("When", "action"))
        scenario.add_then(BDDStep("Then", "assertion"))
        
        reporter.add_result(
            scenario.name,
            scenario.get_all_steps(),
            "PASSED"
        )
        
        stats = reporter.get_statistics()
        assert stats['passed'] == 1
        assert stats['total'] == 1
