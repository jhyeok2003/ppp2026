import os
import urllib.request
import pandas as pd


def main():
    url = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    filename = "weather_146_2020_2020.csv"
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    df.columns = df.columns.str.strip()

    df['diurnal_range'] = df['tmax'] - df['tmin']
    q3_max_range = df['diurnal_range'].max()
    print(f"3) 2020년 전주시 최대 일교차: {q3_max_range:.1f} °C")


if __name__ == '__main__':
    main()