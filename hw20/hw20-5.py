import os
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt


def download_data(station):
    url = f"https://api.taegon.kr/stations/{station}/?sy=1980&ey=2024&format=csv"
    filename = f"weather_{station}_1980_2024.csv"
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    return df


def main():
    df_jj = download_data(146)
    df_sw = download_data(119)

    jj_yearly_avg = df_jj.groupby('year')['ta'].mean()
    sw_yearly_avg = df_sw.groupby('year')['ta'].mean()

    plt.figure(figsize=(10, 5))
    plt.plot(jj_yearly_avg.index, jj_yearly_avg.values, label='Jeonju', color='red', marker='o')
    plt.plot(sw_yearly_avg.index, sw_yearly_avg.values, label='Suwon', color='blue', marker='s')
    plt.title("Average Temperature (1980-2024)")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()