from fastAPI import FastAPI
from data_schema.Data import Data
try:
	
	app = FastAPI()

except Exception as e:
	print(e)

@app.get("/")
async def home_page():
	return "Welcome to the Personal Health Assistant for Diabetics project backend !"

@app.post("/predict")
async def predict(request_data: Data):
	return "/predict endpoint return message"

@app.get("/health-check")
async def check_health():
	return "Server is active."