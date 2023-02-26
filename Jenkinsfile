pipeline {
  agent any
  	environment {
    ALLURE_DIR = "./src/test/allure-reports"
	TESTRAIL_CMD_OPTIONS = "--testrail --tr-config=testrail.cfg --tr-run-id=1285 --tr-no-ssl-cert-check"
	BASE_CMD_OPTIONS = "python -m pytest -n 4 --dist loadfile -q -v --reruns=1"
	BASE_API_PATH = "./src/test/api/tests"
	API_PATHS = ""
	}
  stages {
    stage('sleep') {
        steps {
            script {
                if (currentBuild.buildCauses.toString().contains('UserIdCause')){
                    echo "Path to Allure ${ALLURE_DIR}" }
                      }
                }
              }
            }
    stage('API tests') {
        catchError {
            script {
        def apiPaths = []
        def apiPath
        if (params.API_1) {
            apiPaths.add("${BASE_API_PATH}/test_dispatcher")
        }
        if (params.API_2) {
            apiPaths.add("${BASE_API_PATH}/test_document")
        }
        if (params.AUTH) {
            apiPaths.add("${BASE_API_PATH}/test_auth")
        }
        apiPath = apiPaths.join(" ")
        if (apiPath) {
                echo "Running API tests"
                echo "${BASE_CMD_OPTIONS} ${apiPath} ${TESTRAIL_CMD_OPTIONS} --alluredir ${ALLURE_DIR}"
            }
                }
            }
        }
}
