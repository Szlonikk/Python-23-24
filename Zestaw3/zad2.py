def odwracanie (L, left, right) :
	
	left = int (left)
	right = int (right)
	
	i = 0
	połowa = (right - left) // 2
	while(i <= połowa):
		
		temp = L[left]
		L[left] = L[right]
		L[right] = temp
		
		left += 1
		right -= 1
		i += 1

def odwracanie_rek(L, left, right) :
	
	if left >= right:
		return
	
	left = int (left)
	right = int (right)
	
	temp = L[left]
	L[left] = L[right]
	L[right] = temp
	
	odwracanie_rek(L, left + 1, right - 1)