import json
import os
import urllib3

aws_session_token = os.environ['AWS_SESSION_TOKEN']
port = 2773
parameter_name = "extension-test"
http = urllib3.PoolManager()

def retrieve_ssm_parameter():
    url = f"http://localhost:{port}/systemsmanager/parameters/get/?name={parameter_name}"
    headers = {"X-Aws-Parameters-Secrets-Token": aws_session_token}
    response = http.request("GET", url, headers=headers)
    json_data = json.loads(response.data)
    return json_data

def lambda_handler(event, context):
    parameter = retrieve_ssm_parameter()
    return parameter

