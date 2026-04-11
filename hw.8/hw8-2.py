def gugudan(dan):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")

def main():
    dan = int(input("몇단을 알려드릴까요? "))
    gugudan(dan)

main()