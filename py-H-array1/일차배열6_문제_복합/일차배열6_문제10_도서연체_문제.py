'''
	[문제]
		철수는 도서관에서 책을 한 권 빌렸다. 
		빌린 날짜는 2021년 10월 10일이고, 대여 일수는 20일이다. 
		도서가 연체되면 연체 비용은 하루에 100원이다.
		오늘은 2022년 2월 25일 이라고 할 때, 지급해야 하는 비용은 얼마인지 구하시오.
		또한 2021년 1월1일이 월요일이라고하면, 오늘은 무슨 요일인지 구하시오.
		단, 윤년은 계산하지 않는다.
	[정답]
		11800
'''
monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
연체료 = 100

작년빌린달 = 10
작년빌린일 = 10
총작년일수 = 0

# 일수를 뺀 달만 총작년일수에 더함 (작년)
for i in range(작년빌린달, len(monthList)):
	총작년일수 += monthList[i]
# 달을뺀 일수만큼 총작년일수에 더함 (작년)
총작년일수 += (monthList[작년빌린달 - 1] - 작년빌린일)

올해빌린달 = 2
올해빌린일 = 25
총올해일수 = 0

# 일수를 뺀 달만 총올해일수에 더함 (올해)
for i in range(올해빌린달 - 1):
	총올해일수 += monthList[i]
# 달을뺀 일수만큼 총올해일수에 더함 (올해)
총올해일수 += 올해빌린일

# 작년빌린일수와 올해빌린일수 더함
총빌린일수 = 총작년일수 + 총올해일수

비용 = (총빌린일수 - 20) * 연체료
print(총빌린일수, 비용)

## 요일구하기
# 1일이 월요일이니 idx = 0은 일요일이다
요일 = ["일", "월", "화", "수", "목", "금", "토"]
print(요일[총빌린일수 % 7])