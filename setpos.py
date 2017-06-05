def setpos(x1,y1):
	
	x = float(input('Please enter an x-coordinate: '))
	y = float(input('Please enter a y-coordinate: '))

	
	n = int(abs(x-x1)/.05)
	m = int(abs(y-y1)/.05)
	
	if m>n:
		n = m
	
	#condition 1
	if x>=x1 and y>=y1:
		for i in range(0, n):
			if x>x1:
				x1 = x1+.05
				print(x1)
				list.append(x1)
			else:
				x1 = x1+0
				print(x1)
				
			if y>y1:
				y1 = y1+.05
				print(y1)
				list1.append(y1)
			else:
				y1 = y1+0
				print(y1)

	#condition 2
	if x>=x1 and y<=y1:
		for i in range(0, n):
			if x>x1:
				x1 = x1+.05
				print(x1)
			else:
				x1 = x1+0
				print(x1)
				
			if y<y1:
				y1 = y1-.05
				print(y1)
			else:
				y1 = y1+0
				print(y1)


	#condition 3
	if x<=x1 and y>=y1:
		for i in range(0, n):
			if x<x1:
				x1 = x1-.05
				print(x1)
			else:
				x1 = x1+0
				print(x1)
				
			if y>y1:
				y1 = y1+.05
				print(y1)
			else:
				y1 = y1+0
				print(y1)

	#condition 4
	if x<=x1 and y<=y1:
		for i in range(0, n):
			if x<x1:
				x1 = x1-.05
				print(x1)
			else:
				x1 = x1+0
				print(x1)
				
			if y<y1:
				y1 = y1-.05
				print(y1)
			else:
				y1 = y1+0
				print(y1)
list = []
list1 = []
setpos(0,0)	

