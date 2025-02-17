pipeline {
    agent any

    environment {
        GITHUB_REPO = ''
        GITHUB_CREDENTIALS_ID = 'github_credentials'
        BRANCH_NAME = 'main'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: env.BRANCH_NAME, url: env.GITHUB_REPO, credentialsId: env.GITHUB_CREDENTIALS_ID
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install --upgrade pip'
                    sh 'pip install black autopep8 pylint flake8'
                }
            }
        }

        stage('Optimize Code') {
            steps {
                script {
                    sh 'black .'
                    sh 'autopep8 --in-place --recursive .'
                }
            }
        }

        stage('Static Analysis and Linting') {
            steps {
                script {
                    def lintResults = sh(script: 'flake8 . --count --exit-zero --max-complexity=10 --statistics', returnStdout: true)
                    echo "Linting results:\n${lintResults}"

                    def pylintResults = sh(script: 'pylint $(find . -name "*.py") || true', returnStdout: true)
                    echo "Pylint results:\n${pylintResults}"
                }
            }
        }

        stage('Push Optimized Code to GitHub') {
            steps {
                script {
                    sh '''
                    git config --global user.email "jenkins@localhost"
                    git config --global user.name "Jenkins"
                    git add .
                    git commit -m "Auto-optimized Python code and fixed linting issues"
                    git push https://${env.GITHUB_USERNAME}:${env.GITHUB_TOKEN}@github.com/username/repo.git
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
