pipeline {
    agent any

    environment {
        REPO_URL = ''
        BRANCH = 'main'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip install --upgrade pip'
                sh 'pip install flake8 black autopep8'
            }
        }

        stage('Linting and Static Analysis') {
            steps {
                echo 'Running flake8 for linting...'
                sh 'flake8 --exit-zero . > flake8-report.txt || true'
            }
        }

        stage('Code Optimization') {
            steps {
                echo 'Optimizing code with autopep8 and black...'
                sh 'autopep8 --in-place --aggressive --aggressive main.py'
                sh 'black .'
            }
        }

        stage('Replace Unoptimized Code') {
            steps {
                echo 'Replacing unoptimized code with optimized code...'
                sh 'git config user.name "Jenkins"'
                sh 'git config user.email "jenkins@example.com"'
                sh 'git add .'
                sh 'git commit -m "Auto-optimized code via Jenkins pipeline" || true'
                sh 'git push origin ${BRANCH}'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
