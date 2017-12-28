pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr:'10'))
    }

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
                        radon raw --json irisvmpy/ > raw _report.json
                        radon cc --json irisvmpy/ > cc_report.json
                        radon mi --json irisvmpy/ > mi_report.json
                        sloccount --duplicates --wide --details path-to-code/ > sloccount.sc
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
        success {
            sloccountPublish encoding: '', pattern: ''
        }
    }
}
