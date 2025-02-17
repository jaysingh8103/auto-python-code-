pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/jaysingh8103/auto-python-code-.git'
        BRANCH = 'main'
        GITHUB_USER ='jaysingh8103'
        GITHUB_PASSWORD  = 'ITengineer12'
        SONARQUBE_PASSWORD = 'jay8'
        SONARQUBE_USER = 'admin'
        
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git branch: "${BRANCH}", url: "${REPO_URL}", credentialsId:'github_credentials'
               
            }
        
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate && pip install --upgrade pip
                    pip install --cache-dir .pip-cache flake8 black autopep8 pylint matplotlib pandas
                    curl -o sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
                    unzip -o sonar-scanner.zip
                    export PATH=$PATH:$(pwd)/sonar-scanner-5.0.1.3006-linux/bin
                '''
            }
        }

        stage('Linting') {
            steps {
                echo 'Running Flake8 and Pylint...'
                sh '. venv/bin/activate && flake8 --exit-zero . > flake8-report.txt || true'
                sh '. venv/bin/activate && pylint --output-format=colorized --fail-under=5 main.py || true'
                archiveArtifacts artifacts: 'flake8-report.txt'
            }
        }
        stage('Code Optimization with autopep8 ') {
            steps {
                echo 'Optimizing code with autopep8...'
                sh '. venv/bin/activate && autopep8 --in-place --aggressive --aggressive main.py'
               
            }
        }
        stage('Code Optimization with black ') {
            steps {
                echo 'Optimizing code with black...'
                sh '. venv/bin/activate && black .'
            }
        }

         stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube analysis with debug mode...'
                withCredentials([string(credentialsId: 'pyhton-sonar-id', variable: 'SONAR_TOKEN')]) {
                    sh '''
                    . venv/bin/activate && \
                    ./sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner \
                      -Dsonar.host.url="http://localhost:9000/" \
                      -Dsonar.login=$SONAR_TOKEN \
                      -Dsonar.projectKey="pyhton-auto" \
                      -Dsonar.projectName="pyhton-auto" \
                      -Dsonar.sources="." \
                      -X
                    '''
                }
             }
        }
        stage('Generate Report') {
            steps {
                echo 'Generating code analysis report...'
                sh '. venv/bin/activate && python generate_report.py'
                sh 'ls -la' 
                archiveArtifacts artifacts: 'code_quality_report.txt'
            }
        }
        stage('Replace Unoptimized Code') {
            steps {
                echo 'Replacing unoptimized code with optimized code...'
                withCredentials([usernamePassword(credentialsId: 'github_credentials', usernameVariable: 'GITHUB_USER', passwordVariable: 'GITHUB_PASSWORD')]) {
                    sh 'git config user.name "${GITHUB_USER}"'
                    sh 'git config user.email "jaypals840@gmail.com"'
                    sh 'git add .'
                    sh 'git commit -m "First "'
                    sh 'git push https://${GITHUB_USER}:${GITHUB_PASSWORD}@github.com/jaysingh8103/auto-python-code-.git ${BRANCH}'
                }
            }
        }

    }

    post {
        success { echo 'Pipeline completed successfully!' }
        failure { echo 'Pipeline failed!' }
    }
}
