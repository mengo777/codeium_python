# # 문자열 string

# name = "홍길동"
# city = "서울"
# print(f"이름 : {name}, 도시 : {city}")

# # 문자열 실습

# weapon =  "sword"

# print(weapon[0])
# print(weapon[2])
# print(weapon[-1])
# # 각각 뭐가 출력될까?

# # 문자열 슬라이싱

# phone = '01012345678'
# print(phone[3:11])

# # split() : 분리하다, 쪼개다

# email = "asdf@gmail.com"

# box = email.split("@")[1]

# # gmail.com 나오도록 출력해보기]
# print(box)

# # 문자열 구하기 실습 2

# text = input("문자열을 입력하세요: ")
# print(f"입력한 문자열의 글자수 : {len(text)}글자")

# # 문자열 포함여부 확인

# email = "abc@naver.com"
# print(f"이메일 여부 : {'@' in email}")

email = (input("이메일 입력"))



print(f"{len(email)} 글자입니다")