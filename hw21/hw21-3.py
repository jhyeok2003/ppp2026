import random
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt


def play_hangman(secret_word):
    console = Console()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display_word = ""
        for char in secret_word:
            if char in guessed_letters:
                display_word += char + " "
            else:
                display_word += "_ "

        console.print(Panel(f"[bold magenta]{display_word}[/bold magenta]", title=f"현재 단어 상태 (남은 기회: {attempts})"))

        if "_" not in display_word:
            return True

        guess = Prompt.ask("알파벳 하나를 입력하세요").lower()

        if guess in guessed_letters:
            console.print("[bold yellow]이미 입력한 알파벳입니다.[/bold yellow]\n")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            console.print("[bold red]틀렸습니다![/bold red]\n")
        else:
            console.print("[bold green]맞췄습니다![/bold green]\n")

    return False


def main():
    console = Console()
    words = ["apple", "banana", "python", "orange", "grape"]
    secret_word = random.choice(words)

    console.print(Panel("[bold white]행맨 게임을 시작합니다![/bold white]", title="Hangman"))

    if play_hangman(secret_word):
        console.print(Panel(f"[bold green]성공! 정답은 {secret_word}이었습니다.[/bold green]"))
    else:
        console.print(Panel(f"[bold red]실패! 정답은 {secret_word}이었습니다.[/bold red]"))


if __name__ == '__main__':
    main()