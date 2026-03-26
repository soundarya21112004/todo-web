pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/soundarya21112004/todo-web.git'
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh 'docker-compose down'
            }
        }

        stage('Build & Run New Containers') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }

    }
}
}