def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
def main():
    n = int(input("원하는 숫자 n의 값을 입력하세요 1부터 n까지의 합을 구해드립니다: "))
    result = sum_n(n)
    print(f"1부터 {n}까지의 합: {result}")
main()