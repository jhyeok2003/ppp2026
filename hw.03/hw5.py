print("변환 종류를 선택하시오.(1. 화씨->섭씨 2. 섭씨->화씨 3. 피트(ft)-> cm 4. cm->피트(ft)")

x=int(input("번호를 선택하시오:"))
if x in [1,2,3,4]:
    y=float(input("변환할 값을 입력하시오:"))
    if x==1:
          z=(y-32)*5/9
          print(f"섭씨온도:{z:.1f}℃")
    elif x==2:
          z=y*9/5+32
          print(f"화씨온도:{z:.1f}℉")
    elif x==3:
          z=y*30.48
          print(f"길이:{z:.1f}cm")
    elif x==4:
          z=y/30.48
          print(f"길이:{z:.1f}ft")
else:
        print("1,2,3,4 중에서 선택해주세요.")