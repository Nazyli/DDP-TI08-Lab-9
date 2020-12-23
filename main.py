# Nama: Evry Nazyli Ciptanto
# NIM: 0110220045
# Kelas: TI08

def sort_desc(arr):
  # Tulis kode fungsi sort_desc di bawah ini
  # melakukan pengurutan dengan metode bubble sort
  # penjelasan code ada di bawah (memakai cara bubble sort)
  for x in range(len(arr)): #[1]
    for y in range(1, len(arr)-x): #[2]
      if arr[y] > arr[y-1]:#[3]
        arr[y],arr[y-1] = arr[y-1],arr[y] #[4]
    
  # Fungsi sort_desc mengembalikan array yang terurut
  return arr #[5]
# penjelasan code :
# metodhe pengurutan yang dipakai adalah dengan metode bubble sort, dibandingkan dengan elemen sebelahnya
# [1] melakukan perulangan arr
# [2] melakukan perulangan ke dua dengan index ke 1 dan nilai akhir dikurang dengan x (memperpendek perulangan)
# [3] pengecekan kondisi apakah array di index ini lebih besar dar array sebelumnya
# [4] jika kondisi[3] true > melakukan perpindahan nilai dimana array sekarang diisi array sebelumnya dan array sebelumnya diisi array sekarang
# [5] mengembalikan array yang telah diurutkan



# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = sort_desc([2, 3, 1, 0, 4])
  print(f"sort_desc([2, 3, 1, 0, 4]) = {r} \n(solusi: [4, 3, 2, 1, 0]")
  print()
  r = sort_desc([1, 2, 3])
  print(f"sort_desc([1, 2, 3]) = {r} \n(solusi: [3, 2, 1]")
  print()

if __name__ == '__main__':
  test()