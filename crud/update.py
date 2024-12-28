import os
from utilss.operasi import update_data, read_data

def update_data_menu(file_path):
    data = read_data(file_path)
    if data:
        # Bersihkan layar sebelum menampilkan data
        os.system('cls' if os.name == 'nt' else 'clear')

        # Tentukan panjang terpanjang untuk setiap kolom
        max_id_len = max(len(item.split(',')[0]) for item in data)
        max_name_len = max(len(item.split(',')[1]) for item in data)
        max_score_len = max(len(item.split(',')[2]) for item in data)

        # Menambahkan ruang ekstra untuk header
        max_name_len = max(max_name_len, len("Nama"))  # Untuk memastikan "Nama" pas
        max_score_len = max(max_score_len, len("Nilai UAS"))  # Untuk memastikan "Nilai UAS" pas
        
        # Header tabel
        print("=" * (max_id_len + max_name_len + max_score_len + 18))
        print("|             Data Siswa                       |")
        print("=" * (max_id_len + max_name_len + max_score_len + 18))
        print(f"| No  | {'ID'.ljust(max_id_len)} | {'Nama'.ljust(max_name_len)} | {'Nilai UAS'.ljust(max_score_len)} |")
        print("=" * (max_id_len + max_name_len + max_score_len + 18))

        # Menampilkan data siswa dengan lebar kolom yang disesuaikan
        for i, item in enumerate(data, 1):
            student_id, student_name, uas_score = item.split(',')
            print(f"| {i:<3} | {student_id:<{max_id_len}} | {student_name:<{max_name_len}} | {uas_score:<{max_score_len}} |")

        print("=" * (max_id_len + max_name_len + max_score_len + 18))

        # Memilih data siswa yang ingin diperbarui
        try:
            index = int(input("Pilih nomor data siswa yang ingin diperbarui  : ")) - 1
            if 0 <= index < len(data):
                student_id, student_name, uas_score = data[index].split(',')
                new_name = input(f"Masukkan nama baru (sekarang: {student_name})     : ")
                new_uas = input(f"Masukkan nilai UAS baru (sekarang: {uas_score})   : ")

                # Format data baru
                new_data = f"{student_id},{new_name},{new_uas}"

                # Memperbarui data siswa
                if update_data(file_path, data[index], new_data):
                    print(f"Data siswa dengan ID {student_id} telah diperbarui.")
                else:
                    print("Gagal memperbarui data.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input tidak valid.")
    else:
        print("Tidak ada data siswa untuk diperbarui.")

    input("Tekan Enter untuk kembali ke menu...")
