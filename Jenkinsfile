pipeline {
    agent { dockerfile true }

    stages {
        stage('Test_login') {
            steps {
                sh "sudo poetry run pytest/tests/test_login.py"
                echo "End of Stage Build"
            }
        }
        stage('Test_register') {
            steps {
                sh "sudo poetry run pytest/tests/test_register.py"
                echo "End of Stage Build"
            }
        }
   }
}