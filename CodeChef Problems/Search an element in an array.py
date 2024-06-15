'''Search an element in an array

You are given an array A of size N and an element X. Your task is to find whether the array A contains the element 
X or not.

Input Format
The first line contains two space-separated integers N and X — the size of array and the element to be searched.
The second line contains all the elements of array A

Output Format
Output "YES" if the element 
X is present in A, otherwise output "NO".'''

N, num = map(int, input().split())
array = list(map(int, input().split()))

def findArray(num,array):
    for i in array:
        if i == num:
            print('YES')
            return
    print('NO')

findArray(num,array)