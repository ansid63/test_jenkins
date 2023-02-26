pipeline {
  agent any
  	environment {
    ALLURE_DIR = "./src/test/allure-reports"
	TESTRAIL_CMD_OPTIONS = "--testrail --tr-config=testrail.cfg --tr-run-id=1285 --tr-no-ssl-cert-check"
	BUILD_BY_USER = currentBuild.buildCauses.toString().contains('UserIdCause')
	}
  stages {
    stage('sleep') {
        steps {
            script {
                if (currentBuild.buildCauses.toString().contains('UserIdCause')){
                    echo 'Path to Allure ${ALLURE_DIR}' }
                else {
                      echo "Auto"
                        }
                      }
                }
              }
        }
    }