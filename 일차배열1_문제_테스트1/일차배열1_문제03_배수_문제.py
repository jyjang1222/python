'''
    [문제]
        a 리스트에서 3의 배수만 출력하시오.
    [정답]
        24
        12
'''

a = [10,43,24,12,52]

for i in a:
    if i % 3 == 0:
        print(i)
