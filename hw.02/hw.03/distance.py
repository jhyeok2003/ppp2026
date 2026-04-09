
import math

x1=int(input("x1을 입력하시오 "))
x2=int(input("x2를 입력하시오 "))
y1=int(input("y1을 입력하시오 "))
y2=int(input("y2를 입력하시오 "))
print(f"{x1},{y1},{x2},{y2}")
l=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(l)

