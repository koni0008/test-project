from collections import deque

M,N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
sr,sc,sd = map(int, input().split())
lr,lc,ld = map(int, input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
lot = [(2,3),(2,3),(0,1),(0,1)]

def bfs(x,y,d) :
    queue = deque()
    queue.append([x-1,y-1,d-1])
    visited = [[[0]*4 for _ in range(N)] for _ in range(M)]
    visited[x-1][y-1][d-1] = 1

    while queue :
        ar,ac,ad = queue.popleft()
        if (ar,ac,ad) == (lr,lc,ld) :
            return visited

        for i in range(1,4) :
            nr = ar + dx[ad]*i
            nc = ac + dy[ad]*i
            nd = ad
            if 0<= nr < M and 0<= nc < N and board[nr][nc] == 0 and visited[nr][nc][nd] == 0 :
                queue.append([nr,nc,nd])
                visited[nr][nc][nd] += 1
            elif 0<= nr < M or 0<= nc < N or board[nr][nc] == 0 :
                break
            elif not visited[nr][nc][nd] == 0 :
                continue

        for i in lot[ad] :
            if not visited[ar][ac][i] == 0 :
                continue
            else :
                queue.append([ar,ac,i])
                visited[ar][ac][i] += 1

print(bfs(sr,sc,sd))



