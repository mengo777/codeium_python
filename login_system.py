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
        # 아이디 중복 확인 
        if userid in users:
            print("이미 존재하는 아이디입니다.")
            continue
        # 아이디 길이 제한 확인
        if len(userid) < 8 or len(userid) > 15:
            print("아이디는 8자리 이상, 15자리 이하여야 합니다.")
            continue
        # 아이디에 소문자와 숫자만 포함되어있는지 확인
        has_lower = False
        is_vaild = True
        for ch in userid: 
            if ch.islower():
                has_lower = True
            elif ch.isdigit():
                pass
            else:
                is_vaild = False
                break
        if is_vaild and has_lower:
            print("사용가능한 아이디입니다.")
        else:
            print("영문 소문자(필수)와 숫자만 사용가능합니다.")
        # 위 조건 전부통과했다면 비밀번호 물어보기
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
        print("\n[로그인]")
        loginid = input("아이디를 입력하세요:")
        loginpw = input("비밀번호를 입력하세요")
        if loginid in users:
            if loginpw in users:
                print("로그인에 성공하셨습니다.")
            else:
                print("비밀번호나 아이디를 틀리셨습니다.")
        else:
            print("비밀번호나 아이디를 틀리셨습니다.")

    elif choice == 3:
        print("종료")
    else:
        print("잘못된 번호 입력")