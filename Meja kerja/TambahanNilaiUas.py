Angka = [1,2,3,4,5]
# Menampilkan Semua Isi List Soal 1
print("Tampilkan Seluruh Isi List", Angka)
print("Tampilkan Index Ke 1 =", Angka[1])

# Melihat Panjang Element
print("Panjang Element = ", len (Angka))

#Menambahkan Element/ Soal 2
Angka.append(5)
print("Tampilkan Isi List Setelah Ditambahkan =", Angka)

# Menyisipkan Element
Angka.insert(2, 10)
print("Setelah Disisipkan =", Angka)
print("Tampilkan Isi List Setelah Ditambahkan =", Angka)

#Menghapus Index
Angka.pop(0)
print("Setelah Di Hapus Index = ", Angka)

#Menghapus Element
Angka.remove(3)
print("Setelah Di Hapus Element = ", Angka)

# Sortir Element
Angka.sort()
print("Sortir Element = ", Angka)

Angka [4] = 20
print("setelah di ubah element =", Angka)

sorted(Angka,reverse=True)
print(Angka)

