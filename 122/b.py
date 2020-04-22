ACGT_filter = ['A', 'C', 'G', 'T']

ans = 0
now = 0
for s in input():
    if s in ACGT_filter:
        now += 1
    else:
        now = 0
    ans = max(now, ans)

print(ans)