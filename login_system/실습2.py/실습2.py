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
        if len(userid) < 8 or len(userid) > 15:
            print("아이디는 8자리 이상, 15자리 이하여야 합니다.")
            continue
        for ch in userid:
            if not ch.islower() or not ch.isdigit():
                print("오류 : 아이디는 영어소문자와 숫지로만 이뤄져야 합니다.")
                continue
        userpw = input("비밀번호 입력 : ")
        if len(userpw) < 6:
            print("비밀번호 6자리 이상이어야 합니다")
            continue
        for pw in userpw:
            if not pw.isdigit():
                print("비밀번호는 숫자로만 이루져야합니다")
                continue
        users[userid] = userpw
        print(users)

    elif choice == "2":
        print("로그인")
    elif choice == 3:
        print("종료")
    else:
        print("잘못된 번호 입력")