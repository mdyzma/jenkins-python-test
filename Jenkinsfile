pipeline {
    agent any

    environment{
        PATH="$PATH:/var/lib/jenkins/miniconda3/bin"
    }

    stages {
        stage('Build environment') {
            steps {
                sh '''conda create --yes -n ${BUILD_TAG} python
                    source activate ${BUILD_TAG}
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test environment') {
            steps {
                sh '''source activate ${BUILD_TAG}
                pip list
                echo "================="
                which python
                which pip
                '''
            }
        }
    }
    post {
        always {
            sh 'conda remove --yes -n ${BUILD_TAG} --all'
        }

    }
}
