import random
'''
	[문제]
		랜덤(3~6)숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시1]
		r = 6
	[출력1]
		1 2 3
		4 5 6
		7 8 9
	    10 11 12
        13 14 15
	    16 17 18
 	[예시2]
		r = 3
	[출력2]
		1 2 3
		4 5 6
		7 8 9	
'''

r = random.randint(3, 6)

# for i in range(1, r * 3 + 1):
# 	print(i, end = " ")
# 	if i % 3 == 0:
# 		print()
i = 1
j = 1
cnt = 0
while True:
	if i == r + 1:
		break
	print(j, end = " ")
	cnt += 1
	if cnt == 3:
		print()
		cnt = 0
		i += 1
	j += 1

print()

count = 1
for i in range(r):
	for j in range(3):
		print(count, end = " ")
		count += 1
	print()



# r = random.randint(3, 6)
# print(r)

# for i in range(r):
#     a = i * 3 + 1
#     print(a + 0, a + 1 , a + 2)

# print("----")
# for i in range(r):
#     a = i * 3 + 1
#     for j in range(3):
#         print(a + j, end=" ")
#     print()



