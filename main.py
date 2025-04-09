"""
FastAPI Application for Uploading Multimedia Game Assets

This API allows users to:
- Upload image files (sprites)
- Upload audio files
- Submit player scores

It connects to a MongoDB Atlas database using the Motor async driver.
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import motor.motor_asyncio

load_dotenv()
# Load environment variables from .env file
connectionString = os.getenv("MONGO_URI")


# Initialize the FastAPI app
app = FastAPI()


# Create a MongoDB client and connect to the 'Data' database
client = motor.motor_asyncio.AsyncIOMotorClient(connectionString)
db = client.Data  # 'Data' is the database nam

# Define the schema for player scores using Pydantic
class PlayerScore(BaseModel):
    player_name: str
    score: int
    Date: str


@app.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):

   # Uploads a sprite file (PNG/JPG/JPEG only) to the 'sprites' collection in MongoDB.

    #  Validate file extension
    if not file.filename.endswith(('.png', '.jpg', '.jpeg')):
        raise HTTPException(status_code=400, detail="Invalid file type. Only PNG and JPG files are allowed.")

    # Read file content
    content = await file.read()

    # Save the file as binary data in MongoDB
    sprite_doc = {"filename": file.filename, "content": content}
    result = await db.sprites.insert_one(sprite_doc)

    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}

@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):

    # Uploads an audio file (MP3/WAV only) to the 'audio' collection in MongoDB.

    if not file.filename.endswith(('.mp3', '.wav')):
        raise HTTPException(status_code=400, detail="Invalid file type. Only MP3 and WAV files are allowed.")
 
    content = await file.read()
    audio_doc = {"filename": file.filename, "content": content}
    result = await db.audio.insert_one(audio_doc)

    return {"message": "Audio file uploaded", "id": str(result.inserted_id)}


@app.post("/player_score")
async def add_score(score: PlayerScore):
    #Submits a player's score and stores it in the 'scores' collection.
    # Convert Pydantic model to dictionary
    score_doc = score.dict()

    # Insert into the 'scores' collection
    result = await db.scores.insert_one(score_doc)
    return {"message": "Score recorded", "id": str(result.inserted_id)}
