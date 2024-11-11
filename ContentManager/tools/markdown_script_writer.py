from agency_swarm.tools import BaseTool
from pydantic import Field

class MarkdownScriptWriter(BaseTool):
    """
    Writes and edits scripts in Markdown format.
    """
    script_content: str = Field(..., description="The content of the script to be written in Markdown.")

    def run(self):
        # Logic to save the script content to a Markdown file
        with open("script.md", "w") as file:
            file.write(self.script_content)
        return "Script saved successfully."

if __name__ == "__main__":
    tool = MarkdownScriptWriter(script_content="# My Script\nThis is a sample script.")
    print(tool.run())