pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr:'10'))
    }

    environment{
        PATH="$PATH:/var/lib/jenkins/miniconda3/bin"
    }

    triggers {
        pollSCM('H */4 * * 1-5')
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
                        radon raw --json irisvmpy > raw_report.json
                        radon cc --json irisvmpy > cc_report.json
                        radon mi --json irisvmpy > mi_report.json
                        sloccount --duplicates --wide irisvmpy > sloccount.sc
                    '''
                echo "Test coverage"
                sh  ''' source activate ${BUILD_TAG}
                        coverage run irisvmpy/iris.py 1 1 2 3
                        python -m coverage xml -o ./reports/coverage.xml
                    '''
                echo "Style check"
            }
        }
    }

    post {
        always {
            sh 'conda remove --yes -n ${BUILD_TAG} --all'
        }
        success {
            sh 'ls -las'
            sloccountPublish encoding: '', pattern: ''
            archive '*/reports/*'
            junit "*/reports/*.xml"
        }
    }
}
