import random

def gugudan_correct():
    a = random.randint(2, 9)
    b = random.randint(1, 9)
    try:
        ans = input(f"{a} x {b} = =>>? ")
        return int(ans) == a * b
    except ValueError:
        return False

def main():
    score = 0
    for i in range(2):
        if gugudan_correct():
            score += 50
    print(f"총 점수는 {score}입니다.")

if __name__ == '__main__':
    main()