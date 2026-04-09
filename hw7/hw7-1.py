cal= {"한라봉": 50, "딸기": 34, "바나나": 77}
total_cal = 0
for key, cal in cal.items():
    count = int(input(f"{key} 얼마나 먹었을까요? "))
    total_cal += cal * count
print("섭취한 총 칼로리:", total_cal)