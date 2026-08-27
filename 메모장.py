import os
while True:
    print("=== 메모장 프로그램 ===")
    print("1. 메모 작성")
    print("2. 메모 읽기")
    print("3. 메모 추가")
    print("4. 메모 삭제")
    print("5. 종료")
    choice = input("번호 입력 :   ")


    if choice == "1":
        title = input(" 제목  : ")
        contents = ""
        while True:
            print("내용을 입력하세요.")
            content = input("내용입력 : ")
            if content == "":
                print("중단합니다.")
                with open(f"{title}.txt", "w", encoding='utf-8') as file:
                    file.write(contents)
                break
            contents += content + "\n"
              



    elif choice == "2":
        print("== 메모 읽기 ==")
        title = input(" 읽을 메모 제목 : ")
        if os.path.exists(f"{title}.txt"):
            with open(f"{title}.txt", "r", encoding="utf-8") as file:
                content = file.read()
            print(content)
        else:
            print("없는 파일입니다.")

    elif choice == "3":
            print(" 메모 추가 기능입니다 ")

    elif choice == "4":
            print("\n===메모 삭제===")
            title = input("삭제할 메모 제목: ")
            if os.path.exists(f"{title}.txt"):
                 os.remove(f"{title}.txt")
                 print(f"메모{title}이(가) 삭제되었습니다.")
            else:
                print("해당 메모를 찾을수없습니다")
                 

    elif choice == "5":
            print(" 종료 ")
            break

    else:
          print(" 없는 기능입니다 ")
          continue

    

