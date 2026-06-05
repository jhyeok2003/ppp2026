import random


def play_hangman(secret_word):
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display_word = ""
        for char in secret_word:
            if char in guessed_letters:
                display_word += char
            else:
                display_word += "_"

        print(f"단어: {display_word} (남은 기회: {attempts})")

        if "_" not in display_word:
            return True

        guess = input("알파벳 하나를 입력하세요: ").lower()

        if guess in guessed_letters:
            print("이미 입력한 알파벳입니다.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("틀렸습니다!")

    return False


def main():
    words = ["apple", "banana", "python", "orange", "grape"]
    secret_word = random.choice(words)

    print("[행맨 게임 시작]")
    if play_hangman(secret_word):
        print(f"성공! 정답은 {secret_word}이었습니다.")
    else:
        print(f"실패! 정답은 {secret_word}이었습니다.")


if __name__ == '__main__':
    main()