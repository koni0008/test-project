from collections import deque

m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
queue = deque([])
cnt = 0
total = []
ans = 0

for i in range(m) :
    for j in range(n) :
        if graph[i][j] == 0 :
            queue.append([i,j,0])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs() :
    global cnt
    global ans
    while queue :
        x,y,z= queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                queue.append([nx, ny, z + 1])
                ans += 1
        total.append(ans)

    cnt = z

bfs()

print(cnt)
print(total[-2])
