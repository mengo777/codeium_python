# # in 연산자

# students = ["김철수", "이영희", "박민수"]
# print("박민수" in students) # "박민수" 라는 값이 students라는 리스트에 있나요?
# # 실험해보기
# print("홍길동" in students) # "홍길동" 라는 값이 students라는 리스트에 있나요?
# # 실행해보기

# foods = ["치킨", "피자", "햄버거"]

# food = input("찾을 음식을 입력하세요 : ")

# if food in foods:
#     print("목록에 있습니다.")
# else:
#     print("목록에 없습니다.")

# numbers = [1, 3, 5, 7, 3]

# count = 0

# for  n in numbers:
#     if n == 3:
#         count += 1

# print(count)

students = [
    "김철수",
    "이영희",
    "박민수",
    "최지우",
    "홍길동"
]

name = input("학생 이름 입력 :  ")

found = False

for student in students:
    if student == name:
        found = True
        break

if found:
    print("학생을 찾았습니다.")
else:
    print("학생이 없습니다.")