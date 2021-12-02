n = int(input("Input: "))
y = n
print("Output: ")
if n == 0:
	print(" ")
elif n < 0:
	print("maaf input salah ")
elif n == 2:
	print(" * ")
	print("* *")
elif n == 1:
	print("*")
else:
	print(" "*(n-1)+"*"+" "*(n-1))
	for i in range (1,n):
		print(" "*(n-1-i) + "*" + " "*(i*2-1) +"*"+ " "*(n-1-i))
		if i == n-2:
			break
	for j in range(n):
		print("*",end=' ' )