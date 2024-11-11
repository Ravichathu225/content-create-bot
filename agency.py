from dotenv import load_dotenv
import os
from agency_swarm import Agency
from ContentManager.content_manager import ContentManager
from TrendAnalyzerAgent.trend_analyzer import TrendAnalyzerAgent
from YouTubeAnalyzerAgent.youtube_analyzer import YouTubeAnalyzerAgent
import openai  # {{ edit_1 }} Import the openai module


# Load environment variables
load_dotenv()

# Optionally set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

content_manager = ContentManager()
trend_analyzer = TrendAnalyzerAgent()
youtube_analyzer = YouTubeAnalyzerAgent()

agency = Agency([
        content_manager,
        [content_manager, trend_analyzer],
        [content_manager, youtube_analyzer],
        [trend_analyzer, youtube_analyzer]
    ],
    shared_instructions='agency_manifesto.md',
    temperature=0.5,
    max_prompt_tokens=25000
)

if __name__ == "__main__":
    agency.run_demo()  # starts the agency in terminal