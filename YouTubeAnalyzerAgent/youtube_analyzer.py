from agency_swarm import Agent
from .tools.youtube_analysis_tool import YouTubeAnalysisTool  # Use relative import

class YouTubeAnalyzerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="YouTube Analyzer Agent",
            description="Analyzes YouTube channel performance and identifies content gaps.",
            instructions="./instructions.md",
            tools=[YouTubeAnalysisTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        )