pipeline {
    agent any
    stages {
        stage('Build environment') {
            steps {
                sh 'echo $PATH'
            }
        }
        stage('Test environment') {
            steps {
                sh '''#!/bin/bash
                        echo $SHELL
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
