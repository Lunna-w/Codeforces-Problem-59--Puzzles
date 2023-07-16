n, m = map(int, input().split())

s = sorted(map(int, input().split()))  


min_diff = min(s[i+n-1] - s[i] for i in range(m-n+1)) 

print(min_diff)