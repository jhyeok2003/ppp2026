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

    df_birthday = df[(df['month'] == 3) & (df['day'] == 5)]

    plt.figure(figsize=(10, 5))
    plt.plot(df_birthday['year'], df_birthday['ta'], color='green', marker='o')
    plt.title("Jeonju Temperature on March 5th (1980-2024)")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°C)")
    plt.grid(True)
    plt.show()

    df_subset = df_birthday[(df_birthday['year'] >= 1980) & (df_birthday['year'] <= 2014)].copy()
    df_subset['rank'] = df_subset['ta'].rank(ascending=False, method='min')

    rank_2003 = int(df_subset[df_subset['year'] == 2003]['rank'].values[0])
    highest_year = int(df_subset.loc[df_subset['ta'].idxmax(), 'year'])
    lowest_year = int(df_subset.loc[df_subset['ta'].idxmin(), 'year'])

    print(f"7) 3월 5일 기준 분석 (1980년~2014년 범위):")
    print(f"   - 준혁이 태어난 해(2003년)는 {rank_2003}번째로 온도가 높았습니다.")
    print(f"   - 가장 온도가 높았던 해: {highest_year}년")
    print(f"   - 가장 온도가 낮았던 해: {lowest_year}년")


if __name__ == '__main__':
    main()