# 116044 KB, 276 ms

from collections import deque

# dfs로 하니까 메모리 초과나서 bfs로 바꿔줌
def bfs(i, j, h):
    q = deque()
    visited[i][j] = 1
    q.append((i, j))

    while q:
        a = q.popleft()
        for n in range(4):
            ni = a[0] + di[n]
            nj = a[1] + dj[n]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and ground[ni][nj] > h:
                q.append((ni, nj))
                visited[ni][nj] = 1


N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]
max_safe_area = 0
max_high = max(map(max, ground))
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

# 강수량 0 일때부터 최고 높이일때까지 비교해보면서 구역의 수 세줌
for high in range(0, max_high + 1):
    visited = [[0] * N for _ in range(N)]
    safe_area = 0
    for r in range(N):
        for c in range(N):
            if ground[r][c] > high and not visited[r][c]:
                bfs(r, c, high)
                safe_area += 1
    # 구역 최댓값인지 확인해줌
    if safe_area > max_safe_area:
        max_safe_area = safe_area

print(max_safe_area)


#------------------------------------메모리초과로 실패 -> 집가서 수정해보려고 여기 일단 저장~------------------------------------

import sys
sys.setrecursionlimit(100000)

def dfs(i, j, h):
    visited[i][j] = 1

    for n in range(4):
        ni = i + di[n]
        nj = j + dj[n]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and ground[ni][nj] > h:
            dfs(ni, nj, h)


N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]
max_safe_area = 0
max_high = max(map(max, ground))
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


for high in range(1, max_high + 1):
    visited = [[0] * N for _ in range(N)]
    safe_area = 0
    for r in range(N):
        for c in range(N):
            if ground[r][c] > high and not visited[r][c]:
                dfs(r, c, high)
                safe_area += 1
    if safe_area > max_safe_area:
        max_safe_area = safe_area

print(max_safe_area)

