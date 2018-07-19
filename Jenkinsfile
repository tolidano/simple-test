pipeline {
  agent any
  stages {
    stage('Run Tests') {
      steps {
        catchError() {
          sh '''python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
nosetests test.py --with-timer --with-xunit'''
        }
        post {
            failure {
                echo "Sending Failure Notification Email"
                mail to: 'shawn@tolidano.com',
                     subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                     body: "Something is wrong with ${env.BUILD_URL}"
            }
            success {
                echo "Sending Success Notification Email"
                mail to: 'shawn@tolidano.com',
                     subject: "Successful Pipeline: ${currentBuild.fullDisplayName}",
                     body: "Nothing is wrong with ${env.BUILD_URL}"
            }
        }
      }
    }
  }
  
}
