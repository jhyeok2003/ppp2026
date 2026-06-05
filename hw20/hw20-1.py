import os
import urllib.request
import pandas as pd


def main():
    url = "https://api.taegon.kr/stations/146/?sy=2012&ey=2012&format=csv"
    filename = "weather_146_2012_2012.csv"
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    df.columns = df.columns.str.strip()

    q1_rain = df['rn'].sum()
    print(f"1) 2012년 전주시 연 강수량: {q1_rain:.1f} mm")


if __name__ == '__main__':
    main()