import more_itertools as mit
n_times = 10
v = [0,1,2,4,5,7,8]

a = [list(x) for x in mit.consecutive_groups(v)]
print(a)

if a[0][0] == 0 and a[-1][-1] == n_times-2:
    a[-1] += a[0]
    a.pop(0)

print(a)