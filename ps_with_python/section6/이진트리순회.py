def preDFS(v):
    if v > 7:
        return
    else:
        print(v, end=" ")
        preDFS(v * 2)
        preDFS(v * 2 + 1)


preDFS(1)
print()


def inDFS(v):
    if v > 7:
        return
    else:
        inDFS(v * 2)
        print(v, end=" ")
        inDFS(v * 2 + 1)


inDFS(1)
print()


def postDFS(v):
    if v > 7:
        return
    else:
        postDFS(v * 2)
        postDFS(v * 2 + 1)
        print(v, end=" ")


postDFS(1)
print()
