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
      }
    }
  }
  
}
