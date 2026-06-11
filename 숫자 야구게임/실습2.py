answer = [1,3,5]

guess = [1,7,3]

ball = 0

for u in range(3):
    if guess[u] in answer and guess[u] != answer[u]:
        ball += 1

# ball 개수 출력하기
print(ball)