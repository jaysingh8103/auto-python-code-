pipeline {
    agent any

    environment {
        GITHUB_REPO = 'https://github.com/jaysingh8103/auto-python-code-.git'
        GITHUB_CREDENTIALS_ID = 'github_credentials'
        BRANCH_NAME = 'main'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: env.BRANCH_NAME, url: env.GITHUB_REPO, credentialsId: env.GITHUB_CREDENTIALS_ID
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

        stage('Install Dependencies') {
            steps {
                script {
                    sh '. venv/bin/activate && pip install --upgrade pip'
                    sh '. venv/bin/activate && pip install black autopep8 pylint flake8'
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

        stage('Push Optimized Code to GitHub') {
            steps {
                script {
                    sh '''
                    git config --global user.email "jaypals840@gmail.com"
                    git config --global user.name "jaysingh8103"
                    git add .
                    git commit -m "Auto-optimized Python code and fixed linting issues"
                    git push https://${env.GITHUB_USERNAME}:${env.GITHUB_TOKEN}@github.com/jaysingh8103/auto-python-code-.git
                    '''
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

