from livekit.agents import Agent, AgentServer, AgentSession, room_io, JobProcess, JobContext, cli
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.plugins import groq, silero, noise_cancellation, elevenlabs
from livekit import rtc
import asyncio
from dotenv import load_dotenv
from prompts import INSTRUCTIONS
import logging

load_dotenv()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Shayla(Agent):
    def __init__(self):
        super().__init__(
            instructions=INSTRUCTIONS
        )


server  = AgentServer()


def init_modules(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()
    logger.info("Heavy modules loaded into memory for optimisation")

server.setup_fnc = init_modules

@server.rtc_session()
async def agent_runtime(ctx: JobContext):
    vad: silero.VAD = ctx.proc.userdata["vad"]

    logger.info("Session starting for room: %s", ctx.room.name)
    session = AgentSession(
        stt=groq.STT(),
        llm= groq.LLM(), #Or use any other model you prefer more details in README.md
        tts= elevenlabs.TTS(voice_id="21m00Tcm4TlvDq8ikWAM"),
        preemptive_generation=True,
        turn_detection= MultilingualModel(),
        vad = vad,
    )

    try:
        await session.start(
            room=ctx.room,
            agent=Shayla(),
            room_options= room_io.RoomOptions(
                audio_input = room_io.AudioInputOptions(
                    noise_cancellation = lambda params: noise_cancellation.BVCTelephony()
                    if params.participant.kind == rtc.ParticipantKind.PARTICIPANT_KIND_SIP else noise_cancellation.BVC(),
                ),
                audio_output = room_io.AudioOutputOptions(),
            ),
        )
    except Exception as e:
        logger.critical("Failed to start agent session: %s", e)
        return

    logger.info("Agent takes the first turn in speaking")
    #await asyncio.sleep(.3)
    await session.generate_reply(instructions="Greet the user and ask whether they need assistance in any way possible")


if __name__ == "__main__":
    cli.run_app(server)

