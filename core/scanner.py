import os

class CodeScanner:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.ignore_list = {'.git', '__pycache__', 'venv', '.env', '.vscode', 'node_modules'}

    def scan(self):
        project_data = []
        for root, dirs, files in os.walk(self.target_dir):
            dirs[:] = [d for d in dirs if d not in self.ignore_list]
            for file in files:
                if file.endswith(('.py', '.js', '.html', '.css')) or file == 'requirements.txt':
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, self.target_dir)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = "".join(f.readlines()[:100]) # Get first 100 lines
                        project_data.append({"path": relative_path, "content": content})
                    except Exception:
                        continue
        return project_data