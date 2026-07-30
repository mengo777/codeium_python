users = {} # 회원정보 

print("============")
print("1. 회원가입")
print("2. 로그인")
print("3. 종료")
print("============")
while True:
    choice = input("번호를 입력해주세요")

    if choice == "1":
        print("회원가입")
        userid = input("아이디 입력 : ")
        if userid in users:
            print("이미 존재하는 아이디입니다.")
            continue
        userpw = input("비밀번호 입력 : ")
        users[userid] = userpw
        print(users)

    elif choice == "2":
        print("로그인")
    elif choice == 3:
        print("종료")
    else:
        print("잘못된 번호 입력")