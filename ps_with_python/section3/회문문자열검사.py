TC = int(input())


for i in range(TC):
    word = input().lower()
    size = len(word)
    for j in range(size // 2):
        if word[j] != word[-1 - j]:
            print(f"#{i+1} NO")
            break

    else:
        print(f"#{i+1} YES")
