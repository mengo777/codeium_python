import os

# now_floder = os.getcwd()
# print()
# print(f"[ 현재 풀더 위치] {now_floder}")

# os.mkdir("new_floder")

# files = os.listdir('./')
# print(files)

# os.rmdir("test")

# if os.path.exists("new_folder"):
#     os.rmdir("new_folder")

with open("hello.txt", "w") as file:
    file.write("Hi!")