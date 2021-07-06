# AWS Lambda

In this module we are going to learn how to write Lambda functions using python. We are also going to make use of other AWS services such as; SQS, DynamoDB, API Gateways, S3, IAM, etc. These are all going to be connected to our Lambda functions in one or another way!

### What is AWS Lambda?
> Lambda is a compute service that lets you run code without provisioning or managing servers. Lambda runs your code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, code monitoring and logging. With Lambda, you can run code for virtually any type of application or backend service. All you need to do is supply your code in one of the languages that Lambda supports. [1]

I think AWS Lambda and serverless applications in general is something that will only grow in popularity as more and more people discover the amazing opportunities it can provide. Not only that but also the low cost of running Lambda functions especially for applications with a very variable load.

I my self use AWS Lambda for larger projects. One of the many things that I like about it, is how much time I have saved at operations tasks after going from a platform running on Kubernetes to a completely serverless platform. Both development and deployment time have also gone down a lot!

There are still some limitations like timeout (after max 15 min) etc. that can be an obstacle for migrating applications to serverless, but at the same time you should think about if the applications themselves can be written in another way to leverage the speed and scalability you get with Lambda functions.

### Course topics
- Intro to AWS Lambda
- Creating our first Lambda Function
- Logs using CloudWatch
- Lambda and DynamoDB
- Lambda triggers:
  - SQS
  - S3
- API Gateway:
  - POST - Write object to DB
  - GET - Get object from DB
  - REDIRECT - Redirect users to external resource.
  - JSON request body validation
  - Cognito

### References
1. [AWS Lambda - AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)