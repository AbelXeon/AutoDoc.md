import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Confirm  # Fixed import
from core.scanner import CodeScanner
from core.generator import ReadmeGenerator
import config 


console = Console()

def run():
    console.clear()
    console.print(Panel.fit("[bold magenta]🧙‍♂️ WIZARD: AI README GENERATOR[/bold magenta]", subtitle="By AbelXeon"))

    if len(sys.argv) < 2:
        console.print("[red]❌ Error: Provide a directory. Usage: python main.py .[/red]")
        return

    target_dir = sys.argv[1]
    
    # 1. SCANNING
    with console.status("[bold cyan]Scanning project files...") as status:
        scanner = CodeScanner(target_dir)
        files = scanner.scan()
        console.log(f"✅ Found {len(files)} files to analyze.")

    # 2. GENERATING
    with console.status("[bold magenta]Wizard is weaving the documentation...[/bold magenta]") as status:
        generator = ReadmeGenerator()
        readme_content = generator.generate(files)
    
    # 3. SAVING (Now saves as README.md and overwrites)
    output_path = os.path.join(target_dir, "README.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    console.print(Panel(f"[bold green]✨ SUCCESS![/bold green]\nREADME updated at: [yellow]{output_path}[/yellow]"))
    
    # 4. PREVIEW (Fixed the crash here)
    if Confirm.ask("Do you want to preview the result in your terminal?"):
        console.print(Markdown(readme_content))

    api_key = config.get_api_key()
    if not api_key:
        console.print("[bold yellow]First time setup![/bold yellow]")
        api_key = Prompt.ask("Please enter your Groq API Key")
        config.save_api_key(api_key)
        # Reload the key into the generator
        os.environ["GROQ_API_KEY"] = api_key


if __name__ == "__main__":
    run()