# 상품 데이터 만들기
products = {
    "콜라": {
        "price": 1500,
        "stock": 10
    },
    "아침햇살": {
        "price": 1600,
        "stock": 12
    
    },
    "솔의 눈": {
        "price": 1400,
        "stock":15
    },
}

print("===== 자판기 =====")

for name, info in products.items():
    print(f"{name} : {info['price']}원")

# 소지금 정하기
wallet = 10000

# 현재 얼마나 가지고 있는지 출력하기 : f-string 활용하기
print(f"소지금 : {wallet}")

# 구입할 상품을 입력 받아서 choice에 저장하기
choice = input(f"구입할 상품 입력: ")
print(f"선택한 상품은 : {choice}")

# 입력받은 상품이 저장된 choice가
# 상품 데이터에 존재하는지 확인하기
# hint : in 연산자를 활용해보자
if choice not in products:
    print("없는 상품입니다.")
else:
    print("상품을 찾았습니다")