import os
import urllib.request
import pandas as pd


def download_data(station):
    url = f"https://api.taegon.kr/stations/{station}/?sy=2019&ey=2019&format=csv"
    filename = f"weather_{station}_2019_2019.csv"
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    return df


def main():
    df_sw = download_data(119)
    df_jj = download_data(146)

    q4_diff_rain = abs(df_sw['rn'].sum() - df_jj['rn'].sum())
    print(f"4) 2019년 수원시와 전주시 총강수량 차이(절대값): {q4_diff_rain:.1f} mm")


if __name__ == '__main__':
    main()