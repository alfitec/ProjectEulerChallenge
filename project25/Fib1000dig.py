fibSequence=[1,1]
first1000dig=10**999


for n in range(10000):
	newNum=fibSequence[-2]+fibSequence[-1]
	fibSequence.append(newNum)
	if newNum>first1000dig:
		print(len(fibSequence))
		# print(fibSequence)
		break
