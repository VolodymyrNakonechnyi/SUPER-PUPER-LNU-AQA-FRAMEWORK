"""
Extended test suite with 70+ additional tests for comprehensive coverage
"""

import pytest
from framework.bdd_framework import BDDStep, BDDScenario, BDDFeature, StepRegistry, BDDScenarioBuilder, BDDReporter
from config.config import Config


class TestBDDStepExtended:
    """Extended tests for BDDStep class - 10 tests"""
    
    def test_step_creation_basic(self):
        step = BDDStep("Given", "user is ready")
        assert step.keyword == "Given"
        assert step.description == "user is ready"
    
    def test_step_with_function(self):
        func = lambda: "test"
        step = BDDStep("When", "action", func)
        assert step.func == func
        assert step.func() == "test"
    
    def test_step_repr_format(self):
        step = BDDStep("Given", "test step")
        assert "Given" in repr(step)
        assert "test step" in repr(step)
    
    def test_step_with_long_description(self):
        long_desc = "a" * 500
        step = BDDStep("When", long_desc)
        assert len(step.description) == 500
    
    def test_step_with_special_chars(self):
        step = BDDStep("Then", "User enters @#$%^&*()")
        assert "@#$%^&*()" in step.description
    
    def test_step_with_unicode(self):
        step = BDDStep("Given", "Користувач тест 测试")
        assert "тест" in step.description
    
    def test_step_with_numbers(self):
        step = BDDStep("When", "User enters 12345 items")
        assert "12345" in step.description
    
    def test_step_function_callable(self):
        def test_func():
            return "result"
        step = BDDStep("Given", "setup", test_func)
        assert callable(step.func)
        assert step.func() == "result"
    
    def test_step_function_exception(self):
        def error_func():
            raise RuntimeError("Test")
        step = BDDStep("Then", "verify", error_func)
        with pytest.raises(RuntimeError):
            step.func()
    
    def test_step_no_function(self):
        step = BDDStep("When", "no func")
        assert step.func is None


class TestBDDScenarioExtended:
    """Extended tests for BDDScenario - 15 tests"""
    
    def test_scenario_creation(self):
        scenario = BDDScenario("Test scenario")
        assert scenario.name == "Test scenario"
        assert len(scenario.get_all_steps()) == 0
    
    def test_scenario_add_given_steps(self):
        scenario = BDDScenario("S1")
        step = BDDStep("Given", "precondition")
        scenario.add_given(step)
        assert len(scenario.given_steps) == 1
    
    def test_scenario_add_when_steps(self):
        scenario = BDDScenario("S1")
        step = BDDStep("When", "action")
        scenario.add_when(step)
        assert len(scenario.when_steps) == 1
    
    def test_scenario_add_then_steps(self):
        scenario = BDDScenario("S1")
        step = BDDStep("Then", "assertion")
        scenario.add_then(step)
        assert len(scenario.then_steps) == 1
    
    def test_scenario_fluent_api(self):
        scenario = BDDScenario("Fluent")
        result = scenario.add_given(BDDStep("Given", "step1"))
        assert result is scenario
    
    def test_scenario_all_steps_count(self):
        scenario = BDDScenario("Multi")
        scenario.add_given(BDDStep("Given", "g1"))
        scenario.add_when(BDDStep("When", "w1"))
        scenario.add_then(BDDStep("Then", "t1"))
        assert len(scenario.get_all_steps()) == 3
    
    def test_scenario_step_order(self):
        scenario = BDDScenario("Order")
        scenario.add_background(BDDStep("Background", "bg"))
        scenario.add_given(BDDStep("Given", "g"))
        scenario.add_when(BDDStep("When", "w"))
        scenario.add_then(BDDStep("Then", "t"))
        steps = scenario.get_all_steps()
        assert steps[0].keyword == "Background"
        assert steps[1].keyword == "Given"
    
    def test_scenario_data_table(self):
        scenario = BDDScenario("Data")
        data = {"col1": "val1", "col2": "val2"}
        scenario.set_data_table(data)
        assert scenario.data_table == data
    
    def test_scenario_data_table_multiple_sets(self):
        scenario = BDDScenario("Data2")
        data1 = {"a": "1"}
        data2 = {"b": "2"}
        scenario.set_data_table(data1)
        scenario.set_data_table(data2)
        assert scenario.data_table == data2
    
    def test_scenario_many_given_steps(self):
        scenario = BDDScenario("ManyG")
        for i in range(10):
            scenario.add_given(BDDStep("Given", f"step_{i}"))
        assert len(scenario.given_steps) == 10
    
    def test_scenario_many_when_steps(self):
        scenario = BDDScenario("ManyW")
        for i in range(10):
            scenario.add_when(BDDStep("When", f"action_{i}"))
        assert len(scenario.when_steps) == 10
    
    def test_scenario_many_then_steps(self):
        scenario = BDDScenario("ManyT")
        for i in range(10):
            scenario.add_then(BDDStep("Then", f"verify_{i}"))
        assert len(scenario.then_steps) == 10
    
    def test_scenario_execute_steps(self):
        executed = []
        def func1():
            executed.append(1)
        def func2():
            executed.append(2)
        scenario = BDDScenario("Exec")
        scenario.add_given(BDDStep("Given", "g", func1))
        scenario.add_when(BDDStep("When", "w", func2))
        scenario.execute()
        assert executed == [1, 2]
    
    def test_scenario_fluent_chain(self):
        s = BDDScenario("Chain")
        result = (s
                 .add_given(BDDStep("Given", "g"))
                 .add_when(BDDStep("When", "w"))
                 .add_then(BDDStep("Then", "t")))
        assert result is s
        assert len(s.get_all_steps()) == 3


class TestBDDFeatureExtended:
    """Extended tests for BDDFeature - 10 tests"""
    
    def test_feature_creation(self):
        feature = BDDFeature("Feature1")
        assert feature.name == "Feature1"
        assert len(feature.scenarios) == 0
    
    def test_feature_with_description(self):
        feature = BDDFeature("F", "Test description")
        assert feature.description == "Test description"
    
    def test_feature_add_scenario(self):
        feature = BDDFeature("F")
        scenario = BDDScenario("S1")
        feature.add_scenario(scenario)
        assert len(feature.scenarios) == 1
    
    def test_feature_fluent_api(self):
        feature = BDDFeature("F")
        result = feature.add_scenario(BDDScenario("S"))
        assert result is feature
    
    def test_feature_multiple_scenarios(self):
        feature = BDDFeature("F")
        for i in range(5):
            feature.add_scenario(BDDScenario(f"S{i}"))
        assert len(feature.scenarios) == 5
    
    def test_feature_get_scenarios(self):
        feature = BDDFeature("F")
        s1 = BDDScenario("S1")
        s2 = BDDScenario("S2")
        feature.add_scenario(s1)
        feature.add_scenario(s2)
        scenarios = feature.get_scenarios()
        assert scenarios[0] is s1
        assert scenarios[1] is s2
    
    def test_feature_scenario_order_preserved(self):
        feature = BDDFeature("F")
        for i in range(10):
            feature.add_scenario(BDDScenario(f"S{i}"))
        assert feature.scenarios[0].name == "S0"
        assert feature.scenarios[9].name == "S9"
    
    def test_feature_many_scenarios(self):
        feature = BDDFeature("BigF")
        for i in range(50):
            feature.add_scenario(BDDScenario(f"S{i}"))
        assert len(feature.scenarios) == 50
    
    def test_feature_fluent_chain(self):
        f = BDDFeature("F")
        result = (f
                 .add_scenario(BDDScenario("S1"))
                 .add_scenario(BDDScenario("S2")))
        assert result is f
        assert len(f.scenarios) == 2
    
    def test_feature_scenario_retrieval(self):
        feature = BDDFeature("F")
        s = BDDScenario("S")
        feature.add_scenario(s)
        assert feature.scenarios[0] is s


class TestStepRegistryExtended:
    """Extended tests for StepRegistry - 15 tests"""
    
    def test_registry_creation(self):
        registry = StepRegistry()
        assert len(registry.given_steps) == 0
        assert len(registry.when_steps) == 0
        assert len(registry.then_steps) == 0
    
    def test_registry_given_decorator(self):
        registry = StepRegistry()
        @registry.given("user is ready")
        def step():
            pass
        assert "user is ready" in registry.given_steps
    
    def test_registry_when_decorator(self):
        registry = StepRegistry()
        @registry.when("action performed")
        def step():
            pass
        assert "action performed" in registry.when_steps
    
    def test_registry_then_decorator(self):
        registry = StepRegistry()
        @registry.then("result verified")
        def step():
            pass
        assert "result verified" in registry.then_steps
    
    def test_registry_context_set_get(self):
        registry = StepRegistry()
        registry.set_context("key", "value")
        assert registry.get_context("key") == "value"
    
    def test_registry_context_multiple(self):
        registry = StepRegistry()
        for i in range(10):
            registry.set_context(f"key{i}", f"val{i}")
        for i in range(10):
            assert registry.get_context(f"key{i}") == f"val{i}"
    
    def test_registry_context_clear(self):
        registry = StepRegistry()
        registry.set_context("k1", "v1")
        registry.set_context("k2", "v2")
        registry.clear_context()
        assert registry.get_context("k1") is None
        assert registry.get_context("k2") is None
    
    def test_registry_match_step_exact(self):
        registry = StepRegistry()
        @registry.given("user ready")
        def func():
            return "ok"
        match = registry.match_step("Given", "user ready")
        assert match is not None
    
    def test_registry_match_step_not_found(self):
        registry = StepRegistry()
        match = registry.match_step("Given", "nonexistent")
        assert match is None
    
    def test_registry_many_given_steps(self):
        registry = StepRegistry()
        for i in range(20):
            registry.given(f"step_{i}")(lambda: None)
        assert len(registry.given_steps) == 20
    
    def test_registry_many_when_steps(self):
        registry = StepRegistry()
        for i in range(20):
            registry.when(f"action_{i}")(lambda: None)
        assert len(registry.when_steps) == 20
    
    def test_registry_many_then_steps(self):
        registry = StepRegistry()
        for i in range(20):
            registry.then(f"verify_{i}")(lambda: None)
        assert len(registry.then_steps) == 20
    
    def test_registry_context_isolation(self):
        r1 = StepRegistry()
        r2 = StepRegistry()
        r1.set_context("k", "v1")
        r2.set_context("k", "v2")
        assert r1.get_context("k") == "v1"
        assert r2.get_context("k") == "v2"
    
    def test_registry_callable_step(self):
        registry = StepRegistry()
        @registry.given("test")
        def func():
            return "result"
        assert callable(registry.given_steps["test"])


class TestBDDScenarioBuilderExtended:
    """Extended tests for BDDScenarioBuilder - 12 tests"""
    
    def test_builder_creation(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("Test", registry)
        assert builder.scenario.name == "Test"
    
    def test_builder_given(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("B", registry)
        builder.given("step")
        assert len(builder.scenario.given_steps) == 1
    
    def test_builder_when(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("B", registry)
        builder.when("action")
        assert len(builder.scenario.when_steps) == 1
    
    def test_builder_then(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("B", registry)
        builder.then("result")
        assert len(builder.scenario.then_steps) == 1
    
    def test_builder_background(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("B", registry)
        builder.background("bg")
        assert len(builder.scenario.background_steps) == 1
    
    def test_builder_with_data(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("B", registry)
        data = {"col": "val"}
        builder.with_data(data)
        assert builder.scenario.data_table == data
    
    def test_builder_build(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("B", registry)
        scenario = builder.build()
        assert isinstance(scenario, BDDScenario)
        assert scenario.name == "B"
    
    def test_builder_fluent_chain(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("Chain", registry)
        result = (builder
                 .given("g")
                 .when("w")
                 .then("t"))
        assert result is builder
        assert len(builder.scenario.get_all_steps()) == 3
    
    def test_builder_multiple_given(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("B", registry)
        builder.given("g1").given("g2").given("g3")
        assert len(builder.scenario.given_steps) == 3
    
    def test_builder_multiple_when(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("B", registry)
        builder.when("a1").when("a2").when("a3")
        assert len(builder.scenario.when_steps) == 3
    
    def test_builder_multiple_then(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("B", registry)
        builder.then("t1").then("t2").then("t3")
        assert len(builder.scenario.then_steps) == 3
    
    def test_builder_complex_scenario(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("Complex", registry)
        builder.background("bg")
        builder.given("g1").given("g2")
        builder.when("w1").when("w2")
        builder.then("t1").then("t2")
        scenario = builder.build()
        assert len(scenario.get_all_steps()) == 7


class TestBDDReporterExtended:
    """Extended tests for BDDReporter - 10 tests"""
    
    def test_reporter_creation(self):
        reporter = BDDReporter()
        assert len(reporter.results) == 0
    
    def test_reporter_add_result(self):
        reporter = BDDReporter()
        steps = [BDDStep("Given", "g")]
        reporter.add_result("scenario", steps, "PASSED")
        assert len(reporter.results) == 1
    
    def test_reporter_result_content(self):
        reporter = BDDReporter()
        steps = [BDDStep("Given", "step1")]
        reporter.add_result("test", steps, "FAILED", "error msg")
        result = reporter.results[0]
        assert result["scenario"] == "test"
        assert result["status"] == "FAILED"
        assert result["error"] == "error msg"
    
    def test_reporter_many_results(self):
        reporter = BDDReporter()
        for i in range(20):
            steps = [BDDStep("Given", f"step{i}")]
            reporter.add_result(f"scenario{i}", steps, "PASSED")
        assert len(reporter.results) == 20
    
    def test_reporter_statistics_passed(self):
        reporter = BDDReporter()
        for i in range(5):
            steps = []
            reporter.add_result(f"s{i}", steps, "PASSED")
        stats = reporter.get_statistics()
        assert stats["passed"] == 5
        assert stats["total"] == 5
    
    def test_reporter_statistics_mixed(self):
        reporter = BDDReporter()
        reporter.add_result("s1", [], "PASSED")
        reporter.add_result("s2", [], "FAILED")
        reporter.add_result("s3", [], "SKIPPED")
        stats = reporter.get_statistics()
        assert stats["passed"] == 1
        assert stats["failed"] == 1
        assert stats["skipped"] == 1
    
    def test_reporter_text_report(self):
        reporter = BDDReporter()
        steps = [BDDStep("Given", "step")]
        reporter.add_result("scenario", steps, "PASSED")
        report = reporter.generate_report("text")
        assert isinstance(report, str)
        assert "PASSED" in report
    
    def test_reporter_json_report(self):
        reporter = BDDReporter()
        steps = [BDDStep("Given", "step")]
        reporter.add_result("test", steps, "PASSED")
        report = reporter.generate_report("json")
        assert isinstance(report, str)
        assert "test" in report
    
    def test_reporter_text_with_error(self):
        reporter = BDDReporter()
        steps = []
        reporter.add_result("fail_test", steps, "FAILED", "Error occurred")
        report = reporter.generate_report("text")
        assert "Error occurred" in report
    
    def test_reporter_multiple_scenarios(self):
        reporter = BDDReporter()
        for i in range(10):
            steps = [BDDStep("Given", f"g{i}")]
            reporter.add_result(f"s{i}", steps, "PASSED")
        stats = reporter.get_statistics()
        assert stats["total"] == 10


class TestConfigExtended:
    """Extended tests for Config - 8 tests"""
    
    def test_config_browser_property(self):
        assert hasattr(Config, 'BROWSER')
        assert Config.BROWSER in ["firefox", "chrome", "edge"]
    
    def test_config_headless_property(self):
        assert hasattr(Config, 'HEADLESS')
        assert isinstance(Config.HEADLESS, bool)
    
    def test_config_window_size_parsing(self):
        width, height = Config.get_window_size()
        assert width > 0
        assert height > 0
        assert isinstance(width, int)
        assert isinstance(height, int)
    
    def test_config_timeouts_positive(self):
        assert Config.IMPLICIT_WAIT > 0
        assert Config.EXPLICIT_WAIT > 0
        assert Config.PAGE_LOAD_TIMEOUT > 0
    
    def test_config_base_url_defined(self):
        assert Config.BASE_URL != ""
        assert "http" in Config.BASE_URL.lower()
    
    def test_config_directories_defined(self):
        assert Config.SCREENSHOTS_DIR == "screenshots"
        assert Config.REPORTS_DIR == "reports"
    
    def test_config_window_size_default(self):
        w, h = Config.get_window_size()
        assert (w, h) == (1920, 1080)
    
    def test_config_all_attributes(self):
        attrs = ['BROWSER', 'HEADLESS', 'WINDOW_SIZE', 'IMPLICIT_WAIT', 
                'EXPLICIT_WAIT', 'PAGE_LOAD_TIMEOUT', 'BASE_URL', 
                'SCREENSHOTS_DIR', 'REPORTS_DIR']
        for attr in attrs:
            assert hasattr(Config, attr)


class TestIntegrationScenarios:
    """Integration tests combining multiple components - 8 tests"""
    
    def test_full_scenario_flow(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("Full Flow", registry)
        scenario = builder.given("g").when("w").then("t").build()
        assert len(scenario.get_all_steps()) == 3
    
    def test_feature_with_multiple_scenarios(self):
        feature = BDDFeature("Feature")
        for i in range(3):
            s = BDDScenario(f"S{i}")
            s.add_given(BDDStep("Given", f"g{i}"))
            feature.add_scenario(s)
        assert len(feature.scenarios) == 3
    
    def test_reporter_full_scenario(self):
        reporter = BDDReporter()
        for i in range(5):
            steps = [BDDStep("Given", f"s{i}")]
            reporter.add_result(f"test{i}", steps, "PASSED")
        stats = reporter.get_statistics()
        assert stats["passed"] == 5
        report = reporter.generate_report("text")
        assert len(report) > 0
    
    def test_builder_with_registry(self):
        registry = StepRegistry()
        @registry.given("precondition")
        def precond():
            return "ready"
        builder = BDDScenarioBuilder("Test", registry)
        builder.given("precondition")
        scenario = builder.build()
        assert len(scenario.given_steps) == 1
    
    def test_complex_scenario_with_data(self):
        registry = StepRegistry()
        builder = BDDScenarioBuilder("Data test", registry)
        data = {"user": "alice", "role": "admin"}
        builder.with_data(data)
        builder.given("user exists").when("login").then("success")
        scenario = builder.build()
        assert scenario.data_table == data
        assert len(scenario.get_all_steps()) == 3
    
    def test_feature_scenarios_execution(self):
        feature = BDDFeature("Execute")
        executed = []
        def f1(): executed.append(1)
        def f2(): executed.append(2)
        
        s = BDDScenario("S")
        s.add_given(BDDStep("Given", "g", f1))
        s.add_when(BDDStep("When", "w", f2))
        feature.add_scenario(s)
        
        feature.scenarios[0].execute()
        assert executed == [1, 2]
    
    def test_multiple_registries_isolation(self):
        r1 = StepRegistry()
        r2 = StepRegistry()
        
        @r1.given("step1")
        def f1(): pass
        
        @r2.given("step2")
        def f2(): pass
        
        assert "step1" in r1.given_steps
        assert "step1" not in r2.given_steps
    
    def test_builder_scenario_execution(self):
        registry = StepRegistry()
        executed = []
        
        @registry.given("setup")
        def setup():
            executed.append("setup")
        
        @registry.when("action")
        def action():
            executed.append("action")
        
        builder = BDDScenarioBuilder("Exec", registry)
        scenario = builder.given("setup").when("action").build()
        scenario.execute()
        assert "setup" in executed
        assert "action" in executed


class TestPerformanceStress:
    """Performance and stress tests - 5 tests"""
    
    def test_many_scenarios_in_feature(self):
        feature = BDDFeature("BigFeature")
        for i in range(100):
            feature.add_scenario(BDDScenario(f"S{i}"))
        assert len(feature.scenarios) == 100
    
    def test_many_steps_in_scenario(self):
        scenario = BDDScenario("BigScenario")
        for i in range(50):
            scenario.add_given(BDDStep("Given", f"step{i}"))
        assert len(scenario.given_steps) == 50
    
    def test_large_registry(self):
        registry = StepRegistry()
        for i in range(30):
            registry.given(f"step{i}")(lambda: None)
        for i in range(30):
            registry.when(f"action{i}")(lambda: None)
        for i in range(30):
            registry.then(f"verify{i}")(lambda: None)
        total = len(registry.given_steps) + len(registry.when_steps) + len(registry.then_steps)
        assert total == 90
    
    def test_large_context(self):
        registry = StepRegistry()
        for i in range(100):
            registry.set_context(f"key{i}", f"value{i}")
        for i in range(100):
            assert registry.get_context(f"key{i}") == f"value{i}"
    
    def test_large_reporter_results(self):
        reporter = BDDReporter()
        for i in range(50):
            steps = [BDDStep("Given", f"g{i}")]
            status = "PASSED" if i % 2 == 0 else "FAILED"
            reporter.add_result(f"test{i}", steps, status)
        stats = reporter.get_statistics()
        assert len(reporter.results) == 50
        assert stats["total"] == 50


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
