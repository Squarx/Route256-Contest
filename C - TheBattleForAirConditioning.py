for _ in range(int(input())):
    t = [i for i in range(15, 31)]
    cnt_workers = int(input())
    for i in range(cnt_workers):
        l = input().split()
        if l[0] == ">=":
            t = [i for i in t if i >= int(l[1])]
            if len(t):
                print(t[-1])
            else:
                print(-1)
        else:
            t = [i for i in t if i <= int(l[1])]
            if len(t):
                print(t[0])
            else:
                print(-1)
    print()