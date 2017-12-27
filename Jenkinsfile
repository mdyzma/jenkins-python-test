pipeline {
    agent any

    stages {
        stage('Build environment') {
            steps {
                sh '''echo $PATH
                export PATH="/var/lib/jenkins/miniconda3/bin:$PATH"
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
