pipeline {
    agent any
    stages {
        stage('Build environment') {
            steps {
                sh 'echo P$ATH'
            }
        }
        stage('Test environment') {
            steps {
                sh '''#!/bin/bash
                        pip list
                        which pip
                        which python
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
