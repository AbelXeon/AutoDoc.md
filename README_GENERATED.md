<center>🧙‍♂️ **AI README GENERATOR**</center>

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Requirements](https://img.shields.io/badge/Requirements-Installable-orange.svg)](requirements.txt)

## Features
| Feature | Description | Status |
| --- | --- | --- |
| 📄 **AI Generation** | Generate high-quality README files using AI | ✅ |
| 📁 **File Scanning** | Scan project files and extract relevant information | ✅ |
| 📝 **Markdown Support** | Generate Markdown code for easy formatting | ✅ |
| 📊 **Badges** | Include badges for Python, License, and more | ✅ |
| 📂 **File Structure Tree** | Display file structure tree for easy navigation | ✅ |

## File Structure
```markdown
.
├── config.py
├── core
│   ├── generator.py
│   ├── __init__.py
│   └── scanner.py
├── main.py
├── README.md
└── requirements.txt
```

## Setup and Usage
1. **Install Requirements**: Run `pip install -r requirements.txt` to install the required packages.
2. **Set Environment Variables**: Create a `.env` file with your Groq API key: `GROQ_API_KEY=YOUR_API_KEY`.
3. **Run the Generator**: Run `python main.py .` to generate a README file for the current directory.
4. **Preview the README**: The generator will ask if you want to preview the README in the terminal. Type `y` to preview.

Note: Make sure to replace `YOUR_API_KEY` with your actual Groq API key.