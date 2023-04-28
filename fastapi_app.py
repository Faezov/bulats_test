

from fastapi import FastAPI
from model import model # Change this to match your model import statement

app = FastAPI()

@app.post("/predict/")
def predict(data: str):
    prediction = model.predict(data)
    return {"prediction": prediction}
