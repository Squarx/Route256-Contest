for _ in range(int(input())):
    matrixes = list(list(str()))
    cnt, n, m,  = map(int, input().split())
    for i in range(cnt):
        tmp = list()
        for j in range(n):
            tmp.append(input())
        if i != cnt -1 :
            input()
        matrixes.append(tmp)

    matrixes_res = matrixes[-1]

    for i in matrixes[-2::-1]:
        for j in range(n):
            for x in range(m):
                if i[j][x] != '.':
                    matrixes_res[j] = matrixes_res[j][:x] + i[j][x] + matrixes_res[j][x+1:]


    for s in matrixes_res:
        print(s)
    print()