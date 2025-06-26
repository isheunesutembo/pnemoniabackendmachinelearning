
from fastapi import FastAPI, File, UploadFile
from keras.src.applications.convnext import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import get_file
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from tensorflow import expand_dims
from tensorflow.nn import softmax
from tensorflow.nn import sigmoid
from numpy import argmax
from numpy import max
from numpy import array
from json import dumps
from uvicorn import run
import os
import uvicorn
from io import BytesIO
from PIL import Image


app=FastAPI()

model_dir="pneumonia_model.h5"
model=load_model(model_dir)


@app.post("/predict")
async def pneumonia_prediction(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(BytesIO(image_data)).convert("RGB")
    image = image.resize((224, 224))


    classes = ['NORMAL', 'PNEUMONIA']

    img_array=img_to_array(image)
    img_array = img_array / 255.0
    img_array=expand_dims(img_array,axis=0)
    pred=model.predict(img_array)

    score = float(pred[0][0])  # single float output
    class_prediction = "PNEUMONIA" if score > 0.5 else "NORMAL"
    model_score = round(float(score if score > 0.5 else 1 - score) * 100, 2)

    return {
        "prediction":class_prediction,
        "scoreconfidence":model_score
    }


if __name__=="__main__":
    port=int(os.environ.get("PORT",3000))
    uvicorn.run(app, host="127.0.0.1", port=port)
