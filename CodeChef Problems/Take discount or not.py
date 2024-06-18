'''
https://www.codechef.com/practice/course/arrays/ARRAYS/problems/DISCOUNTT?tab=statement

'''
t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    initial_cost = 0
    final_cost = 0
 
    for i in range(n):
        initial_cost += a[i]
        if a[i] < y:
            a[i] = 0
        else:
            a[i] = a[i] - y
        final_cost += a[i]
    final_cost += x
    
    if final_cost < initial_cost:
        print('COUPON')
    else:
        print('NO COUPON')
 
        