def spiral(n):
    a = [[0] * n for _ in range(n)]
    k, l = 0, 0
    m, p = n, n
    cnt = 1

    while (k < m and l < p):
        for i in range(l, p):
            a[k][i] = cnt
            cnt += 1
        k += 1

        for i in range(k, m):
            a[i][p - 1] = cnt
            cnt += 1
        p -= 1

        if (k < m):
            for i in range(p - 1, l - 1, -1):
                a[m - 1][i] = cnt
                cnt += 1
            m -= 1

        if (l < p):
            for i in range(m - 1, k - 1, -1):
                a[i][l] = cnt
                cnt += 1
            l += 1

    for i in range(n):
        for j in range(n):
            print(a[i][j], end='\t')
        print()

# Example usage:
spiral(5)
