pipeline {
    agent any

    environment {
        GITHUB_REPO = 'https://github.com/jaysingh8103/auto-python-code-.git'
        GITHUB_CREDENTIALS_ID = 'github_credentials'
        BRANCH_NAME = 'main'
        GITHUB_USER ='jaysingh8103'
        GITHUB_PASSWORD  = 'ITengineer12'
    }

    stages {

       stage('Clone Repository') {
            steps {
                git branch: env.BRANCH_NAME, url: env.GITHUB_REPO, credentialsId: env.GITHUB_CREDENTIALS_ID
                script {
                    sh 'git clone -b ${BRANCH_NAME} ${GITHUB_REPO}'
                }
            }
        }
        
        stage('Set Up Virtual Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                }
            }
        }
        stage('Archive Optimized Code') {
            steps {
                script{
                    echo 'Archiving optimized code...'
                    archiveArtifacts artifacts: 'code1.py', fingerprint: true
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh '. venv/bin/activate && pip install --upgrade pip'
                    sh '. venv/bin/activate && pip install black autopep8 pylint flake8 bandit pyflakes'
                }
            }
        }

        stage('Optimize Code') {
            steps {
                script {
                    sh '. venv/bin/activate && black .'
                    sh '. venv/bin/activate && autopep8 --in-place --recursive .'
                }
            }
        }

        stage('Static Analysis and Linting') {
            steps {
                script {
                    def lintResults = sh(script: '. venv/bin/activate && flake8 . --count --exit-zero --max-complexity=10 --statistics', returnStdout: true)
                    echo "Linting results:\n${lintResults}"

                    def pylintResults = sh(script: '. venv/bin/activate && pylint $(find . -name "*.py") || true', returnStdout: true)
                    echo "Pylint results:\n${pylintResults}"
                }
            }
        }

        stage('Error Detection and Fixing') {
            steps {
                script {
                    def banditResults = sh(script: '. venv/bin/activate && bandit -r . -f json', returnStdout: true)
                    echo "Security analysis results:\n${banditResults}"

                    def pyflakesResults = sh(script: '. venv/bin/activate && python3 -m pyflakes . || true', returnStdout: true)
                    echo "Error detection results:\n${pyflakesResults}"

                    // Auto-fix common issues
                    sh '. venv/bin/activate && autopep8 --in-place --recursive .'
                    sh '. venv/bin/activate && pylint --exit-zero $(find . -name "*.py")'
                }
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
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for errors.'
        }
    }
}

