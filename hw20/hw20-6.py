import os
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt


def main():
    url = "https://api.taegon.kr/stations/146/?sy=1980&ey=2024&format=csv"
    filename = "weather_146_1980_2024.csv"
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    df.columns = df.columns.str.strip()

    jj_yearly_rain = df.groupby('year')['rn'].sum()

    plt.figure(figsize=(12, 5))
    plt.bar(jj_yearly_rain.index, jj_yearly_rain.values, color='skyblue', edgecolor='black')
    plt.title("Jeonju Annual Precipitation (1980-2024)")
    plt.xlabel("Year")
    plt.ylabel("Precipitation (mm)")
    plt.grid(axis='y')
    plt.show()


if __name__ == '__main__':
    main()