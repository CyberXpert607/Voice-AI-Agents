This guide walks you through setting up the Voice AI Agent locally.

1️⃣ Install uv (Python Package Manager)

This project uses UV Package Manager for fast, reproducible Python environments.

```bash
pip install uv
```

Verify installation:
```bash
uv --version
```

2️⃣ Clone the Repository
```bash
git clone https://github.com/CyberXpert607/Voice-AI-Agents.git
```
```bash
cd Voice-AI-Agents
```

3️⃣ Sync the Python Environment

This project does NOT require requirements.txt.

Instead, dependencies are managed via:

`pyproject.toml`

`uv.lock`

Install dependencies
```bash
uv sync
```

This will:

Create a virtual environment automatically

Install exact, locked dependency versions

4️⃣ Create a .env File

Create a .env file in the project root:
```bash
cp .env.example .env
```

Or manually create one if .env.example is not present.
Also make sure to use the command:
```bash
cd src/
uv run python agent.py download-files
```

to install the dependencies needed for the agent to run.

5️⃣ Obtain Required API Keys

This agent requires multiple external services.

🔹 OpenAI (LLM)

Used for reasoning and conversation.

Go to: `https://platform.openai.com/`

`Create an account`

`Generate an API key`

`Copy the key`

🔹 Groq (LLM / optional TTS)

Used for ultra-fast inference.

Go to: `https://console.groq.com/`

`Create an account`

`Generate an API key`

`Copy the key`

🔹 ElevenLabs (Text-to-Speech)

Used for high-quality voice synthesis.

Go to: `https://elevenlabs.io/`

`Create an account`

`Generate an API key`

`Copy the key`

🔹 LiveKit (Realtime Audio / Rooms)

Go to: `https://cloud.livekit.io/`

`Create a project`

Copy:

`API Key`

`API Secret`

`WebSocket URL`

6️⃣ Configure Environment Variables

Open your .env file and fill in the values:

# LLM Providers

OPENAI_API_KEY=your_openai_api_key_here

GROQ_API_KEY=your_groq_api_key_here

# Text-to-Speech

ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

# LiveKit

LIVEKIT_API_KEY=your_livekit_api_key_here

LIVEKIT_API_SECRET=your_livekit_api_secret_here

LIVEKIT_URL=wss://your-livekit-url.livekit.cloud

7️⃣ Run the Agent

Activate the environment and start the agent:
```bash
cd src/
uv run python agent.py console
```
