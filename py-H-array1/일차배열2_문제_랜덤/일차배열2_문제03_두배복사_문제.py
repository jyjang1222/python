import random
'''
    [문제]
        랜덤 숫자(1~10) 다섯 개를 arr에 추가하고
        그 두 배를 total에 저장 후 출력하시오.
    [예시]
        arr   = [10, 3, 4, 2, 6]
        total = [20, 6, 8, 4, 12]
'''

arr = []
total = []

for i in range(5):
    num = random.randint(1, 10)
    arr.append(num)

print(arr)

for i in arr:
    total.append(i * 2)

print(total)