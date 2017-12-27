pipeline {
    agent any
    stages {
        stage('Build environment') {
            steps {
                bash '''#!/bin/bash
                        conda create --yes -n ${JOB_NAME} python
                        source activate ${JOB_NAME}
                        pip install -r requirements.txt --download-cache=/tmp/${JOB_NAME}
                '''
            }
        }
        stage('Test environment') {
            steps {
                bash '''#!/bin/bash
                        pip list
                        which pip
                        which python
                    '''
            }
        }
    }
    post {
        always {
            bash 'conda remove --yes -n ${JOB_NAME} --all'
        }

    }
}
