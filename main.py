from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes import router
import uvicorn

app = FastAPI()

app.include_router(router)

origins = [
    "*",
    #"http://localhost",
    #"http://localhost:8000",
    #"http://127.0.0.1:8000",
    #"https://devreporting.kgaswe.ac.bw",
    #"https://reporting.kgaswe.ac.bw",
    # "https://billing-api.kgaswe.ac.bw"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"Hello": "World"}

if __name__ == '__main__':
    uvicorn.run(app="__main__:app", host="0.0.0.0", reload=True, port=4000)  
    # uvicorn.run(app="__main__:app", host="34.235.226.214", reload=True, port=4000)  