pipeline {
    agent any
    stages {
        stage('Build environment') {
            steps {
                bash 'echo P$ATH'
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
            //bash 'conda remove --yes -n ${JOB_NAME} --all'
        }

    }
}
