'''MIN To MAX

https://www.codechef.com/practice/course/arrays/ARRAYS/problems/OPMIN

'''
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] > min(a):
            a[i] = min(a)
            count += 1 
    print(count)
    t -= 1
