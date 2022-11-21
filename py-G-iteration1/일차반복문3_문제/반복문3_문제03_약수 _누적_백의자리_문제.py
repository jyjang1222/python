'''
    [문제]
        2000의 약수 중에서 순서대로 약수를 출력했을 때, 
        [조건1] 백의자리가 4인 약수들만 출력하고, 
        [조건2] 그 전체 합을 출력하시오. 
        [조건3] 위 약수들의 개수를 출력하시오.
    [정답]
        400 
        total = 400
        count = 1
'''

# 풀이
num = 2000
i = 1
sum = 0
count = 0

while i <= num:
	if num % i == 0 and i % 1000 // 100 == 4:
		sum += i
		count += 1
	i += 1

print(sum, count)