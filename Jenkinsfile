pipeline {
  agent any
  	environment {
    ALLURE_DIR = "./src/test/allure-reports"
	TESTRAIL_CMD_OPTIONS = "--testrail --tr-config=testrail.cfg --tr-run-id=1285 --tr-no-ssl-cert-check"
	BASE_CMD_OPTIONS = "python -m pytest -n 4 --dist loadfile -q -v --reruns=1"
	BASE_API_PATH = "./src/test/api/tests"
	BASE_UI_PATH = "./src/test/ui/tests"
	API_PATHS = ""
	}
  stages {
    stage("Build image") {
		  steps {
			catchError {
			  script {
				docker.build("python-tests", "-f Dockerfile .")
			  }
			 }
		  }
		}
    stage('sleep') {
        steps {
            script {
                if (currentBuild.buildCauses.toString().contains('UserIdCause')){
                    echo "timeout(time:120, unit: 'SECONDS')" }
                      }
                }
              }
    stage('Run API tests') {
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
                    if (params.AUTH_API) {
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

    stage("Start Selenoid") {
        steps {
            catchError {
               script {
//         dir('/home/av@domain.ru/') {
//             sh "./cm_linux_amd64 selenoid stop"
//             sh "./cm_linux_amd64 selenoid start --browsers-json ${env.WORKSPACE}/browsers.json --args '-limit 5'"
//             sh "./cm_linux_amd64 selenoid status"
               echo "Current workspace is ${env.WORKSPACE}"
               bat "dir /b /a-d"
//                def status = bat(returnS: true, script: 'docker ps').toString()
//                if (status.contains("lts")) {
//                   echo "Selenoid worked well!"
//                } else {
//                   echo "Selenoid broken"
//                }
                }
            }
        }
    }
    stage('Run UI tests') {
        steps {
            catchError {
                script {
                    def uiPaths = []
                    def uiPath
                    if (params.UI_1) {
                        uiPaths.add("${BASE_UI_PATH}/test_dispatcher")
                    }
                    if (params.UI_2) {
                        uiPaths.add("${BASE_UI_PATH}/test_document")
                    }
                    if (params.AUTH_UI) {
                        uiPaths.add("${BASE_UI_PATH}/test_auth")
                    }
                    uiPath = uiPaths.join(" ")
                    if (uiPath) {
                        echo "Running tests"
//                         echo "headless mode=${HEADLESS}"
                        echo "${BASE_CMD_OPTIONS} --log-cli-level=INFO ${uiPath} ${TESTRAIL_CMD_OPTIONS} --alluredir ${ALLURE_DIR}"
                        }
                    }
                }
            }
        }
//     stage('Reports') {
//       steps {
//         allure([
//           includeProperties: false,
//           jdk: '',
//           properties: [],
//           reportBuildPolicy: 'ALWAYS',
//           results: [[path: 'report']]
//         ])
//       }
//      }
    stage('Remove image') {
        steps {
            script {
                bat "docker rmi python-tests:latest"
                      }
                }
              }
    stage("Discord Chat") {
            steps {
                script {
                   def summaryJson = readJSON file: 'browsers.json'
                    def json_ = summaryJson["chrome"]["versions"]["latest"]["port"]
                    def reportLink = "http://jenkins.alrosa.ru/job/CDSRE_testing/job/CADAS_DM_tests/job/Run%20tests/allure/"
                    def message = "Total: $json_. Link: $reportLink"
                    def webhookUrl = 'https://discord.com/api/webhooks/1088058148411158609/6kJkLUidP-ipXWRrGPmhug8c2gjPlsxO5sjXHLoEJbVasv8c6M-OiEE3LTYhddU_2L1g'
                    bat """curl -H "Content-Type:application/json" -v -X POST --data \"{\\\"content\\\": \\\"$message\\\"}\" --url $webhookUrl"""
                    }
                }
            }
    }
  }
