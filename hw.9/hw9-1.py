def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)
def main():
    nums = input("숫자 입력(한칸씩 띄어쓰기하며 여러개를 입력하시오): ").split()
    nums = [int(n) for n in nums]

    result = average(nums)
    print(f"평균: {result:.1f}")
if __name__ == "__main__":
    main()