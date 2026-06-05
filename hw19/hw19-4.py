import random

def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

def main():
    lotto_result = generate_lotto_numbers()
    print(f"추천 로또 번호: {lotto_result}")

if __name__ == '__main__':
    main()