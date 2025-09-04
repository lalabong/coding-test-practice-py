# 1012

from collections import deque

def bfs(start_x, start_y, arr, visited, m, n):
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            ni, nj = x + di[i], y + dj[i]

            if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and arr[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())  # 가로길이, 세로길이, 배추개수
    arr = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    ans = 0
    visited = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0 and arr[i][j] == 1:
                bfs(i, j, arr, visited, m, n)
                ans += 1

    print(ans)
