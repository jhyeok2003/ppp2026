def main():
    num_list = []

    while True:
        user_input = input("X=? ")

        if user_input == "-1":
            break

        try:
            num = int(user_input)
            if num > 0:
                num_list.append(num)
        except ValueError:
            pass

    count = len(num_list)

    if count > 0:
        avg = sum(num_list) / count
        print(f"입력된 값은 {num_list} 입니다. 총 {count}개의 자연수가 입력되었고, 평균은 {avg:.1f}입니다.")
    else:
        print("입력된 자연수가 없습니다.")


if __name__ == '__main__':
    main()