from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_num = 0

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def bfs() :
    cnt = 0
    queue = deque()
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and visited[i][j] == 0:
                queue.append([i,j])
                visited[i][j] = 1

                while queue :
                    x,y = queue.popleft()
                    for a in range(4) :
                        nx = x + dx[a]
                        ny = y + dy[a]
                        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0 and board[nx][ny] != 0 :
                            queue.append([nx,ny])
                            visited[nx][ny] = 1
                cnt += 1
    return cnt

for i in range(N) :
    for j in range(N) :
        max_num = max(max_num,board[i][j])

ans_list = []

for k in range(max_num) :
    for i in range(N) :
        for j in range(N) :
            if board[i][j] == k :
                board[i][j] = 0
    a = bfs()
    ans_list.append(a)

print(max(ans_list))