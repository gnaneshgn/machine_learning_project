# machine_learning_project
This is first machine learning project

### Software and account requirments

1. [Github] :-(https://github.com)
2. [Heroku] :-(https://dashboard.heroku.com/login)
3. [VSCODE] :-(https://code.visualstudio.com/download)
4. [GITCLI] :-(https://git-scm.com/downloads)

To setup CI/CD pipeline in heroku we need 3 info
1. HEROKU_EMAIL
2. HEROKU_API_KEY
3. HEROKU_APP_NAME

Build DOCKER Image
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be in lowercase

To list docker images
```
docker images
```

run docker image
```
docker run -p 5000:5000 -e PORT=5000 image-id
```

To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop container-id

```