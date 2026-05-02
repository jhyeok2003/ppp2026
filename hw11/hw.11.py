import csv
filename = "weather(146)_2022-2022.csv"
temp_sum = 0
temp_count = 0

rain_days = 0
rain_total = 0

with open(filename, encoding="cp949") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        try:
            temp = float(row[3])
            rain = float(row[9])

            temp_sum += temp
            temp_count += 1

            if rain >= 5:
                rain_days += 1


            rain_total += rain

        except:
            continue

avg_temp = temp_sum / temp_count

print(f"연 평균 기온: {avg_temp:.1f}℃")
print(f"5mm 이상 강우일수: {rain_days}일")
print(f"총 강우량: {rain_total:.1f}mm")