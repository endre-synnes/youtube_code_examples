# API Gateway request body validation

AWS REST API Gateways has support for a built in request body validation. The video related to this document will go in depth on how you can enable this in your API.


### Setting up request model
Open your API in the AWS Console. Under "Model", hit create. This model object is a JSON schema where you define each field you require to be present (or not) in a request body. The schema also include validation rules as defined in the [JSON Schema Validation](http://json-schema.org/draft/2020-12/json-schema-validation.html).

![API Gateway request model][requestModel]


### Setting up request validation
After we have created a request model we need to use that model to validate request bodies hitting the API endpoint. Find the endpoint in our API and open "Method Execution". Under "Settings" add a request validator that validates request bodies. Under "Request Body" add a new content type and choose our model object as visualised in the picture below.
![API Gateway request validation][requestValidation]


[requestModel]: https://github.com/endre-synnes/python_aws_course/blob/master/images/APIGatewayRequestModel.png?raw=true "API Gateway request model"

[requestValidation]: https://github.com/endre-synnes/python_aws_course/blob/master/images/APIGatewayRequestValidation.png?raw=true "API Gateway request validation"
