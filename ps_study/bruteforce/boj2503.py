

questions = int(input())

hint = [list(map(int, input().split())) for i in range(questions)]

answer = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
                if (a == b or b == c or c == a):
                     continue
                
                cnt = 0
                for each in hint:
                    number = each[0]
                    strike = each[1]
                    ball = each[2]
                    # abc와 number를 비교해서
                    # ball_count와 strike_count를 올려준다  

                    strike_count = 0
                    ball_count = 0
                

                    if a == int(str(number)[0]):
                        strike_count += 1
                    
                    if a == int(str(number)[1]) or a == int(str(number)[2]):
                        ball_count += 1
                    
                    if b == int(str(number)[1]):
                        strike_count += 1
                    
                    if b == int(str(number)[0]) or b == int(str(number)[2]):
                        ball_count += 1

                    if c == int(str(number)[2]):
                        strike_count += 1
                    
                    if c == int(str(number)[0]) or c == int(str(number)[1]):
                        ball_count += 1

                    if strike_count == strike and ball_count == ball:
                        cnt += 1
                    
                if cnt == questions:
                        answer += 1
print(answer)