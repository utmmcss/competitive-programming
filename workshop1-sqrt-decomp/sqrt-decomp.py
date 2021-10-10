from math import sqrt


L = []
n = int(input("n? "))
for i in range(n):
	L.append(int(input("element " + str(i) + ": ")))

k = int(sqrt(n))

# initialize the bucket index of every element, and calc sum of buckets

bucket_index = [-1] * n
bucket_sum = [0] * (n // k + 1)

b_index = -1
for i in range(n):
	if i % k == 0: # every time we reach beginning of new bucket
		b_index += 1
	bucket_index[i] = b_index
	bucket_sum[b_index] += L[i]

m = int(input("num queries? "))

while m > 0:
	type = input("type 1/2? ")

	if type == "1": # sum query
		l = int(input("l? "))
		r = int(input("r? "))
		ans = 0
		i = l

		# add everything after l that is not in the next bucket
		while (i < r and i % k != 0):
			ans += L[i]
			i += 1

		# sum up every bucket in between
		while (i + k <= r):
			ans += bucket_sum[bucket_index[i]]
			i += k

		# sum up everything before r that is not in the previous bucket

		while (i <= r):
			ans += L[i]
			i += 1

		print("answer:", ans)

	else: # update element query
		ind = int(input("ind? "))
		val = int(input("new val? "))
		b_num = bucket_index[ind]
		bucket_sum[b_num] += val - L[ind]
		L[ind] = val
		print("query done!")

	m -=1


