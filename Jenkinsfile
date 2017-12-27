pipeline {
    agent any

    environment{
        PATH="$PATH:/var/lib/jenkins/miniconda3/bin"
    }

    stages {
        stage('Build environment') {
            steps {
                sh '''echo $PATH
                echo $HOME
                echo $SHELL
                conda info
                source /etc/profile
                '''
            }
        }
        stage('Test environment') {
            steps {
                sh '''echo $SHELL
                        which pip
                        which python
                        conda info
                        source /etc/profile
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
