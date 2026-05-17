def get_weather_data(file_name, index=9, converter=float):
    result_list = []
    with open(file_name, 'r') as file:
        rows = file.readlines()[1:]
        for row in rows:
            items = row.split(",")
            result_list.append(converter(items[index]))
    return result_list


def calculate_seasonal_sum(data_values, month_values, target_months=[6, 7, 8]):
    total_sum = 0
    for value, month in zip(data_values, month_values):
        if month in target_months:
            total_sum += value
    return total_sum


def main():
    csv_path = "week09/weather(146)_2022-2022.csv"
    rain_data = get_weather_data(csv_path)
    month_data = get_weather_data(csv_path, 1, int)
    total_rain = calculate_seasonal_sum(rain_data, month_data)
    print(f"2022년도의 여름철 강수량은 {total_rain:.1f}mm 입니다.")


if __name__ == "__main__":
    main()