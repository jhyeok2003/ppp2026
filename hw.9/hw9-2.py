def get_range_list(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result
def main():
    n = int(input("n 입력해주세요 1부터 나열해드리겠습니다: "))
    print(get_range_list(n))
if __name__ == "__main__":
    main()