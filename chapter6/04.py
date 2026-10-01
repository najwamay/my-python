def starFormation3(n):
    mid = (n + 1) // 2

    for i in range(1, mid + 1):
        print("* " * i)

    for i in range(mid - 1, 0, -1):
        print("* " * i)

starFormation3(7)