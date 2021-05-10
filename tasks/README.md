
```bash
$ direnv allow
```


- build

```bash
$ sudo docker build -t lambda_docker_template1 -f docker/lambda/crawl/Dockerfile . 
```

- Docker CLI Authentication

```bash
$ sudo aws ecr get-login-password --region ap-northeast-1 | sudo docker login --username AWS --password-stdin ${RESISTORY_ID}.dkr.ecr.ap-northeast-1.amazonaws.com
```

- Create ECR

```bash
$ aws ecr create-repository --repository-name lambda-docker-template1 --image-scanning-configuration scanOnPush=true
```

- Tagging

```bash
$ sudo docker tag lambda_docker_template1:latest ${RESISTORY_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/lambda-docker-template1:latest
```

- Push to ECR

```bash
$ sudo docker push ${RESISTORY_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/lambda-docker-template1:latest
```

- Check image list

```bash
$ aws ecr list-images --repository-name lambda-docker-template1
```

- deploy

```bash
$ sudo -E sls deploy
```
