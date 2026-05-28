# # break
# # break는 for문과 while문 둘다 사용 가능하다.

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# # break 실습 - 숫자 맞추기

# import random

# answer = random.randint(1, 30)

# while True:
#     user_input = int(input("1qnxj 30 사이의 숫자를 입력하세요: "))

#     if user_input < answer:
#         print("더 큰 숫자입니다. 다시 시도하세요.")
#     elif user_input > answer:
#         print("더 작은 숫자압니다. 다시 시도하세요.")
#     else:
#         print("축하합니다! 정답입니다.")
#         break

# print("정답을 맞췄으니, 반복문에서 나와서 프로그램이 종료됩니다.")

# # continue 예제 - 짝수만 출력하기 
# for i in range(1,11):
#     if i % 2 != 0:
#         continue
#     print(i)

# 반복문 제어자 정리
# 1. break : 반복문 종료
# 2. continue : 이번 반복문만 건너뜀
# 3. pass : 아무일도 안함

password = "1234"

while True:

    user = input("비밀번호 입력: ")

    if user != password:
        print("틀렸습니다.")
        continue # 다시 while로 돌아감

    print("로그인 성공")
    break

print("로그인 완료. 환영합니다.")