def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False
def main():
    y = int(input("연도 입력해주세요 윤년인지 봐드리겠습니다.: "))
    if is_leap_year(y):
        print("윤년입니다.")
    else:
        print("윤년이 아닙니다.")
if __name__ == "__main__":
    main()