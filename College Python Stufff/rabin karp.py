def rabin_karp(T, P, n, m, d, q):
    h = (d ** (m - 1)) % q
    p = 0
    to = 0
    for i in range(m):
        p = (d * p + ord(P[i])) % q
        to = (d * to + ord(T[i])) % q
    for s in range(n - m + 1):
        if p == to:
            if P[0:m] == T[s:s + m]:
                print(f"Pattern occurs with shift:{s}")
        if s < n - m:
            to = (d * (to - ord(T[s]) * h) + ord(T[s + m])) % q


T = "bananabanana"
P = "banana"
n = len(T)
m = len(P)
d = 256
q = 101
rabin_karp(T, P, n, m, d, q)
