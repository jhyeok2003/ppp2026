def load_weather_column(file_path, col_idx=9, parser=float):
    parsed_data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            items = line.split(",")
            parsed_data.append(parser(items[col_idx]))
    return parsed_data


def sum_yearly_precipitation(rain_data, year_data, Target_years):
    total_rain = 0
    for rain, year in zip(rain_data, year_data):
        if year in target_years:
            total_rain += rain
    return total_rain


def main():
    csv_file = "week10/weather(146)_2001-2022.csv"

    rainfall = load_weather_column(csv_file)
    years = load_weather_column(csv_file, 0, int)

    selected_years = [2020, 2021, 2022]
    total_value = sum_yearly_precipitation(rainfall, years, selected_years)

    print(f"지정된 연도의 총 강수량은 {total_value:.1f}mm 입니다.")


if __name__ == "__main__":
    main()