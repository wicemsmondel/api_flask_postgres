podTemplate(containers: [
  containerTemplate(name: 'docker', image: 'docker:1.11', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'python', image: 'python:2', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'aws', image: 'xueshanf/awscli:3.10-alpine', command: 'cat', ttyEnabled: true),
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
]){
    node(POD_LABEL){
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'AWS_Cred']]){
          stage('Build Image'){
            withCredentials([usernamePassword(credentialsId: 'GitCred', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]){
              sh '''
              git config --global user.name $USERNAME
              git config --global user.email $USERNAME@gmail.com
              git clone https://$USERNAME:$PASSWORD@github.com/api_flask_postgres.git
              cd api_flask_postgres/api
              GIT_COMMIT="$(git rev-parse HEAD)"
              echo '###### Git START ########'
              echo $GIT_COMMIT
              echo '###### Git END ########'
              echo 'export IMAGE=817235077064.dkr.ecr.eu-west-1.amazonaws.com/jenkins:'$GIT_COMMIT > ./load_env.sh
              echo 'export IMAGELATEST=817235077064.dkr.ecr.eu-west-1.amazonaws.com/jenkins:latest' >> ./load_env.sh
              echo 'export GIT_COMMIT='$GIT_COMMIT >> ./load_env.sh
              echo 'export REPO=817235077064.dkr.ecr.eu-west-1.amazonaws.com/jenkins' >> ./load_env.sh
              chmod 750 ./load_env.sh
              '''
              container('python'){
                  sh '''
                  echo ‘#### PYTHON START ####’
            				cd api_flask_postgres/api
            				pip install flask
            				echo ‘#### PYTHON END ####’
                  '''
              }
            }
          }
          stage('Push Image In ECR'){
              container('aws'){
                  sh '''
                  aws ecr get-login --region eu-west-1 --no-include-email | bash -
                  '''
              }
              container('docker'){
                  sh '''
                  cd /api_flask_postgres/api
                  . ./load_env.sh
                  docker build . -t $IMAGE
                  docker tag $IMAGE $IMAGELATEST
                  docker push $IMAGE
                  docker push $IMAGELATEST
                  '''
              }
            }
            stage('Generate Report'){
                  sh '''
                  cd api_flask_postgres/api
                  . ./load_env.sh
                  cd ..
                  mkdir report
                  cd report
                  echo '##############################################' > ./report.yaml
                  echo 'RapportDeBuild:' >> ./report.yaml
                  echo 'gitCommit: '$GIT_COMMIT >> ./report.yaml
                  echo 'imagesBuild : ' >> ./report.yaml
                  echo '  tagCommit : '$IMAGE >> ./report.yaml
                  echo '  tagLatest : '$IMAGELATEST >> ./report.yaml
                  echo '##############################################' >> ./report.yaml
                  cat ./report.yaml
                  '''
          }
        }
    }
}
