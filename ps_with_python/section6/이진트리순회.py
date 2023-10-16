def preDFS(v):
    if v > 7:
        return
    else:
        print(v)
        preDFS(v * 2)
        preDFS(v * 2 + 1)


preDFS(1)


def inDFS(v):
    if v > 7:
        return
    else:
        inDFS(v * 2)
        print(v)
        inDFS(v * 2 + 1)


inDFS(1)


def postDFS(v):
    if v > 7:
        return
    else:
        postDFS(v * 2)
        postDFS(v * 2 + 1)
        print(v)


postDFS(1)
