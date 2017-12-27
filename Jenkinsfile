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
                    pip install -r requirements.txt --download-cache=/tmp/${JOB_NAME}
                '''
            }
        }
        stage('Test environment') {
            steps {
                sh '''pip list
                    '''
            }
        }
    }
    post {
        always {
            echo 'Finished'
            //bash 'conda remove --yes -n ${BUILD_TAG} --all'
        }

    }
}
