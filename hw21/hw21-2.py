import random
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt


def gugudan_correct():
    console = Console()
    a = random.randint(2, 9)
    b = random.randint(1, 9)

    try:
        ans = Prompt.ask(f"[bold yellow]{a} x {b}[/bold yellow]의 정답은?")
        return int(ans) == a * b
    except ValueError:
        return False


def main():
    console = Console()
    score = 0

    console.print(Panel("[bold green]구구단 퀴즈를 시작합니다![/bold green]", subtitle="총 2문제"))

    for i in range(2):
        if gugudan_correct():
            score += 50
            console.print("[bold blue]정답입니다! (+50점)[/bold blue]\n")
        else:
            console.print("[bold red]틀렸습니다![/bold red]\n")

    console.print(Panel(f"[bold white]최종 점수: {score}점[/bold white]", title="결과"))


if __name__ == '__main__':
    main()