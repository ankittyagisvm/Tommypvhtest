pipeline{
    agent any
    parameters{
        choice(choices: 'Yes/No', description: 'Are you sure to want to execute this test ?', name: 'run_test_only')
        choice(choices:'Yes/No', description: 'Archieved war ?', name: 'archive_war')
        string(defaultValue: "antyagi291@gmail.com", description: 'email for notification', name: 'notification_email')
    }
    environment{
        firstEnvVar = 'FIRST_VAR'
        secondEnvVar = 'SECOND_VAR'
        thirdEnvVar = 'THIRD_VAR'
    }
    stages{
        stage('Test'){
            when{
                environment name: 'run_test_only', value: 'Yes'
            }
            steps{
                echo "We except first choice with first variable value ${firstEnvVar}"
            }
        }
        stage('Run demo parallel stages'){
            steps{
                parallel(
                    "Parallel stage #1":
                    {
                        // running a script instead of DSL. In this case to run an if/else
                        script{
                            if(env.run_test_only=='Yes')
                                {
                                    echo env.firstEnvVar
                                }
                            else{
                                    echo env.secondEnvVar
                            }       
                        }
                    },
                    "Parallel stage #2":
                    {
                        echo "${thirdEnvVar}"
                    }
                )
            }
        }
    }
    post{
        success{
            echo "Testing succeeds"
            script{

                mail(bcc: '', 
                     body: "Run ${JOB_NAME}-#${BUILD_NUMBER} succeeded. To get more detail, visit the build results page: ${BUILD_URL}.",
                     cc: '',
                     from: 'jenkins-admin@gmail.com',
                     replyTo: '',
                     subject: "${JOB_NAME} ${BUILD_NUMBER} succeeded",
                     to: env.notification_email,)
                     if(env.archive_war == 'yes')
                     {
                         echo "step 2 forward"
                     }
            }
        }
    }
}
