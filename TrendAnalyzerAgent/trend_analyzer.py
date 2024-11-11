from agency_swarm import Agent
from .tools.trend_analysis_tool import TrendAnalysisTool  # Use relative import

class TrendAnalyzerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Trend Analyzer Agent",
            description="Analyzes latest trends and identifies content gaps.",
            instructions="./instructions.md",
            tools=[TrendAnalysisTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        )