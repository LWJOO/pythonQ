def waterPay(com, leter):
    pay = 0
    if com == 'A' or com == 'a':
        pay = leter * 100
    elif com == 'B' or com == 'b':
        if leter <= 50:
            pay = leter * 150
        else:
            pay = 50 * 150 + (leter-50) * 75
    else:
        print('잘못된 회사명입니다.')
    return(pay)

com = input('수도 회사가 어디인가요? : ')
leter = int(input('사용하신 물의 양을 알려주세요 : '))
print(f'{com} 회사에 지불해야할 금액은 {waterPay(com, leter)}원 입니다.')
