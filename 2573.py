from collections import deque
from copy import deepcopy

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def one_year(graph) :
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] > 0 :
                cnt = 0
                queue = deque()
                queue.append([i,j])
                visited = [[0]*m for _ in range(n)]
                visited[i][j] = 1

                for k in range(4) :
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0 :
                        cnt += 1
                board[i][j] = board[i][j] - cnt

                if board[i][j] < 0:
                    board[i][j] = 0
    return board

def cnt_area(b) :
    queue = deque()
    visited = [[0]*m for _ in range(n)]
    area = 0
    for i in range(n) :
        for j in range(m) :
            if b[i][j] > 0 and visited[i][j] == 0:
                queue.append([i,j])
                visited[i][j] = 1

                while queue :
                    x,y = queue.popleft()
                    for k in range(4) :
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and b[nx][ny] > 0 and visited[nx][ny] == 0 :
                            queue.append([nx,ny])
                            visited[nx][ny] = 1
                area += 1

    return area

year = 1
while True :
    last_graph = deepcopy(board)
    next_graph = one_year(last_graph)
    board = next_graph
    if cnt_area(board) >= 2 :
        print(year)
        break
    elif year > 100 :
        print(0)
        break
    else:
        year += 1
# last_graph = deepcopy(board)
# print(one_year(last_graph))
print(f'#{test_case} {}')



