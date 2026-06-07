import random
from rich.console import Console
from rich.panel import Panel


def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers


def main():
    console = Console()
    lotto_result = generate_lotto_numbers()

    result_str = "  ".join([f"[bold yellow]{num}[/bold yellow]" for num in lotto_result])

    console.print(Panel(result_str, title=" 이번 주 추천 로또 번호 ", expand=False))


if __name__ == '__main__':
    main()