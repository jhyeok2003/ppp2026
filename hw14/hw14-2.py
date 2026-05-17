def load_date_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]  # 헤더 제외하고 바로 가져오기


    return [[int(token) for token in line.strip().split(',')[:3]] for line in lines]


def load_weather_column(file_path, col_index):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]

    return [float(line.split(',')[col_index]) for line in lines]


def calculate_gdd(date_list, avg_temps):
    total_gdd = 0.0

    for date, temp in zip(date_list, avg_temps):
        month = date[1]
        if month in [5, 6, 7, 8, 9] and temp > 5:
            total_gdd += (temp - 5)
    return total_gdd


def main():
    csv_file = "weather(146)_2001-2022.csv"

    dates = load_date_list(csv_file)
    tavg = load_weather_column(csv_file, 4)

    result_gdd = calculate_gdd(dates, tavg)
    print(f"5월부터 9월까지의 적산온도는 {result_gdd:.1f}도 입니다.")


if __name__ == "__main__":
    main()