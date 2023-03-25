from collections import deque

M,N = int(input('M: ')), int(input('N: '))

visited = set()
count = 0

array = []
row = []
print('Matrix: ')
for i in range(M):
    for j in range(N):
        row.append(int(input('Row {}, Column {}: '.format(i, j))))
    array.append(row)
    row = []


def bfs(r, c):
    q = deque()
    visited.add((r, c))
    q.append((r, c))

    while q:
        row, col = q.popleft()

        r1, c1 = row + 1, col
        r2, c2 = row + -1, col
        r3, c3 = row, col + 1
        r4, c4 = row, col + -1

        rows = [r1, r2, r3, r4]
        columns = [c1, c2, c3, c4]

        for i in range(4):
            if rows[i] in range(M) and\
                    columns[i] in range(N) and\
                    array[rows[i]][columns[i]] == 1 and\
                    (rows[i], columns[i]) not in visited:

                q.append((rows[i], columns[i]))
                visited.add((rows[i], columns[i]))

for i in range(M):
    for j in range(N):
        if array[i][j] == 1 and (i, j) not in visited:
            bfs(i,j)
            count += 1

print('islands: ', count)


