'''
https://www.codechef.com/practice/course/arrays/ARRAYS/problems/UWCOI20A?tab=statement

'''

for I in range(int(input())):
    k=[]
    n=int(input())
    for j in range(n):
        a=int(input())
        k.append(a)
    print(max(k))