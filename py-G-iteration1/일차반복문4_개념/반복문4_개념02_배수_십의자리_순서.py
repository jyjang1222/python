'''
[문제]
    100 이상인 9의 배수 중에서 
    10의 자리가 6인 두 번째 배수를 출력하시오. 
[정답]
    261
[설명]
    배수는 범위를 특별히 제한하지 않으면 계속해서 커지기 때문에,
    위 문제를 풀기 위해선 무한 반복문을 사용해야 한다.
'''

# 풀이
i = 100
count = 0

while i >= 100:
    if i % 9 == 0 and i % 100 // 10 == 6:
        count += 1
        if count == 2:
            print(i)
            break
    i += 1



# i = 100
# count = 0

# run = 1
# while run == 1:
#     if i % 9 == 0:
#         if i % 100 // 10 == 6:
#             count += 1
#         if count == 2:
#             print(i)
#             run = 0
#     i += 1