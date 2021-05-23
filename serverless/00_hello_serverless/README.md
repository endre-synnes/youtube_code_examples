# Prerequisites

- Create an AWS account.
- Generate a set of Access Keys for your IAM user.
- Install the AWS CLI and configure it with your Access Keys.

# Steps
- Install serverless CLI.
- Create a new folder and navigate to it.
- Open the folder in VS Code.
- Create serverless application: `serverless create -t aws-python3` (using the `aws-python3` template).
- Change the default region to `eu-central-1` (just my preference)
- Deploy CloudFormation stack: `sls deploy --aws-profile=youtube` (I'm using a separate AWS profile since I have a few AWS accounts).
- Login to the AWS console to see that the CloudFormation stack is created and that the lambda functions is there.