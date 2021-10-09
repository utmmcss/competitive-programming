from math import sqrt

L = []
n = int(input("n? "))
for i in range(n):
	L.append(int(input("element " + str(i) + ": ")))

k = int(sqrt(n))

bucket_index = [-1] * n
bucket_sum = [0] * (k+1)

b_index = -1
for i in range(n):
	if i % k == 0:
		b_index += 1
	bucket_index[i] = b_index
	bucket_sum[b_index] += L[i]

m = int(input("number of queries? "))

while m > 0:
	type = input("query type 1/2? ")

	if type == "1": # sum query
		l = int(input("l? "))
		r = int(input("r? "))
		ans = 0
		i = l
		while i < r and i % k != 0:
			ans += L[i]
			i += 1
		while i + k <= r:
			ans += bucket_sum[i // k]
			i += k

		while i <= r:
			ans += L[i]
			i += 1
		print("here is the answer:", ans)
	else:
		ind = int(input("ind? "))
		val = int(input("new val? "))
		b_num = ind // k
		bucket_sum[b_num] += val - L[ind]
		L[ind] = val
		print("query computations done")
	m -= 1
