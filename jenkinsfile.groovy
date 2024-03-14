pipeline {
    agent any

    stages {
        stage('Insert Data to SQL Server') {
            steps {
                script {
                    // Wywołaj skrypt Pythona, który wstawia dane do SQL Server
                    sh 'python skrypt.py'
                }
            }
        }
    }
}
