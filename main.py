from fastapi import FastAPI
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import get_file
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from tensorflow import expand_dims
from tensorflow.nn import softmax
from numpy import argmax
from numpy import max
from numpy import array
from json import dumps
from uvicorn import run
import os

app=FastAPI()

model_dir=""
model=load_model(model_dir)


@app.post("/predict")
async def pneumonia_prediction(image_link:str=""):
    if image_link == "":
        return {"message":"Please provide Image Link"}

    img_path=get_file(origin=image_link)
    img=load_img(img_path,target_size=(224,224))
    img_array=img_to_array(img)
    img_array=expand_dims(img_array,axis=0)
    pred=model.predict(img_array)

    score=softmax(pred[0])

    class_prediction=class_predictions[argmax(score)]

    model_score=round(max(score)*100,2)

    return {
        "prediction":class_prediction,
        "scoreconfidence":model_score
    }


if __name__=="__main__":
    port=int(os.environ.get("PORT",5000))
    run(host="0.0.0.0",port=port)
