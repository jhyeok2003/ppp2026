import PySimpleGUI as sg
import time

def countdown(seconds):

    layout = [
        [sg.Text("", key="COUNT", font=("Arial", 30))]
    ]

    window = sg.Window("카운트다운", layout)

    for i in range(seconds, 0, -1):

        event, values = window.read(timeout=1000)

        if event == sg.WIN_CLOSED:
            break

        window["COUNT"].update(str(i))

    window["COUNT"].update("정지!")

    window.read()

    window.close()

def main():

    seconds = sg.popup_get_text("초를 입력하세요")

    try:
        countdown(int(seconds))
    except:
        sg.popup("숫자를 입력하세요")

if __name__ == '__main__':
    main()