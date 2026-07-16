<center>🧙‍♂️ **AI README GENERATOR** 🧙‍♂️</center>
===============================================

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Stars](https://img.shields.io/github/stars/your-username/your-repo-name?style=social)](https://github.com/your-username/your-repo-name)

**Automate your README generation with AI-powered technology!**
===========================================================

### ✨ Key Features

| Feature | Description |
| --- | --- |
| **AI-powered** | Leverages Groq's AI capabilities to generate high-quality READMEs |
| **Customizable** | Allows for custom prompts and project data to tailor the output |
| **Easy to use** | Simply run the script and provide a directory to generate a README |

### 🗂️ Project Structure
```markdown
.
├── core
│   ├── __init__.py
│   ├── generator.py
│   └── scanner.py
├── config.py
├── main.py
└── requirements.txt
```

### 🚀 Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python main.py .
```

### 🛠️ Detailed Architecture

The project consists of the following components:

* `config.py`: Loads environment variables, including the Groq API key.
* `main.py`: Runs the script, scanning the provided directory and generating a README.
* `core/scanner.py`: Scans the project directory, collecting file data and contents.
* `core/generator.py`: Uses the Groq API to generate a README based on the collected project data.

### ⚙️ Configuration

The following environment variables are required:

* `GROQ_API_KEY`: Your Groq API key, loaded from a `.env` file.

### 📚 How It Works

1. **Scanning**: The `CodeScanner` class scans the provided directory, collecting file data and contents.
2. **Generating**: The `ReadmeGenerator` class uses the Groq API to generate a README based on the collected project data.
3. **Saving**: The generated README is saved as `README.md` in the provided directory.
4. **Preview**: The generated README is optionally previewed in the terminal using Rich.

Note: Make sure to replace `your-username` and `your-repo-name` with your actual GitHub username and repository name in the badges.