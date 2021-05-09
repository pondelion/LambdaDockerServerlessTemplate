```bash
$ direnv allow
```

- build

```bash
$ sudo docker build -t lambda_docker_template_api_auth -f docker/Dockerfile . 
```

- Docker CLI Authentication

```bash
$ sudo aws ecr get-login-password --region ap-northeast-1 | sudo docker login --username AWS --password-stdin ${RESISTORY_ID}.dkr.ecr.ap-northeast-1.amazonaws.com
```

- Create ECR

```bash
$ aws ecr create-repository --repository-name lambda-docker-template-api-auth
```

- Tagging

```bash
$ sudo docker tag lambda_docker_template_api_auth:latest ${RESISTORY_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/lambda-docker-template-api-auth:latest
```

- Push to ECR

```bash
$ sudo docker push ${RESISTORY_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/lambda-docker-template-api-auth:latest
```

- Check image list

```bash
$ aws ecr list-images --repository-name lambda-docker-template-api-auth
```

- deploy

```bash
$ sudo -E sls deploy
```

- test

get ID token  

```bash
$ aws cognito-idp admin-initiate-auth --user-pool-id ap-northeast-1_******** --client-id ********** --auth-flow ADMIN_NO_SRP_AUTH --auth-parameters USERNAME=your_user_name,PASSWORD=*******
```

```bash
$ curl https://********.execute-api.ap-northeast-1.amazonaws.com/dev/api/v1/endpoint_without_auth
{"message": "2"}
```

```bash
$ curl https://********.execute-api.ap-northeast-1.amazonaws.com/dev/api/v1/endpoint_with_auth
{"message":"Unauthorized"}
```

```bash
$ curl https://********.execute-api.ap-northeast-1.amazonaws.com/dev/api/v1/endpoint_with_auth -H "Authorization: [ID_TOKEN]"
{"statusCode": 200, "body": "{\"message\": \"env1\"}", "headers": {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Credentials": "true"}}
```