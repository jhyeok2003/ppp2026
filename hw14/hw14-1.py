def load_date_data(file_path):
    date_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]  
        for line in lines:
            parts = line.strip().split(',')

            date_list.append([int(parts[0]), int(parts[1]), int(parts[2])])
    return date_list


def load_weather_column(file_path, col_index):
    column_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]
        for line in lines:
            parts = line.strip().split(',')
            column_data.append(float(parts[col_index]))
    return column_data


def find_max_diurnal_range(dates, max_temps, min_temps):
    highest_diff = -1.0
    target_date = None


    for date, t_max, t_max_min in zip(dates, max_temps, min_temps):
        current_diff = t_max - t_max_min

        if current_diff > highest_diff:
            highest_diff = current_diff
            target_date = date

    return target_date, highest_diff


def main():
    csv_file = "weather(146)_2001-2022.csv"

    dates = load_date_data(csv_file)
    tmax = load_weather_column(csv_file, 3)
    tmin = load_weather_column(csv_file, 5)

    best_date, max_diff = find_max_diurnal_range(dates, tmax, tmin)

    print(f"일교차가 가장 큰 날: {best_date}")
    print(f"일교차가 가장 큰 날의 일교차는 {max_diff:.1f}도 입니다.")


if __name__ == "__main__":
    main()