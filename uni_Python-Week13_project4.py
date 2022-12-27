num1 = 0
num2 = 0
while ValueError:
    try:
        num1 = int(input("나누어질 수: "))
        num2 = int(input("나눌 수: "))
    except ValueError:
        print("문자열은 입력하실 수 없습니다.")
        continue
    else:
        break;

answer = 0
try:
    answer = num1 / num2
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print("에러가 없었습니다.")
finally:
    print("모든 업무가 끝났습니다.")
