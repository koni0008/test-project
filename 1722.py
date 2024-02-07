from itertools import permutations

arr = []
N = int(input())
data = list(map(int, input().split()))

for i in range(1,N+1) :
    arr.append(i)

per_arr = []
find_per = []

for i in permutations(arr,N) :
    per_arr.append(i)

if data[0] == 1 :
    print(per_arr[data[1]-1])

if data[0] == 2 :
    for i in range(1,N+1) :
        find_per.append(data[i])
    print(per_arr.index(tuple(find_per))+1)
