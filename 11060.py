from collections import deque
N = int(input())
miro = list(map(int, input().split()))

def bfs(x) :
    queue = deque()
    queue.append(x)
    visited = [0 for _ in range(N)]
    visited[x] = 1

    while queue :
        a = queue.popleft()
        k = miro[a]
        for i in range(1,k+1) :
            na = a + i
            if a == N:
                return visited
            elif visited[na] == 0 :
                queue.append(na)
                visited[na] = visited[a] + 1
            else:
                continue

print(bfs(0))