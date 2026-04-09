import math

r = float(input("반지름을 입력하세요"))
pi = math.pi
S = pi*r**2
l = 2*pi*r
print(f"원의 면적은 {S:.2f}입니다.")
print(f"원의 둘레는 {l:.1f}입니다.")