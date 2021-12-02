n = input("Masukkan deret angka: ")
da = n.split(",")
sum = 0
z = ''
for i in da:
	if int(i)%2 == 0:
		angka = 0 + int(i)
	else:
		angka = 0 - int(i)
	sum = sum + angka
print("Total: ",end='' )
for i in da:
	
	if int(i)%2 == 0:
		x = (" + "+str(i))
	else:
		x = (" - "+str(i))
	z = z+x

if z[1] == "+":
	print(z[2:len(z)])
else:
	print(z)
print("Hasil perhitungan di atas ialah: ",sum)