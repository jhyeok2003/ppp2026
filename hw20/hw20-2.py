import os
import urllib.request
import pandas as pd


def main():
    url = "https://api.taegon.kr/stations/146/?sy=2024&ey=2024&format=csv"
    filename = "weather_146_2024_2024.csv"
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    df.columns = df.columns.str.strip()

    q2_max_temp = df['tmax'].max()
    print(f"2) 2024년 전주시 최대기온: {q2_max_temp:.1f} °C")


if __name__ == '__main__':
    main()