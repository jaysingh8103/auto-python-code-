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
                    sh '. venv/bin/activate && pip install black autopep8 pylint flake8 bandit pyflakes os ast'
                }
            }
        }
        stage('Fix Syntax Errors') {
            steps {
                script {
                    echo 'Fixing syntax errors in Python files...'
                    sh '. venv/bin/activate && python3 fix_syntax_errors.py'
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
                    echo 'Running black formatter...'
                    def result = sh(script: 'black . --check --diff || true', returnStatus: true)
                    if (result != 0) {
                        echo '⚠️ Some files could not be formatted. Please check syntax issues manually.'
                        
                        error("Static analysis failed due to unformattable files.")
                    }
        
                    echo 'Running pylint...'
                    sh 'pylint **/*.py || true'
                }
            }
        }


        


       stage('Replace Unoptimized Code') {
            steps {
                echo 'Replacing unoptimized code with optimized code...'
                // withCredentials([usernamePassword(
                //     credentialsId: 'Github_Credentials',
                //     usernameVariable: 'jaysingh8103',
                //     passwordVariable: 'ITengineer12'
                // )]) {
                //     sh '''
                //         set -x
                //         git config user.name "${GITHUB_USER}"
                //         git config user.email "jaypals840@gmail.com"
                //         git checkout ${BRANCH_NAME} || git checkout  ${BRANCH_NAME}
                //         git add .
                //         git commit -m "Auto commit: optimized code" || echo "Nothing to commit"
                //         git push https://${GITHUB_USER}:${GITHUB_PASSWORD}@github.com/jaysingh8103/auto-python-code-.git ${BRANCH_NAME}
                //     '''
                // }
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

