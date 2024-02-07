import sys

input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]
result = []


# 색종이 최대 길이 구하는 함수
def find_length(y, x):
    length = 1
    for l in range(2, min(10 - y, 10 - x, 5) + 1):
        for i in range(y, y + l):
            for j in range(x, x + l):
                if board[i][j] == 0:
                    return length
        length += 1
    return length


# 색종이 덮는 함수
def cover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            board[i][j] = 0


# 색종이 치우는 함수
def uncover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            board[i][j] = 1


def dfs():
    sum =0
    for i in range(0, 10):
        for j in range(0, 10):
            if board[i][j] == 1:
                length = find_length(i, j)
                if papers[length] > 0 :
                    cover(i, j, length)
                    papers[length] -= 1
                    sum += 1
                elif papers[length] == 0 :
                    return -1
                    break
    return sum

print(dfs())
#
# result.add(dfs(0))
# if -1 in result:
#     result.remove(-1)
# print(min(result) if result else -1)