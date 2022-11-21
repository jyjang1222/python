'''
    [문제]
        철수는 자판기에 물건을 채우려고 한다. 
        vending 리스트는 현재 자판기에 남아있는 물건 개수이다.
        box리스트는 자판기에 추가할 물건 개수이며, 5개씩 4줄 총 20개 여분이 있다.
        box의 앞에서부터 순차적으로 자판기에 물건을 채워 넣는다.
        자판기는 한 줄당 최대 10개까지 채울 수 있다.
        자판기가 전부 채워지거나 box가 전부 비워지면 종료되는 프로그램을 작성하시오.
    [예시]
        vending = [7, 5, 3, 5, 3]
        box     = [5, 5, 5, 5]

        vending = [10, 5, 3, 5, 3]
        box     = [2, 5, 5, 5]    

        vending = [10, 7, 3, 5, 3]
        box     = [0, 5, 5, 5]    

        vending = [10, 10, 3, 5, 3]
        box     = [0, 2, 5, 5]

        vending = [10, 10, 5, 5, 3]
        box     = [0, 0, 5, 5]

        vending = [10, 10, 10, 5, 3]
        box     = [0, 0, 0, 5]

        vending = [10, 10, 10, 10, 3]
        box     = [0, 0, 0, 0]
    [정답] 
        vending = [10, 10, 10, 10, 3]
        box     = [0, 0, 0, 0]
'''

vending = [7, 5, 3, 5, 3]
box = [5, 5, 5, 5]

print(vending)
print(box)

i = 0
while True:
    chk = True
    # 박스가 모두 0아니면 false
    for j in box:
        if j != 0:
            chk = False
    if chk:
        break

    # 재고채우기
    for j in range(len(box)):
        # 채우고 10이 넘으면 
        if vending[i] + box[j] >= 10:
            # 박스에 남은수량넣고 현재수량10넣기
            box[j] = vending[i] - box[j]
            vending[i] = 10
        # 10이 안넘으면
        else:
            # 현재수량에 박스만큼 넣고 박스0
            vending[i] += box[j]
            box[j] = 0
    print(vending)
    print(box)
    i += 1
