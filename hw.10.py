def main():
    data = input()
    numbers = data.split()

    nums = []
    for x in numbers:
        nums.append(int(x))

    count = len(nums)

    total = 0
    for n in nums:
        total += n
    avg = total / count

    max_val = nums[0]
    min_val = nums[0]

    for n in nums:
        if n > max_val:
            max_val = n
        if n < min_val:
            min_val = n

    nums.sort()

    if count % 2 == 1:
        median = nums[count // 2]
    else:
        median = (nums[count // 2 - 1] + nums[count // 2]) / 2

    print(count)
    print(avg)
    print(max_val)
    print(min_val)
    print(median)


if __name__ == "__main__":
    main()