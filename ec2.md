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
### Step 1: Find the Running Container ID
```
sudo docker ps
```
### Step 2: Stop the Container ID 
```
sudo docker stop <container-id>
```


# Disable sudo for ec2-user
### Run the following command to open the sudoers file in the vi editor:
```
sudo visudo
```

### Add the following line to the file to give the ec2-user passwordless sudo privileges:
```
ec2-user ALL=(ALL) NOPASSWD:ALL
```

# Got permission denied while trying to connect to the Docker daemon socket
### Add the current user to the docker group:
```
sudo usermod -aG docker $USER
```
### Verify that the user is now part of the docker group:
```
groups $USER
```
### Ensure that the permissions on the Docker socket file are set correctly:
```
sudo chmod 666 /var/run/docker.sock
```