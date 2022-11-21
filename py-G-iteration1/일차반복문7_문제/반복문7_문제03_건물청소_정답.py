'''
	[문제]
		철수는 50층 빌딩의 소유주이다.
		청소를 위해 청소직원 3명을 고용했다. 
		청소는 한 사람당 두 개 층씩 청소하기로 했다. 
		예를 들어 직원 1이 [1층 2층] 청소하면, 직원 2는 [3층 4층] , 직원 3은 [5층 6층]을 청소한다.
		다시 직원 1은 [7층 8층], 직원 2는 [9층 10층], 직원 3은 [11층 12층]을 청소한다. 
		이런 식으로 50층을 전부 청소한다. 
		전부 청소했을때, 직원 2의 청소한 층을 전부 출력하시오.
	[정답]
		3 4 9 10 15 16 21 22 27 28 33 34 39 40 45 46 
'''

전체층 = 50

i = 1
while i <= 전체층:
	unit = i % 6

	if unit == 3 or unit == 4:
		print(i, end=" ")
		
	i += 1
