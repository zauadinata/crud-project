from utilss.operasi import append_data

def create_data(file_path):
    student_id      = input("Masukkan ID Siswa      : ")
    student_name    = input("Masukkan Nama Siswa    : ")
    uas_score       = input("Masukkan Nilai UAS     : ")
    
    student_data = f"{student_id},{student_name},{uas_score}"
    append_data(file_path, student_data)
    print(f"Data siswa {student_name} dengan ID {student_id} telah ditambahkan.")

