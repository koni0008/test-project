n = int(input())
grape = [0]
for i in range(n) :
    grape.append(int(input()))

dp = [0]*(n+1)
if n >= 3 :
    dp[1] = grape[1]
    dp[2] = grape[1] + grape[2]
    dp[3] = max(dp[2], grape[2] + grape[3], grape[1] + grape[3])

    for j in range(4,n+1) :
        dp[j] = max(dp[j-2]+grape[j], dp[j-1], dp[j-3] + grape[j-1] + grape[j])

    print(dp[n])
elif n == 2 :
    print(grape[1]+grape[2])
else :
    print(grape[1])