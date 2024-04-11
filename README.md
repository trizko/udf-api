# Python UDF API
API for running user defined python functions.

# Requirements
- Docker

# Installation
Run the following command to build the docker image locally:
```bash
docker build -t safe-app .
```

# Usage
Run the following docker command to start the api in a safe-ish environment
```bash
docker run -it --rm --readonly --cpus 1.0 --mem 512m -p 8000:8000 safe-app
```