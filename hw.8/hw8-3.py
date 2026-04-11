def c2f(temp_c):
    return temp_c * 9 / 5 + 32
def main():
    t = float(input("섭씨 온도를 입력하세요: "))
    result = c2f(t)
    print(f"화씨 온도: {result:.1f}℉")
main()