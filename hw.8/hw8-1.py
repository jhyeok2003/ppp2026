def calc_calories():
    calories = {"한라봉": 50, "딸기": 34, "바나나": 77}
    total = 0

    for fruit in calories:
        count = int(input(f"{fruit} 섭취한 과일의 양은? "))
        total += calories[fruit] * count

    print(f"총 칼로리: {total} kcal입니다.")
