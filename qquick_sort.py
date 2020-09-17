def qquick_sort(arr):
	

	def partition(arr,l,h):
		j = l+1
		for i in range(l+1,h+1):
			if arr[i]<arr[l]:
				arr[i], arr[j] =arr[j],arr[i]
				j+=1
		arr[l],arr[j-1] = arr[j-1], arr[l]
		return j-1
	
	def helper(arr, l, h):
		if l>=h:
			return
		else:
			pivot = partition(arr,l,h)
			helper(arr, l, pivot-1)
			helper (arr, pivot+1, h)

	low = 0
	high = len(arr)-1
	helper(arr, low, high)
	return arr
