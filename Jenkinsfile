node {    	
	stage('Run JOB1') {	
	    build job: '../../JOB1'	
	}
	stage('Run JOB2') {
	    build job: '../../JOB2'	
	}
	stage('Run Shell') {
	    sh "ls -l"
	    sh "env"
	}
}
