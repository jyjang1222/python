'''
	[문제]
		철수네 학교의 수학 시험은 4점짜리 문제와 5점짜리 문제가 섞여서 출제된다.	
		철수는 20개의 문제를 맞혀서 90점을 받았다. 	
		각각 몇 문제씩 맞혔는지 구하시오. 
		주석으로 표현하시오.
	[정답]
		4점 문제 = 10
		5점 문제 = 10
'''

_4점 = 20
_5점 = 0

while True:
	_4점 -= 1
	_5점 += 1
	if _4점 * 4 + _5점 * 5 == 90:
		print(_4점, _5점)
		break
