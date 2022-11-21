import random
'''
    [문제]
        [1] 1~50 사이의 랜덤 숫자 중 3의 배수 3개의 합을 total에 추가한다. 
        [2] 위 내용을 총 다섯 번 반복한다. 
        [3] 합이 가장 큰 수를 변수 max에 저장하시오.
    [예시]
        27 27 18 = 72
        30 24 15 = 69 
        6 12 45 = 63  
        45 27 48 = 120
        30 18 27 = 75 
        
        max = 120
'''

total = []
max = 0

for i in range(5):
    sum = 0
    cnt = 0
    while True:
        r = random.randint(1, 50)
        if r % 3 == 0:
            sum += r
            cnt += 1
        if cnt == 3:
            total.append(sum)
            break

print(total)

for i in total:
    if i > max:
        max = i

print(max)