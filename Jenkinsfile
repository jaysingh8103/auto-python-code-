pipeline {
    agent any

    environment {
        GITHUB_REPO = 'https://github.com/jaysingh8103/auto-python-code-.git'
        GITHUB_CREDENTIALS_ID = 'Github_Credentials'
        BRANCH_NAME = 'main'
        GITHUB_USER ='jaysingh8103'
        GITHUB_PASSWORD  = 'ITengineer12'
    }


    stages {

       stage('Clone Repository') {
            steps {
                script {
                    def repoDir = 'auto-python-code-'
                    if (fileExists(repoDir)) {
                        echo "Repository already exists. Pulling latest changes..."
                        dir(repoDir) {
                            sh 'git reset --hard'  // Reset any local changes
                            sh 'git pull origin main'
                        }
                    } else {
                        echo "Cloning repository..."
                        sh "git clone -b main https://github.com/jaysingh8103/auto-python-code-.git"
                    }
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

        


       stage('Replace Unoptimized Code') {
            steps {
                echo 'Replacing unoptimized code with optimized code...'
                withCredentials([usernamePassword(
                    credentialsId: 'Github_Credentials',
                    usernameVariable: 'GITHUB_USER',
                    passwordVariable: 'GITHUB_PASSWORD'
                )]) {
                    sh '''
                        set -x
                        git config user.name "${GITHUB_USER}"
                        git config user.email "jaypals840@gmail.com"
                        git checkout ${BRANCH_NAME} || git checkout  ${BRANCH_NAME}
                        git add .
                        git commit -m "Auto commit: optimized code" || echo "Nothing to commit"
                        git push https://${GITHUB_USER}:${GITHUB_PASSWORD}@github.com/jaysingh8103/auto-python-code-.git ${BRANCH_NAME}
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

