import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from data_model.educational_path import EducationalPath
from data_model.learning_object import LearningObject
from data_model.path_prediction_request import PathPredictionRequest
from data_model.path_prediction_response import PathPredictionResponse

app = FastAPI(
    title="Path Prediction API",
    description=None,
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "HKA",
        "url": "https://www.h-ka.de/iaf/merlot",
        "email": "foo@bar.de",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    })


security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"foo"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"bar"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/educational_paths/")
async def info():
    return {"api":"educational_paths", "version":"1.0.0"}


@app.post("/educational_paths/", response_model=PathPredictionResponse)
async def predict(prediction_request: PathPredictionRequest, credentials: HTTPBasicCredentials = Depends(get_current_user)):

    # for testing
    educationalPath = EducationalPath(
        start = LearningObject(name="Abitur - Fichte Gymnasium Karlsruhe", description="Lorem ipsum"),
        end = LearningObject(name="Master Informatik - HKA", description="Lorem ipsum"),
        stations=[
            LearningObject(name="Bachelor Informatik - HKA", description="Lorem ipsum")
        ]
    )

    prediction_response = PathPredictionResponse(educationals_paths=[educationalPath])
    
    return prediction_response
