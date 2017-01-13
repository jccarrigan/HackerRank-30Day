arr = []
for _ in xrange(6):
	arr_temp = map(int,raw_input().strip().split(' '))
	arr.append(arr_temp)

max = -70
for x in [1, 2, 3, 4]:
	for y in [1, 2, 3, 4]:
		hourglass = [arr[y-1][x-1], arr[y-1][x], arr[y-1][x+1], arr[y][x], arr[y+1][x-1], arr[y+1][x], arr[y+1][x+1]]
		adding = sum(hourglass)
		if adding > max:
			max = adding
print max
