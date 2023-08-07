![style check](https://github.com/razzor58/http_proxy/actions/workflows/style_check.yaml/badge.svg) ![test](https://github.com/razzor58/http_proxy/actions/workflows/coverage_check.yaml/badge.svg) ![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/razzor58/f13f71ad0ffb0e32726a0d1bdfbfbc82/raw/coverage1.json)

## HTTP proxy implementation
Program implement the test challenge described [here](https://github.com/castlabs/python_programming_task)

### Pre-requirements
 - [docker](https://www.docker.com/products/docker-desktop/) should be installed and running on your machine
 - [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) should be installed on your machine
 - Makefile tools are installed

### Initial setup
 - Clone repository and go to source code directory:
    ```
    git clone https://github.com/razzor58/http_proxy.git
    cd http_proxy
    ```
 - Make sure you set the `SECRET_KEY` in `.env` file
 - Build image
    ```
    make build
    ```
 - Verify the build by executing unit tests
    ```
    make test
    ```
 - Run proxy app
    ```
    make run
    ```

### Using solution

- Open in browser http://0.0.0.0:8080/status to check uptime and number of requests processed
- Send request, via curl for example
    ```
    curl --location 'http://0.0.0.0:8080/test' \
        --header 'Content-Type: application/json' \
        --data '{
        "name": "morpheus",
        "job": "leader"
        }'
    ```

### Restriction:
 - Only `application/json` and `multipart/form-data` can be processed

### Parameters
These options can be overwritten in `.env` file:

- TARGET_URL 
- LOG_LEVEL
- HTTP_PORT
- SECRET_KEY
- TIMEOUT
- MAX_BODY


