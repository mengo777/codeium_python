# student = {}

# student['name'] = 'ghkddudtj' # 본인이름
# student['age'] = 14 # 본인나이

# print(student)

menu = {
    '콘찹' : {
        'price' : 1500,
        'stock' : 10
    },
    '새우깡' : {
        'price'  : 1500,
        'stock' : 10
    },
    '칸쵸' : {
        'price' : 1500,
        'stock' : 10
    },
}

# 딕셔너리.items()는 key와 value를 전부 반환합니다.
print("===== 자판기 =====")
for name, info in menu.items():
    print(f'{name} : {info['price']}원')

print("\n종료를 원하면 '종료'를 입력하세요.")

# 소지금
wallet = 10000
print(f"소지금 : {wallet}원")

# 구매할 상품 입력받기
choice = input("구매할 상품을 입력 : ")

if choice == '종료':
    print("구매를 중단합니다.")
    # break

# in 연산자
if choice not in menu:
    print("없는 상풍입니다.")
else:
    print("구매 진행")

# 소지금이 부족할떄 구매중단.
price = menu[choice]['price']
if wallet < price:
    print("소지금이 부족합니다")
    # break