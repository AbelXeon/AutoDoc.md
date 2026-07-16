from groq import Groq
from config import GROQ_API_KEY

class ReadmeGenerator:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, project_files):
        context = ""
        for f in project_files:
            context += f"\n--- File: {f['path']} ---\n{f['content']}\n"

        # This prompt is now much more "aggressive" about quality and detail
        prompt = f"""
        You are an elite Technical Writer and Software Architect. 
        Write a MASTERPIECE README.md for this project based on the code provided.

        STRICT RULES:
        1. VISUALS: Use high-quality GitHub badges, emojis, and clean dividers.
        2. LOGIC: Include a 'How It Works' section that explains the actual technical logic of the code.
        3. STRUCTURE: 
           - Centered Title with a cool icon.
           - Professional Badges.
           - Short, catchy description.
           - '✨ Key Features' table.
           - '🗂️ Project Structure' (ASCII tree).
           - '🚀 Quick Start' (with code blocks).
           - '🛠️ Detailed Architecture' (explain how the files interact).
           - '⚙️ Configuration' (Environment variables).
        4. STYLE: Make it look like a top-tier Open Source project (like FastAPI or Tailwind).
        
        Project Source Data:
        {context}
        
        Return ONLY the Markdown code. Do not include any intro/outro text.
        """

        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[{"role": "system", "content": "You output only valid Markdown."},
                      {"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content