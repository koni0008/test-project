from collections import deque
n,m = map(int, input().split())
board = [list(input()) for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs() :
    queue = deque()
    visited = [[0]*n for _ in range(m)]
    W_list = []
    B_list = []

    for i in range(m) :
        for j in range(n) :
            cnt = 1
            if visited[i][j] == 0 :
                queue.append([i,j])
                visited[i][j] = 1
                team = str(board[i][j])
            else :
                team = 'F'

            while queue :
                x,y = queue.popleft()
                for k in range(4) :
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<= nx < m and 0<= ny < n and board[nx][ny] == board[x][y] and visited[nx][ny] == 0 :
                        queue.append([nx,ny])
                        visited[nx][ny] = 1
                        cnt += 1
            if team == 'W' :
                W_list.append(cnt)
            elif team == 'B':
                B_list.append(cnt)
            else:
                continue
    return W_list,B_list


a,b = bfs()
c = 0
d = 0
for q in a :
    c += q*q
for w in b :
    d += w*w
print(c,d)