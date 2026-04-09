height = float(input("당신의 신장을 입력하세요."))/100
weight = int(input("당신의 몸무게를 입력하세요."))

BMI = weight / (height * height)
print(f"당신의 BMI는 {BMI}입니다.")

if 23<= BMI <= 24.9 :
    print("당신은 비만 전단계 입니다.")
elif 25<=BMI <= 29.9 :
    print("당신은 1단계 비만입니다.")
elif 30<=BMI <= 34.9 :
    print("당신은 2단계 비만입니다.")
elif 35<=BMI :
    print("당신은 3단계 비만입니다.")
else:
    print("당신은 비만이 아닙니다.")