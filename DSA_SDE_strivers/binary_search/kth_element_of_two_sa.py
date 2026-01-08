'''

'''

def find_k(a, b, k):
    i, j = 0, 0
    n1, n2 = len(a), len(b)

    while True:
        if i == n1:
            return b[j + k - 1]
        if j == n2:
            return a[i+k-1]
        if k == 1:
            return min(a[i], b[j])
        
        mid1 = min(n1-i, k//2)
        mid2 = min(n2-j, k//2)

        if a[i+mid1-1] < b[j+mid2-1]:
            i += mid1
            k-=mid1
        else:
            j+=mid2
            k-=mid2


a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
res = find_k(a, b, k)
print(res)