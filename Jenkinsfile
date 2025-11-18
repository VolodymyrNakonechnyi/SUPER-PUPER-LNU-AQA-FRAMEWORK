pipeline {
    agent any
    
    environment {
        BROWSER = 'firefox'
        HEADLESS = 'true'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/VolodymyrNakonechnyi/SUPER-PUPER-LNU-AQA-FRAMEWORK.git'
            }
        }
        
        stage('Setup Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest-xdist allure-pytest
                '''
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/test_framework_components.py -n 4 -v \
                        --junitxml=reports/junit-unit.xml \
                        --html=reports/unit-tests.html \
                        --alluredir=reports/allure-results
                '''
            }
        }
        
        stage('Run BDD Tests') {
            parallel {
                stage('Homepage Tests') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            pytest tests/test_bdd_scenarios.py::TestBDDHomepageScenarios -v \
                                --junitxml=reports/junit-homepage.xml \
                                --alluredir=reports/allure-results
                        '''
                    }
                }
                stage('Demo Tests') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            pytest tests/test_bdd_scenarios.py::TestBDDDemoScenarios -v \
                                --junitxml=reports/junit-demo.xml \
                                --alluredir=reports/allure-results
                        '''
                    }
                }
            }
        }
        
        stage('Generate Reports') {
            steps {
                sh '''
                    . venv/bin/activate
                    allure generate reports/allure-results -o reports/allure-report --clean
                '''
            }
        }
        
        stage('Security Scan') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install bandit safety
                    bandit -r framework pages config -f json -o reports/bandit-report.json
                    safety check --json > reports/safety-report.json || true
                '''
            }
        }
    }
    
    post {
        always {
            junit 'reports/junit-*.xml'
            
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports/allure-report',
                reportFiles: 'index.html',
                reportName: 'Allure Report'
            ])
            
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'reports/allure-results']]
            ])
            
            archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true
        }
        
        failure {
            emailext (
                subject: "Build Failed: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                body: "Check console output at ${env.BUILD_URL}",
                to: 'your-email@example.com'
            )
        }
    }
}