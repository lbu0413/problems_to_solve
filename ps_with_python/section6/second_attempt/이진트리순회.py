def preDFS(v):
    if v > 7:
        return
    else:
        print(v, end=" ")
        preDFS(v * 2)
        preDFS(v * 2 + 1)


print(preDFS(1))


def inDFS(v):
    if v > 7:
        return
    else:
        inDFS(v * 2)
        print(v, end=" ")
        inDFS(v * 2 + 1)


print(inDFS(1))


def postDFS(v):
    if v > 7:
        return
    else:
        postDFS(v * 2)
        postDFS(v * 2 + 1)
        print(v, end=" ")


print(postDFS(1))
