# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI, UploadFile
from model import predict_image
import numpy as np
import pickle
import pandas as pd
from PIL import Image
# 2. Create the app object
app = FastAPI()
# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000


@app.get('/')
def index():
    return {'message': 'Hello!!!!, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere


@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence


@app.post('/upload')
async def predict_disease(file: UploadFile):
    print('On Server')
    image_data = await file.read()
    return {predict_image(image_data)}

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

# uvicorn app:app --reload
