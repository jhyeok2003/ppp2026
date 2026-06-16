import random
import PySimpleGUI as sg

def gugudan_correct():

    a = random.randint(2, 9)
    b = random.randint(1, 9)

    ans = sg.popup_get_text(f"{a} x {b} = ?")

    try:
        return int(ans) == a * b
    except:
        return False

def main():

    score = 0

    for i in range(2):

        if gugudan_correct():
            score += 50

    sg.popup(f"총 점수는 {score}점입니다.")

if __name__ == '__main__':
    main()