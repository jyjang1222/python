'''
    [문제]
        a 리스트에서 백의자리가 2인 수만 출력하시오.
    [정답]
        1210
        1212
'''

a = [1210,1343,1524,1212,7452]

for i in a:
    if i % 1000 // 100 == 2:
        print(i)
