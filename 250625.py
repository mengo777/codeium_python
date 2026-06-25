# # 딕셔너리는 key를 사용해서 value를 출력한다.

# student = {
#     "name" : "철수",
#     "age"  : 18,
#     "city" : "서울"
# }

# print(student["name"])
# print(student["age"])
# print(student["city"])

# # 데이터 추가하기
# # 원하는 이름으로 딕셔너리를 만들고
# # 원하는 키로 값을 추가해보세요

# user = {}

# user["name"] = "민수"
# user["age"] = 17

# print(user)

# # 딕셔너리를 수정해보자

# user = {
#     "name" : "철수",
#     "age"  : 18,
#     "city" : "서울"
# }

# user["age"] = 19

# print(user)

# # 딕셔너리 요소를 수정해보자
# # 몬스터의 이름을 "골렘"
# # hp는 100으로 바꿔보자

# monster = {
#     "name": "슬라임",
#     "hp": 50
# }

# monster["hp"] = 30

# print(monster)

# 딕셔너리 요소를 삭제해보자

# user = {
#      "name" : "철수",
#      "age"  : 18,
#      "city" : "서울"
#  }

# del user ["city"]

# print(user)

# # 딕셔너리 요소를 검색해보자

# scores = {
#     "math" : 100,
#     "science" : 100,
#     "korean" : 100
# }

# target = input("점수를 검색할 과목 입력 : ")
# print(scores[target])

random_box = {
    "1" : "롤렉스",
    "2" : "윤후",
    "3" : "아무거나",
    "4" : "무한반복문 종료"
 }
while True:
 print("=== 운영의 보물상자 게임 ===")
 print("앞에 3개의 상자가 있습니다.몇 번 상자를 여시겠습니다?")
 choice = input("선택(1, 2, 3, 4) : ")
 if choice == "1":
    print("롤렉스")
 elif choice == "2":
    print("윤후")
 elif choice == "3":
    print("원하는거 아무거나")
 else:
    print("실패")
    break