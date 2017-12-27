pipeline {
    agent any

    environment{
        PATH="$PATH:/var/lib/jenkins/miniconda3/bin"
    }

    stages {
        stage('Build environment') {
            steps {
                sh '''conda create --yes -n ${JOB_NAME} python
                    source activate ${JOB_NAME}
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
            //bash 'conda remove --yes -n ${JOB_NAME} --all'
        }

    }
}
