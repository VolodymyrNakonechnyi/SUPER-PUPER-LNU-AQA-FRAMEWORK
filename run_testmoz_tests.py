#!/usr/bin/env python3
"""
Test runner script specifically for Testmoz tests
"""
import subprocess
import sys
import os
from pathlib import Path


def run_testmoz_tests(test_type="all", browser="firefox", headless=False):
    """
    Run Testmoz tests with specified parameters
    
    Args:
        test_type (str): Type of tests to run (all, homepage, demo, functionality)
        browser (str): Browser to use (chrome, firefox, edge)
        headless (bool): Run in headless mode
    """
    
    # Set environment variables
    env = os.environ.copy()
    env['BROWSER'] = browser
    env['HEADLESS'] = str(headless).lower()
    env['BASE_URL'] = 'https://testmoz.com'
    
    # Base pytest command
    cmd = [sys.executable, "-m", "pytest"]
    
    # Add test selection based on type
    if test_type == "homepage":
        cmd.append("tests/test_testmoz_homepage.py")
    elif test_type == "demo":
        cmd.append("tests/test_testmoz_demo.py")
    elif test_type == "functionality":
        cmd.append("tests/test_testmoz_functionality.py")
    elif test_type == "testmoz":
        cmd.extend(["tests/test_testmoz_homepage.py", 
                   "tests/test_testmoz_demo.py", 
                   "tests/test_testmoz_functionality.py"])
    else:  # all
        cmd.extend(["tests/test_testmoz_homepage.py", 
                   "tests/test_testmoz_demo.py", 
                   "tests/test_testmoz_functionality.py"])
    
    # Add other options
    cmd.extend([
        "--verbose",
        "--tb=short",
        "--html=reports/testmoz_report.html",
        "--self-contained-html",
        "--junitxml=reports/testmoz_junit.xml"
    ])
    
    # Run tests
    print(f"Running Testmoz tests with command: {' '.join(cmd)}")
    print(f"Browser: {browser}, Headless: {headless}")
    print(f"Test type: {test_type}")
    
    result = subprocess.run(cmd, env=env)
    return result.returncode


def main():
    """Main function to handle command line arguments"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Testmoz Test Runner")
    parser.add_argument("--test-type", 
                       choices=["all", "homepage", "demo", "functionality", "testmoz"], 
                       default="homepage", 
                       help="Type of tests to run")
    parser.add_argument("--browser", choices=["chrome", "firefox", "edge"], 
                       default="firefox", help="Browser to use")
    parser.add_argument("--headless", action="store_true", 
                       help="Run in headless mode")
    
    args = parser.parse_args()
    
    # Create necessary directories
    Path("reports").mkdir(exist_ok=True)
    Path("screenshots").mkdir(exist_ok=True)
    
    # Run tests
    exit_code = run_testmoz_tests(args.test_type, args.browser, args.headless)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
