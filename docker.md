# ECR Login
```
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/l6l3i2k4
```

# Docker Build Step
### Build the image
```
docker build -t pacer-test .
```
### Tag the image
```
docker tag pacer-test:latest public.ecr.aws/l6l3i2k4/pacer-test:latest
```
### Push the image
```
docker push public.ecr.aws/l6l3i2k4/pacer-test:latest
```