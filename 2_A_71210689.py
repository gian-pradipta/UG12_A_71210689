orang = []
nomor = []
while True:
	nama = (input("Masukkan nama: "))
	if nama == "STOP":
		break
	else:
		kursi = (input("Masukkan nomor kursi "+nama+": "))
	
	if kursi in nomor:
		print("Mohon maaf, kursi tersebut telah terisi")
	else:
		orang.append(nama)
		nomor.append(kursi)
		
print("\nLihat kursi yang telah terisi: ")

for i in range(len(nomor)):
	print("Kursi nomor",nomor[i],"telah diisi oleh", orang[i])
	

	
		
	
	
	
		
	