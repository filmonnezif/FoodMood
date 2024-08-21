from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Add your Quasar dev server URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MoodData(BaseModel):
    mood: str
    time: str
    type: str

@app.post("/process_mood")
async def process_mood(data: MoodData):
    # Process the mood data here
    result = f"Processed: {data.mood} at {data.time} ({data.type})"
    print (result)
    return {"result": result}
