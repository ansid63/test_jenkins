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
//     stage("Build image") {
// 		  steps {
// 			catchError {
// 			  script {
// 				docker.build("python-tests", "-f Dockerfile .")
// 			  }
// 			 }
// 		  }
// 		}
    stage('sleep') {
        steps {
            script {
                if (currentBuild.buildCauses.toString().contains('UserIdCause')){
                    echo "timeout(time:120, unit: 'SECONDS')" }
                      }
                }
              }
    stage('API tests') {
        steps {
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

//     stage("Start Selenoid") {
//         dir('/home/av@domain.ru/') {
//             sh "./cm_linux_amd64 selenoid stop"
//             sh "./cm_linux_amd64 selenoid start --browsers-json ${homeDir}/browsers.json --args '-limit 5'"
//             sh "./cm_linux_amd64 selenoid status"
//         }
//     }


    }
  }
