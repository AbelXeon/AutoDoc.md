from groq import Groq
from config import GROQ_API_KEY

class ReadmeGenerator:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, project_files):
        # Prepare the context for the AI
        context = ""
        for f in project_files:
            context += f"\n--- File: {f['path']} ---\n{f['content']}\n"

        prompt = f"""
        You are a professional technical writer. Write a high-quality, high-style README.md for this project.
        Include:
        1. A centered header with an emoji.
        2. Badges (Python, License, etc.).
        3. A 'Features' table with emojis.
        4. A file structure tree.
        5. Setup and Usage instructions.

        Project Files Context:
        {context}
        
        Return ONLY the Markdown code. Do not talk.
        """

        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-specdec",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content