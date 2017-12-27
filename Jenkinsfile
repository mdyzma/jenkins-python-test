pipeline {
    agent any

    environment{
        source /etc/profile
    }
    stages {
        stage('Build environment') {
            steps {
                sh '''echo $PATH
                conda info
                '''
            }
        }
        stage('Test environment') {
            steps {
                sh '''echo $SHELL
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
