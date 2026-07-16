<div align="center">

# 🧙‍♂️ Wizard: The AI README Architect

**Stop writing documentation. Start weaving masterpieces.**  
*An intelligent CLI tool that scans your codebase and generates high-style, professional READMEs instantly.*

![Python](https://img.shields.io/badge/python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/AI-Groq-orange?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)

</div>

---

## ✨ Why Wizard?

Writing a README is the most boring part of coding. **Wizard** solves this by acting as a Technical Architect. It doesn't just list files; it reads your logic, understands your architecture, and styles your documentation like a 10k-star GitHub repository.

| Feature | Description |
| :--- | :--- |
| 🧠 **Deep Context** | Scans all `.py`, `.js`, `.html`, and `.css` files to understand your logic. |
| 🎭 **Custom Persona** | Tell the Wizard to be "Funny," "Professional," or "Minimalist." |
| 🚀 **Global Access** | Run it from anywhere on your system like `yt-dlp`. |
| 🛡️ **Zero-Config Key** | Saves your API key locally—enter it once, use it forever. |

---

## 🗂️ Project Structure

```text
wizard/
├── core/
│   ├── scanner.py      # The "Eyes": Scans and filters your codebase.
│   └── generator.py    # The "Brain": Crafts the AI prompt and styles.
├── main.py             # The "Face": Beautiful terminal interface (Rich).
├── config.py           # The "Memory": Handles persistent API keys.
└── requirements.txt    # The "Gear": Necessary libraries.

🛠️ How It Works
The Scanner (Eyes): The tool walks through your directory, ignoring "trash" like venv, .git, and __pycache__. It extracts the most important parts of your code.
The Generator (Brain): It builds a massive prompt including your code context and sends it to the Groq Llama 3.3-70b model.
The Weaver: The AI returns structured Markdown with badges, tables, and architecture breakdowns, which is then saved as README.md.

🚀 Installation & Developer Setup
If you want to customize the Wizard or build your own version:
1. Clone & Environment
git clone https://github.com/AbelXeon/wizard.git
cd wizard
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt

2. Customizing the AI Prompt
You can change the "style" of the generated README by editing core/generator.py. Find the prompt variable and tell the AI exactly how you want it to behave!

3. One-Time API Setup
Run the script:code

python main.py .

The Wizard will ask for your Groq API Key. It saves this to ~/.wizard_config so you never have to provide it again.

📦 Building the Global EXE
To use the Wizard like a professional system tool (no python command needed):
Compile to EXE:


pyinstaller --onefile --name wizard main.py
Make it Global:
Move dist/wizard.exe to a folder (e.g., C:\MyTools).
Add C:\MyTools to your Windows System PATH.
Use it Anywhere:
Open any folder on your computer and simply type:


wizard .
📝 Notes & Persistence
Security: Your API key is stored locally in your User profile and is never uploaded.
Overwrite: Running the Wizard will automatically overwrite your existing README.md—always backup if you have manual notes!
<div align="center">
Created with ❤️ by <b>AbelXeon</b>
</div>
```
