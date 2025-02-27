# Example testing FusionAuth with Mocking vs Development Server

Example repo for the Why mocking sucks post illustrating testing FusionAuth with mocking vs with the development server.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv)
- [Docker](https://www.docker.com/)


## Test with Mocking 

Use the following command to run mocked tests:

```sh
uv run pytest fusionauth_test_with_mocking.py
```


### Test with FusionAuth Development server

In a new terminal run the following commands to start the FusionAuth development server configured with [Kickstart](https://fusionauth.io/docs/get-started/download-and-install/development/kickstart).

```sh
cd fusionauth
docker compose up
```

In another terminal in the root directory of this project run the tests with the following command:

```sh
uv run pytest fusionauth_test_with_dev_server.py
```
