# Cognito OAuth2 - API Gateway

### Cognito setup
- Create a Cognito User Pool and a App Client
- Set up domain
- Set up resource server
- Update App Client settings
  - Use cognito user pool
  - Add implicit workflow (just for demo)
  - add Allowed custom scopes

## API Gateway setup
- Add new Authorizer
- Use new Authorizer in API Resource.
- Add custom OAuth scopes
- DEploy API


## Test using Postman
- Use postman built in OAuth2 setup
- Do POST request with and without Authorization header.