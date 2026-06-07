import time
from rich.console import Console
from rich.panel import Panel

def countdown(seconds):
    console = Console()
    for i in range(seconds, 0, -1):
        console.print(Panel(f"[bold cyan]{i:3d}[/bold cyan]", title="카운트다운", expand=False), end="\r")
        time.sleep(1)
    console.print("\n[bold red]정지![/bold red]")

def main():
    countdown(10)

if __name__ == '__main__':
    main()