

Create aurora DB
- choose serverless, can scale fast etc.
- VPC, just use default
- Just type in a username and password, but we are not going to use it anyways.
- enable Data API so that we can communicate with db through HTTP


Create Lambda
- Since we are using the Data API we dont need to put the lambda function inside the same VPN as the database. 
  Without the Data API, our lambda had to be in the same VPC as the database.
- copy some variables, including the arn of the auto-generated aws secret.
- link to Boto3 RDS documentation
- write code
- should now fail: Add IAM permissions