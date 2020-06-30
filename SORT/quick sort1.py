def quick(data):
	less = []
	pivotList = []
	more = []
	if len(data) <= 1:
		return data
	else:
		pivot = data[0]
		for i in data:
			if i < pivot:
				less.append(i)
			elif i > pivot:
				more.append(i)
			else:
				pivotList.append(i)
		less = quick(less)
		more = quick(more)
		return less + pivotList + more

a = [3,67,43,2,3,0,5,8,4]
s = quick(a)
print(s)
