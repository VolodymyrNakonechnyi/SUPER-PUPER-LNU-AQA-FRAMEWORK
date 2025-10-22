"""
Custom BDD Framework - DSL for Feature-Based Testing
Provides Given-When-Then pattern for readable test scenarios
"""
from typing import Callable, Dict, List, Any
from functools import wraps
import inspect


class BDDStep:
    """Represents a single BDD step"""
    def __init__(self, keyword: str, description: str, func: Callable = None):
        self.keyword = keyword
        self.description = description
        self.func = func
    
    def __repr__(self):
        return f"{self.keyword} {self.description}"


class BDDScenario:
    """Represents a BDD scenario with Given-When-Then steps"""
    def __init__(self, scenario_name: str):
        self.name = scenario_name
        self.given_steps: List[BDDStep] = []
        self.when_steps: List[BDDStep] = []
        self.then_steps: List[BDDStep] = []
        self.background_steps: List[BDDStep] = []
        self.data_table: Dict[str, Any] = {}
    
    def add_given(self, step: BDDStep):
        """Add a Given step (precondition)"""
        self.given_steps.append(step)
        return self
    
    def add_when(self, step: BDDStep):
        """Add a When step (action)"""
        self.when_steps.append(step)
        return self
    
    def add_then(self, step: BDDStep):
        """Add a Then step (assertion)"""
        self.then_steps.append(step)
        return self
    
    def add_background(self, step: BDDStep):
        """Add a Background step (precondition for all scenarios)"""
        self.background_steps.append(step)
        return self
    
    def set_data_table(self, data: Dict[str, Any]):
        """Set data table for the scenario"""
        self.data_table = data
        return self
    
    def get_all_steps(self) -> List[BDDStep]:
        """Get all steps in order"""
        return self.background_steps + self.given_steps + self.when_steps + self.then_steps
    
    def execute(self):
        """Execute all steps in sequence"""
        steps = self.get_all_steps()
        for step in steps:
            if step.func:
                step.func()


class BDDFeature:
    """Represents a BDD Feature with multiple scenarios"""
    def __init__(self, feature_name: str, description: str = ""):
        self.name = feature_name
        self.description = description
        self.scenarios: List[BDDScenario] = []
    
    def add_scenario(self, scenario: BDDScenario):
        """Add a scenario to the feature"""
        self.scenarios.append(scenario)
        return self
    
    def get_scenarios(self) -> List[BDDScenario]:
        """Get all scenarios"""
        return self.scenarios


class StepRegistry:
    """Registry for step definitions and their implementations"""
    def __init__(self):
        self.given_steps: Dict[str, Callable] = {}
        self.when_steps: Dict[str, Callable] = {}
        self.then_steps: Dict[str, Callable] = {}
        self.scenario_context: Dict[str, Any] = {}
    
    def given(self, step_definition: str):
        """Decorator for Given step definitions"""
        def decorator(func: Callable):
            self.given_steps[step_definition] = func
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def when(self, step_definition: str):
        """Decorator for When step definitions"""
        def decorator(func: Callable):
            self.when_steps[step_definition] = func
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def then(self, step_definition: str):
        """Decorator for Then step definitions"""
        def decorator(func: Callable):
            self.then_steps[step_definition] = func
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def set_context(self, key: str, value: Any):
        """Store context data for steps"""
        self.scenario_context[key] = value
    
    def get_context(self, key: str) -> Any:
        """Retrieve context data"""
        return self.scenario_context.get(key)
    
    def clear_context(self):
        """Clear context data"""
        self.scenario_context.clear()
    
    def match_step(self, keyword: str, description: str) -> Callable:
        """Find matching step definition"""
        steps_dict = {
            'Given': self.given_steps,
            'When': self.when_steps,
            'Then': self.then_steps,
        }
        
        step_dict = steps_dict.get(keyword, {})
        
        # Try exact match first
        if description in step_dict:
            return step_dict[description]
        
        # Try pattern matching (for parameterized steps)
        for pattern, func in step_dict.items():
            if self._matches_pattern(pattern, description):
                return func
        
        return None
    
    @staticmethod
    def _matches_pattern(pattern: str, text: str) -> bool:
        """Simple pattern matching for parameterized steps"""
        import re
        # Convert pattern to regex (e.g., "I search for {query}" -> "I search for (.*)")
        regex_pattern = re.escape(pattern).replace(r'\{.*?\}', '(.*)')
        return re.match(regex_pattern, text) is not None


class BDDScenarioBuilder:
    """Fluent builder for creating BDD scenarios"""
    def __init__(self, scenario_name: str, registry: StepRegistry):
        self.scenario = BDDScenario(scenario_name)
        self.registry = registry
    
    def given(self, description: str) -> 'BDDScenarioBuilder':
        """Add a Given step"""
        func = self.registry.match_step('Given', description)
        step = BDDStep('Given', description, func)
        self.scenario.add_given(step)
        return self
    
    def when(self, description: str) -> 'BDDScenarioBuilder':
        """Add a When step"""
        func = self.registry.match_step('When', description)
        step = BDDStep('When', description, func)
        self.scenario.add_when(step)
        return self
    
    def then(self, description: str) -> 'BDDScenarioBuilder':
        """Add a Then step"""
        func = self.registry.match_step('Then', description)
        step = BDDStep('Then', description, func)
        self.scenario.add_then(step)
        return self
    
    def background(self, description: str) -> 'BDDScenarioBuilder':
        """Add a Background step"""
        func = self.registry.match_step('Given', description)
        step = BDDStep('Background', description, func)
        self.scenario.add_background(step)
        return self
    
    def with_data(self, data: Dict[str, Any]) -> 'BDDScenarioBuilder':
        """Add data table"""
        self.scenario.set_data_table(data)
        return self
    
    def build(self) -> BDDScenario:
        """Build and return the scenario"""
        return self.scenario


class BDDReporter:
    """Generate BDD reports"""
    def __init__(self):
        self.results: List[Dict[str, Any]] = []
    
    def add_result(self, scenario_name: str, steps: List[BDDStep], 
                   status: str, error: str = None):
        """Add test result"""
        self.results.append({
            'scenario': scenario_name,
            'steps': [str(s) for s in steps],
            'status': status,
            'error': error
        })
    
    def generate_report(self, format: str = 'text') -> str:
        """Generate report in specified format"""
        if format == 'text':
            return self._generate_text_report()
        elif format == 'json':
            return self._generate_json_report()
        return ""
    
    def _generate_text_report(self) -> str:
        """Generate text format report"""
        report = "=" * 60 + "\nBDD TEST REPORT\n" + "=" * 60 + "\n\n"
        for result in self.results:
            report += f"Scenario: {result['scenario']}\n"
            report += f"Status: {result['status']}\n"
            for step in result['steps']:
                report += f"  - {step}\n"
            if result['error']:
                report += f"Error: {result['error']}\n"
            report += "\n"
        return report
    
    def _generate_json_report(self) -> str:
        """Generate JSON format report"""
        import json
        return json.dumps(self.results, indent=2)
    
    def get_statistics(self) -> Dict[str, int]:
        """Get test statistics"""
        return {
            'total': len(self.results),
            'passed': len([r for r in self.results if r['status'] == 'PASSED']),
            'failed': len([r for r in self.results if r['status'] == 'FAILED']),
            'skipped': len([r for r in self.results if r['status'] == 'SKIPPED'])
        }


# Global step registry instance
step_registry = StepRegistry()
