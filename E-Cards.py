m, n = map(int, input().split())
big_set = set(range(1, n + 1))
items = list(map(int, input().split()[:m]))
friends = {i + 1: set(range(1, items[i] + 1)) for i in range(m)}

for k, v in friends.items():
    tmp = big_set.difference(v)
    if len(tmp) == 0:
        print(-1)
        exit(0)
    value = next(iter(tmp))
    friends[k] = value
    big_set.remove(value)

print(' '.join(str(i) for i in friends.values()))