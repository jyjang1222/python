'''
	[문제]
		a리스트는 학생 번호와 점수 한 세트를 이루고 있다.		
		0 ~ 7 사이의 랜덤 숫자를 저장하고,
		해당 위치의 학생 번호와 그 점수를 삭제하시오.
	[예시]
		
'''
import random

a = [1001, 40, 1002, 60, 1003, 65, 1004, 70]

index = random.randint(0, len(a) - 1)
print("index =", index)

if index % 2 == 0:
	a.remove(a[index])
	a.remove(a[index])
else:
	a.remove(a[index])
	a.remove(a[index - 1])


print(a)