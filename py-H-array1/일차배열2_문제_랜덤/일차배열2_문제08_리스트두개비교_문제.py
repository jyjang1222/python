import random
'''
    [문제]
        [조건1] 리스트 두 개에 1~100 사이의 랜덤 값 다섯 개를 저장한다.
        [조건2] 둘 다 짝수이거나 "짝수" 출력, 둘 다 홀수이면 "홀수" 출력 , 
                한쪽은 홀수이고 다른 한쪽은 짝수이면 "다르다"를 출력하시오.
    [예시]
'''

a = []
b = []

for i in range(5):
    num = random.randint(1, 100)
    a.append(num)
    num = random.randint(1, 100)
    b.append(num)

    if a[i] % 2 == 0 and b[i] % 2 == 0:
        print(a[i], b[i], "짝수")
    if a[i] % 2 == 1 and b[i] % 2 == 1:
        print(a[i], b[i], "홀수")


