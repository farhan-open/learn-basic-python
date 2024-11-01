def cari_kata_di_file(nama_file, kata_cari):
    try:
        with open(nama_file, mode='r', encoding='utf-8') as file:
            posisi_akhir = 0
            while True:
                # Mencari kata di dalam file
                posisi = file.read().find(kata_cari, posisi_akhir)
                if posisi == -1:
                    break

                # Menggunakan method seek untuk berpindah ke posisi kata yang ditemukan
                file.seek(posisi)

                # Membaca satu baris dari posisi yang ditemukan
                baris = file.readline()
                print(baris.rstrip())  # Menghapus karakter newline dari baris

                # Update posisi_akhir untuk mencari kata berikutnya
                posisi_akhir = file.tell()
                print(posisi)

    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


if __name__ == "__main__":
    nama_file = "data.txt"
    kata_cari = input("Masukkan kata yang ingin dicari: ")
    print(f"Hasil pencarian kata '{kata_cari}' dalam file '{nama_file}':")
    cari_kata_di_file(nama_file, kata_cari)

kalimat = 'Ini adalah kalimat\n'
kalimat_juga = kalimat.strip()
print(kalimat)
print(kalimat_juga)
