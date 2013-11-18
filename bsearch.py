alphabet = []#[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

def bsearch(List, number):
	found = 0
	lenList = len(List)-1
	min = 0
	max = lenList
	x = 0
	if max <= min:
			return -1
	else:	
		while max >= min: 
			x = (max + min)/2
			if List[x] == number:
				found = [x]
				return x
			elif List[x] < number:
				min = x + 1
			else: 
				max = x - 1	
		return found

print bsearch(alphabet, 1)		
			



	

