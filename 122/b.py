S = list(input())
ACGT_filter = ['A', 'C', 'G', 'T']

str_length = 0
str_lengths = []
for s in S:
    if s in ACGT_filter:
        str_length += 1
    else:
        str_lengths.append(str_length)
        str_length = 0

print(max(str_lengths))