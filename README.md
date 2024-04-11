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
Run the following docker command to start the api in a safe-ish (still has network access) environment
```bash
docker run -it --rm --readonly --cpus 1.0 --mem 512m -p 8000:8000 safe-app
```

# Example
Here is an example of how to use the API to register a function:
```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "user_func", "code": "def user_func(x):\n\treturn x + 1"}' \
    http://localhost:8000/api/register-function
```

And then to call the function, you can run the following:
```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "user_func", "args": [4]}' \
    http://localhost:8000/api/execute-function
```