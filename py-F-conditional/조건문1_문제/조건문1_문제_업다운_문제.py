import random

'''
    [문제]
        1부터 100 사이의 숫자 두 개를 랜덤으로 저장한다.
        두 숫자 중 더 큰 숫자를 출력하시오.
        단, 서로 같으면 "같다"를 출력하시오.
'''

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

res = "같다"

if num1 > num2:
    print(num1)
if num1 < num2:
    print(num2)

print(res)