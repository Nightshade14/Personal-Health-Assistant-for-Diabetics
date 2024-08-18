from fastAPI import FastAPI
from data_schema.Data import Data
from tensorflow import keras
from flask import Flask, request, jsonify, render_template
import pickle
try:
	
	app = FastAPI()

except Exception as e:
	print(e)

@app.get("/")
async def home_page():
	return "Welcome to the Personal Health Assistant for Diabetics project backend !"

@app.post("/predict")
async def predict(request_data: Data):
	from fastapi.encoders import jsonable_encoder
	from fastapi.responses import JSONResponse

	model = keras.models.load_model('annModel')
	standardScaler = pickle.load(open('standardScaler.pkl', 'rb'))
	int_features = [float(x) for x in request.form.values()]
	final_features = [np.array(int_features)]
	final_features = standardScaler.transform(final_features)
	print(final_features)

	prediction = model.predict(final_features)

	output = float(prediction)

	prediction_text = 'Your chances of having diabetes are {0:.2f}%.\n'.format(output*100)

	if (output >= 0.85):
		prediction_text = prediction_text + 'You should consider seeing a doctor.'
	elif(output >= 0.45):
		prediction_text = prediction_text + 'You are likely to develop Diabetes.'
	else:
		prediction_text = prediction_text + 'Congratulations!!!! You are healthy.'
	
	json_compatible_data = jsonable_encoder({"prediction_text": prediction_text})
	return JSONResponse(content=json_compatible_data)

@app.get("/health-check")
async def check_health():
	return "Server is active."