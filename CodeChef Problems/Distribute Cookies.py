'''Distribute Cookies

https://www.codechef.com/START139D/problems/DISCOOKIE

'''

t = int(input())
data_list = []
while t > 0:
    n,m = map(int, input().split())
    data_list.append([n,m])
    t = t-1
    
for i in range(len(data_list)):
    n = data_list[i][0]
    m = data_list[i][1]
    count1 = m
    count2 = m
    
    if m % n == 0:
        print(0)
        continue
    
    count2 -= (m%n)
    count1 = ((m//n)+1)*n
    
    
    if count2 == 0:
        print(count1-m)
        continue
    
    if (count1 - m) > (m-count2):
        print(m-count2)
        continue
        
    else:
        print(count1-m)
    
    