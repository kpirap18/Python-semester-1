def insertion_binary(data):
	for i in range(len(data)):
		k = False
		key = data[i]
		lo, hi = 0, i - 1
		while lo < hi:
			mid = lo + (hi - lo) // 2
			if key < data[mid]:
				hi = mid
			else:
				lo = mid + 1		
		for j in range(i, lo , -1):
			data[j] = data[j - 1]; k = True
		if k: data[lo] = key
	return data

a = [9,8,7,6,5,4,3,3]
print(a)
s = insertion_binary(a)
print(s)
