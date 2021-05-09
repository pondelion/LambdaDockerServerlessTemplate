```bash
$ direnv allow
```

- build

```bash
$ sudo docker build -t lambda_docker_template_api_public -f docker/Dockerfile . 
```

- Docker CLI Authentication

```bash
$ sudo aws ecr get-login-password --region ap-northeast-1 | sudo docker login --username AWS --password-stdin ${RESISTORY_ID}.dkr.ecr.ap-northeast-1.amazonaws.com
```

- Create ECR

```bash
$ aws ecr create-repository --repository-name lambda-docker-template-api-public
```

- Tagging

```bash
$ sudo docker tag lambda_docker_template_api_public:latest ${RESISTORY_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/lambda-docker-template-api-public:latest
```

- Push to ECR

```bash
$ sudo docker push ${RESISTORY_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/lambda-docker-template-api-public:latest
```

- Check image list

```bash
$ aws ecr list-images --repository-name lambda-docker-template-api-public
```

- deploy

```bash
$ sudo -E sls deploy
```
