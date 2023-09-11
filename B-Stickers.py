start_str = input()
cnt_upd = int(input())
for _ in range(cnt_upd):
    inp = input().split()
    start, end = map(int, inp[:2])
    str_in = inp[2]
    start_str = start_str[:start - 1] + str_in + start_str[end:]

print(start_str)