pipeline {
    agent any

    environment{
        PATH="$PATH:/var/lib/jenkins/miniconda3/bin"
    }

    stages {
        stage('Build environment') {
            steps {
                echo "Building virtualenv"
                sh  ''' conda create --yes -n ${BUILD_TAG} python
                        source activate ${BUILD_TAG}
                        pip install -r requirements/dev.txt
                    '''
            }
        }
        stage('Static code metrics') {
            steps {
                echo "Raw metrics"
                sh  ''' source activate ${BUILD_TAG}
                        radon raw --json irisvmpy/
                        radon cc --json irisvmpy/
                        radon mi --json irisvmpy/
                    '''
                echo "Test coverage"
                echo "Error and style check"
            }
        }
    }
    post {
        always {
            sh 'conda remove --yes -n ${BUILD_TAG} --all'

        }

    }
}
