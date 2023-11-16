a, n = map(int,input().split())
result = 1
for i in range(n+1):
	result *= (a - i*n)
print(result)
