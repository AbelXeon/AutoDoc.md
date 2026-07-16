import sys
import os
import config
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Confirm, Prompt
from core.scanner import CodeScanner
from core.generator import ReadmeGenerator

console = Console()

def run():
    console.clear()
    console.print(Panel.fit("[bold magenta]🧙‍♂️ WIZARD: AI README GENERATOR[/bold magenta]", subtitle="By AbelXeon"))

    # Check for saved API Key
    api_key = config.get_api_key()
    
    if not api_key:
        console.print("[bold yellow]First time setup: No API Key found![/bold yellow]")
        api_key = Prompt.ask("Please paste your Groq API Key")
        config.save_api_key(api_key)
        console.print("[bold green]Key saved successfully! You won't have to enter it again.[/bold green]\n")

    if len(sys.argv) < 2:
        console.print("[red]❌ Usage: wizard .[/red]")
        return

    target_dir = sys.argv[1]
    user_pref = Prompt.ask("[bold yellow]Any specific style instructions?[/bold yellow]", default="Make it professional and highly detailed")
    
    # 1. SCANNING
    with console.status("[bold cyan]Scanning project files...") as status:
        scanner = CodeScanner(target_dir)
        files = scanner.scan()
        console.log(f"✅ Found {len(files)} files to analyze.")

    # 2. GENERATING
    with console.status("[bold magenta]Wizard is weaving the documentation...[/bold magenta]") as status:
        generator = ReadmeGenerator(api_key)
        readme_content = generator.generate(files, user_pref)
    
    # 3. SAVING
    output_path = os.path.join(target_dir, "README.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    console.print(Panel(f"[bold green]✨ SUCCESS![/bold green]\nREADME updated: [yellow]{output_path}[/yellow]"))
    
    if Confirm.ask("Do you want to preview the result?"):
        console.print(Markdown(readme_content))

if __name__ == "__main__":
    run()