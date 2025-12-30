from fastapi import FastAPI
from pydantic import BaseModel
from livekit import api
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

class TokenRequest(BaseModel):
    room: str
    identity: str

@app.post("/token")
def token(req: TokenRequest):
    token = (
        api.AccessToken(
            os.environ["LIVEKIT_API_KEY"],
            os.environ["LIVEKIT_API_SECRET"],
        )
        .with_identity(req.identity)
        .with_grants(
            api.VideoGrants(
                room_join=True,
                room=req.room,
            )
        )
        .to_jwt()
    )

    return {
        "url": os.environ["LIVEKIT_URL"],
        "token": token,
    }
