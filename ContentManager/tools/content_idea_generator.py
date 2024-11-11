from agency_swarm.tools import BaseTool
from pydantic import Field
import openai

class ContentIdeaGenerator(BaseTool):
    """
    Generates content ideas based on analysis.
    """
    topic: str = Field(..., description="The topic for which to generate content ideas.")

    def run(self):
        # Logic to generate content ideas using OpenAI API
        ideas = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Generate content ideas for {self.topic}"}]
        )
        return ideas['choices'][0]['message']['content']

if __name__ == "__main__":
    tool = ContentIdeaGenerator(topic="latest trends")
    print(tool.run())