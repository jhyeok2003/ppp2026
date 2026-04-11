def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)
def main():
    nums = input("한킨씩 띄어쓰며 숫자를 여러개 입력해주세요: ").split()
    nums = [int(n) for n in nums]
    print(f"평균: {average(nums):.1f}")
if __name__ == "__main__":
    main()