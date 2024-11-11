from agency_swarm import Agent
from .tools.content_idea_generator import ContentIdeaGenerator  # Use relative import
from .tools.markdown_script_writer import MarkdownScriptWriter  # Use relative import

class ContentManager(Agent):
    def __init__(self):
        super().__init__(
            name="Content Manager",
            description="Responsible for generating content ideas and writing scripts.",
            instructions="./instructions.md",
            tools=[ContentIdeaGenerator, MarkdownScriptWriter],
            temperature=0.5,
            max_prompt_tokens=25000,
        )