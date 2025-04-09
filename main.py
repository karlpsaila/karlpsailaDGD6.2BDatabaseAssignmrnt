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
connectionString = os.getenv("MONGO_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(connectionString)
db = client["Data"]  # or whatever your DB name is


# Initialize the FastAPI app
app = FastAPI()

#  Hardcoded credentials to access MongoDB Atlas

# Create a MongoDB client and connect to the 'Data' database
client = motor.motor_asyncio.AsyncIOMotorClient(connectionString)
db = client.Data  # 'Data' is the database name

# Define the schema for player scores using Pydantic
class PlayerScore(BaseModel):
    player_name: str
    score: int

@app.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    """
    Uploads a sprite image file and stores it in the 'sprites' collection.

    Args:
        file (UploadFile): The uploaded image file.

    Returns:
        dict: Message and ID of inserted document.
    """
    # Read file content from the request
    content = await file.read()
    
    # Create document to insert into MongoDB
    sprite_doc = {"filename": file.filename, "content": content}

    # Insert document into the 'sprites' collection
    result = await db.sprites.insert_one(sprite_doc)

    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}

@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    """
    Uploads an audio file and stores it in the 'audio' collection.

    Args:
        file (UploadFile): The uploaded audio file.

    Returns:
        dict: Message and ID of inserted document.
    """
    content = await file.read()
    audio_doc = {"filename": file.filename, "content": content}
    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)}

@app.post("/player_score")
async def add_score(score: PlayerScore):
    """
    Submits a player's score and stores it in the 'scores' collection.

    Args:
        score (PlayerScore): JSON body containing player name and score.

    Returns:
        dict: Message and ID of inserted document.
    """
    # Convert Pydantic model to dictionary
    score_doc = score.dict()

    # Insert into the 'scores' collection
    result = await db.scores.insert_one(score_doc)
    return {"message": "Score recorded", "id": str(result.inserted_id)}
