# hexagonal-fastapi-sentry-sqlalchemy

Hexagonal Architecture in Python with Sentry, FastAPI and SQLAlchemy on Kubernetes

### Kind
#### create kind cluster
```
kind create cluster --name fastapi-api
```

### Docker
#### create docker image
```
docker build --tag guilhermeia/fastapi-api:v1 .
```

#### run docker image
```
docker run -it -d --name fastapi-api -p 80:80 guilhermeia/fastapi-api:v1
```

#### add tag docker image
```
docker tag <image id> guilhermeia/fastapi-api:v1
```

#### push docker image
```
docker push guilherme/fastapi-api:v1
```

### Kubernetes

#### kubernetes apply
```
kubectl apply -f api.yml
```

#### kubernetes port forward
```
sudo kubectl port-forward fastapi-api-7b98f5bc64-lv8zn 80:80
```

#### kubernetes logs
```
kubectl logs -f fastapi-api-7b98f5bc64-lv8zn
```

### API Docs
```
http://localhost/docs
```

### Tests
```
sh tests.sh
```