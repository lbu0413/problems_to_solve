from collections import deque


input_str = list(input())

N = int(input())


for i in range(N):
    classes = list(input())
    Q = deque(input_str)
    for x in classes:
        if x in Q:
            if x != Q.popleft():
                print(f"#{i+1} NO")
                break

    else:
        if len(Q) == 0:
            print(f"#{i+1} YES")
        else:
            print(f"#{i+1} NO")
