import os
from utilss.operasi import read_data

def display_data(file_path):
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
        print("|             Data Siswa             |")
        print("=" * (max_id_len + max_name_len + max_score_len + 18))
        print(f"| No  | {'ID'.ljust(max_id_len)} | {'Nama'.ljust(max_name_len)} | {'Nilai UAS'.ljust(max_score_len)} |")
        print("=" * (max_id_len + max_name_len + max_score_len + 18))
        
        # Menampilkan data siswa dengan lebar kolom yang disesuaikan
        for i, item in enumerate(data, 1):
            student_id, student_name, uas_score = item.split(',')
            print(f"| {i:<3} | {student_id:<{max_id_len}} | {student_name:<{max_name_len}} | {uas_score:<{max_score_len}} |")
        
        print("=" * (max_id_len + max_name_len + max_score_len + 18))
    else:
        print("Tidak ada data siswa.")
    
    input("Tekan Enter untuk kembali ke menu...")

