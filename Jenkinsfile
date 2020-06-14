pipeline {
    agent { dockerfile true }

    stages {
        stage('Test_login') {
            steps {
                sh "poetry run pytest/tests/test_login.py --no-cache-dir"
                echo "End of Stage Build"
            }
            }
        }
    }
