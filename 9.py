cnt = 0
for s in open('9.txt'):
    cnt += 1
    st = [int(x) for x in s.split()]
    if len(st) != len(set(st)): continue
    mx = max(st); mn = min(st)
    st.remove(mx); st.remove(mn)
    if 2 * (mx + mn) == 3*(sum(st)):
        print(cnt)
