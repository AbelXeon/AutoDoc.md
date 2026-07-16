import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from core.scanner import CodeScanner
from core.generator import ReadmeGenerator

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
    with console.status("[bold magenta]Wizard is thinking (AI Generation)...") as status:
        generator = ReadmeGenerator()
        readme_content = generator.generate(files)
    
    # 3. SAVING
    output_path = os.path.join(target_dir, "README_GENERATED.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    console.print(Panel(f"[bold green]✨ SUCCESS![/bold green]\nREADME created at: [yellow]{output_path}[/yellow]"))
    
    # Preview it in terminal
    if console.confirm("Do you want to preview the README in terminal?"):
        console.print(Markdown(readme_content))

if __name__ == "__main__":
    run()