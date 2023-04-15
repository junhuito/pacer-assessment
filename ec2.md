# Server Prerequisition
### Install requirement
```
sudo yum update -y
sudo yum install docker
```

### Launch Docker
```
sudo service docker start
```

### Pull Repository from AWS ECR
```
sudo docker pull public.ecr.aws/l6l3i2k4/pacer-test:latest
```

### Launch Docker Container Image
```
sudo docker run --rm -d -p 8000:8000/tcp public.ecr.aws/l6l3i2k4/pacer-test:latest
```


# Stop a Docker Container
### Step 1 Find the Running Container ID
```
sudo docker ps
```
### Step 2: Stop the Container ID 
```
sudo docker stop <container-id>
```


