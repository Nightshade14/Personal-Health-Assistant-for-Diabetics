from fastAPI import FastAPI
try:
	
	app = FastAPI()

except Exception as e:
	print(e)

@app.get("/")
def home_page():
	return "Welcome to the router"

@app.get("/health-check")
def check_health():
	return "Server is active."