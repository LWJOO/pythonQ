def electricPay(kwh):
    if kwh <= 100:
        pay = kwh * 60.7 +410
    elif kwh <= 200:
        pay = 100 * 60.7 + (kwh - 100) *125.9 + 910
    else:
        pay = 100 * 60.7 + 100 * 125.9 + (kwh - 200) * 187.9 + 1600

    pay = int(pay * 1.137)
    return pay

kwh = int(input('전력 사용량을 입력해주세요 : '))
print(f'이번달 전기요금은 {electricPay(kwh)}원 입니다.')
