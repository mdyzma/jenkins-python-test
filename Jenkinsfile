pipeline {
    agent any
    stages {
        stage('Build environment') {
            steps {
                sh '''
                conda create --yes -n ${BUILD_TAG} python
                source activate ${BUILD_TAG}
                pip install -r requirements.txt --download-cache=/tmp/${JOB_NAME}
                '''
            }
        }
        stage('Test environment') {
            steps {
                sh '''
                    pip list
                    which pip
                    which python
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
