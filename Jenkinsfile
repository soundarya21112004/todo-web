pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/soundarya21112004/todo-web.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t todo-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker stop todo-container || true'
                sh 'docker rm todo-container || true'
                sh 'docker run -d -p 8081:80 --name todo-container todo-app'
            }
        }
    }
}