inpt = input("Input: ")
x = 0
y = 0
print("Output:")
while y < len(inpt):
	print(inpt[0:y])
	y += 1
while x < len(inpt):
	print(inpt[0:len(inpt)-x])
	x += 1
	