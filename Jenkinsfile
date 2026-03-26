pipeline {
    agent any

    stages {

        stage('Stop Old Containers') {
            steps {
                sh 'docker-compose down || true'
            }
        }

        stage('Build & Run Containers') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }

    }
}