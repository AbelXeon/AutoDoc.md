from groq import Groq

class ReadmeGenerator:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def generate(self, project_files, user_instruction=""):
        context = ""
        for f in project_files:
            context += f"\n--- File: {f['path']} ---\n{f['content']}\n"

        # The "Masterpiece" Prompt
        prompt = f"""
        You are an elite Technical Writer and Software Architect. 
        Write a MASTERPIECE README.md for this project based on the code provided.

        STRICT RULES:
        1. VISUALS: Use high-quality GitHub badges, emojis, and clean dividers (---).
        2. NO DECORATIONS: Do NOT use '=====' or '-------' lines. Use '#' for headers.
        3. LOGIC: Include a 'How It Works' section that explains the actual technical logic of the code.
        4. STRUCTURE: 
           - Centered Title with a cool icon.
           - Professional Badges (Python, MIT, etc.).
           - Short, catchy description.
           - '✨ Key Features' table.
           - '🗂️ Project Structure' (ASCII tree).
           - '🚀 Quick Start' (with code blocks).
           - '🛠️ Detailed Architecture' (how files interact).
           - '⚙️ Configuration' (Environment variables).
        
        USER SPECIAL INSTRUCTIONS: {user_instruction}

        Project Source Data:
        {context}
        
        Return ONLY the Markdown code. No intro/outro text.
        """

        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[{"role": "system", "content": "You are a Markdown expert. Output ONLY valid Markdown."},
                      {"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content