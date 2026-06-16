import random
import PySimpleGUI as sg

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

        if "_" not in display_word:
            return True

        guess = sg.popup_get_text(
            f"단어 : {display_word}\n남은 기회 : {attempts}\n알파벳 입력"
        )

        if guess is None:
            return False

        guess = guess.lower()

        if guess in guessed_letters:

            sg.popup("이미 입력한 알파벳입니다")

            continue

        guessed_letters.append(guess)

        if guess not in secret_word:

            attempts -= 1

            sg.popup("틀렸습니다!")

    return False

def main():

    words = [
        "apple",
        "banana",
        "python",
        "orange",
        "grape"
    ]

    secret_word = random.choice(words)

    if play_hangman(secret_word):

        sg.popup(
            f"성공! 정답은 {secret_word}"
        )

    else:

        sg.popup(
            f"실패! 정답은 {secret_word}"
        )

if __name__ == '__main__':
    main()