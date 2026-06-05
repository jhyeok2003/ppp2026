import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"{i:3d}", end="\r")
        time.sleep(1)
    print("정지!")

def main():
    countdown(10)

if __name__ == '__main__':
    main()