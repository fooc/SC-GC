mind = 1000000000
pos = 0
with open("xy_LA.txt") as f:
	num = 0
	done = 0
	while not done and num < 20000:
		line = f.readline()
		if line:
			done = 0
			items = line.split(" ")
			x = int(items[2])
			y = int(items[3])
			d = (x - 141922) * (x - 141922) + (y - 42333) * (y - 42333)
			if mind > d:
				mind = d
				pos = num
		else:
			done = 1
		num = num + 1

print mind, pos
