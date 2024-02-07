from collections import deque

n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs() :
    ans_list2 = []
    for i in range(n) :
        for j in range(m) :
            queue = deque()
            visited = [[0] * m for _ in range(n)]
            if board[i][j] == 'L' :
                queue.append([i, j])
                visited[i][j] = 1

                while queue :
                    x,y = queue.popleft()
                    for i in range(4) :
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == 'L' :
                            queue.append([nx,ny])
                            visited[nx][ny] = visited[x][y] + 1

                ans_list = []
                for i in range(n) :
                    for j in range(m) :
                        ans_list.append(visited[i][j])
                a = max(ans_list)
                ans_list2.append(a)

    return ans_list2

k = max(bfs())-1

if k == -1 :
    print(0)
else :
    print(k)