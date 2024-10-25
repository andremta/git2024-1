# Webcounter Project
Simple Python Webcounter with redis server

## Project tree

```
📦webcounter
 ┣ 📂static
 ┃ ┗ 📜main.css
 ┣ 📂templates
 ┃ ┗ 📜index.html
 ┣ 📜redis_helper.py
 ┣ 📜__init__.py
 ┗ 📜__main__.py
```

---
## Developer tasks

### Local run

    $ python -m webcounter

---
## Manual server operations

### Build
    docker build -t <docker-id>/webcounter:latest .

### Run Dependencies
    docker run -d  -p 6379:6379 --name redis --rm redis:alpine

### Deploy
    docker run -d --rm -p 80:5000 --name webcounter --link redis -e REDIS_URL=redis <docker-id>/webcounter:latest

---
## Cluster operations

### Push to docker repository

    docker login 
    docker push <docker-id>/webcounter:latest

### Create a docker swarm cluster

    docker swarm init

### Deploy stack app 

    docker stack deploy --compose-file docker-compose.yml app

---
## Automated operations CI/CD


### GitLab Variables 
Variables are in: `Gitlab » Settings » CI/CD » Variables`

Create Gitlab variables with docker credentials: `$USER` and `$PASSWORD`
 
### Get gitlab token and change `--registration-token` bellow

Token are in: `Gitlab » Settings » CI/CD » Runners`

    New Project runner

### Instal gitlab-runner on managers

    sudo apk add gitlab-runner

### Gitlab register at server

Register shell executer for build and deploy on manager1

gitlab-runner register  \
    --non-interactive \
    --url https://gitlab.com  \
    --executor "shell" \
    --tag-list "shell-build-server,shell-deploy-server" \
    --token glrt-DxjA37pyEQXXwTzmeGy3

### Run runner

    gitlab-runner run
