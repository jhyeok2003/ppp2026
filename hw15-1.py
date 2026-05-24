import os
import urllib.request
import pandas as pd

def main():
    url = "https://api.taegon.kr/stations/146/?sy=2023&ey=2023&format=csv"
    csv_filename = "jeonju_2023.csv"
    output_filename = "result.txt"

    if not os.path.exists(csv_filename):
        urllib.request.urlretrieve(url, csv_filename)

    df = pd.read_csv(csv_filename, skipinitialspace=True)
    df.columns = df.columns.str.strip()

    avg_temp = df['ta'].mean()
    rain_days_over_5mm = df[df['rn'] >= 5].shape[0]
    total_rain = df['rn'].sum()

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(f"1)연 평균 기온: {avg_temp:.2f}\n")
        f.write(f"2)5mm이상 강우일수: {rain_days_over_5mm}\n")
        f.write(f"3)총 강우량: {total_rain:.1f}\n")

if __name__ == '__main__':
    main()