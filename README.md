# path-prediction-api

## Installation
    conda create -n path-prediction-api
  
    conda activate path-prediction-api
  
    pip install "fastapi[all]"

    pip install git+https://github.com/thorsten-zylowski-hka/merlot-data-models.git

## Running the API
    uvicorn api:app --reload

## API documentation
host:port/docs

Example: localhost:8000/docs
