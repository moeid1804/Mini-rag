# mini-rag
This is a minimal implementation of the RAG model for question answering

## Requirements
-Python 3.8 or later

### Install python using MiniConda
1) Download and install MiniConda from [here] (https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html).
2) create a new environment using the following command:
````bash
$ conda create -n mini-rag python=3.8
````
3) activate the environment:
````bash
$ conda activate mini-rag
````
## Installation
### install the required pachages
````bash
$ pip install -r requirements.txt
````
### Setup the environment variables
````bash
$ cp .env.example .env
````
set your environment variables in `env` file. like `APP_NAME`,`OPEN_API_KEY`

### Run Project
````bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 8000
````
