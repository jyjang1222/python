'''
	[문제] 아래 조건을 만족하는 식을 작성하시오.  
 		[조건1] 10~1까지 거꾸로 반복문을 실행해 숫자를 출력한다.
 		[조건2] 6~3 사이는 숫자 대신 "a"만 출력한다.
	[정답]
		10
		9
		8
		7
		a
		a
		a
		a
		2
		1
'''

num = 10
i = 1

while i <= 10:
	if 3 <= num and num <= 6:
		print("a")
		num -= 1
		i += 1
		continue
	print(num)
	num -= 1
	i += 1