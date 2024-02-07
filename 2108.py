import sys
input = sys.stdin.readline

N = int(input())
list = []
for i in range(N) :
    data = int(input())
    list.append(data)

list.sort()
def fun_1() :
    sum = 0
    for i in list :
        sum += i
    return round(sum/N)

def fun_2() :
    a = list[(N//2)]
    return a

def fun_3() :
    count_list = []
    max_cnt = 0
    max_num = []

    if len(list) == 1 :
        return list[0]

    for i in list :
        a = list.count(i)
        if a >= max_cnt :
            max_cnt = a
    for i in list :
        if list.count(i) == max_cnt :
            max_num.append(i)
    if a == 1 :
        return list[1]
    elif len(max_num) == 2 :
        return (max_num[0])
    else :
        max_num.sort()
        return (max_num[2])

def fun_4() :
    b = max(list) - min(list)
    return b


print(fun_1())
print(fun_2())
print(fun_3())
print(fun_4())
