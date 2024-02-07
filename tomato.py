from collections import deque

m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
cnt = 0

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            queue.append([i,j,0])

da = [0,1,-1,0]
db = [-1,0,0,1]
def bfs() :
    global cnt
    while queue :
        a,b,c = queue.popleft()

        for i in range(4) :
            na = a + da[i]
            nb = b + db[i]
            if 0<=na<n and 0<=nb<m and graph[na][nb] == 1 :
                queue.append([na,nb,c+1])
                graph[na][nb] = 0
    cnt = c

bfs()
for i in range(n) :
    if 0 in graph[i] :
        cnt = -1

print(cnt)


