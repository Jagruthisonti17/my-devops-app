pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp /opt/myapp'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker stop myapp || true'
                sh 'docker rm myapp || true'
                sh 'docker run -d -p 5000:5000 --name myapp myapp'
            }
        }
    }
}
