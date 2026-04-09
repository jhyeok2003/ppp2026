import math
print("각도\t sin\t cos\t tan")
for i in range(0,91):
    rad=math.radians(i)

    sin=math.sin(rad)
    cos=math.cos(rad)

    if i==90:
        tan="정의되지 않습니다."
        print(f"{i}\t {sin:.3f}\t {cos:.3f}\t {tan}")
    else:
        tan=math.tan(rad)
        print(f"{i}\t {sin:.3f}\t {cos:.3f}\t {tan:.3f}")