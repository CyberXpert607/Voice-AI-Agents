import os
import httpx
from dotenv import load_dotenv
from livekit.agents import function_tool


load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not OPENWEATHER_API_KEY:
    raise RuntimeError("OPENWEATHER_API_KEY not found in environment")

@function_tool(
    name="get_weather",
    description="Get current weather for a given city"
)
async def get_weather(city: str) -> str:
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
    }

    async with httpx.AsyncClient(timeout=5) as client:
        resp = await client.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"The current temperature in {city} is {temp}°C with {desc}."
