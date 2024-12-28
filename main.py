import os
from CRUD.create import create_data
from CRUD.read import display_data
from CRUD.update import update_data_menu
from CRUD.delete import delete_data_menu

FILE_PATH = "dataa/data.txt"

def menu():
    # Bersihkan layar terminal sebelum mencetak menu
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print ('    WELCOME TO CRUD    ')
    print ('=======================')
    print ("| Menu CRUD Siswa   : |")
    print ("| 1. Create data      |")
    print ("| 2. Read data        |")
    print ("| 3. Update data      |")
    print ("| 4. Delete data      |")
    print ("| 5. Exit             |")
    print ('=======================')

    return input("Pilih opsi     : ")

def main():
    while True:
        choice = menu()
        if choice == "1":
            create_data(FILE_PATH)
            input("Data berhasil dibuat. Tekan Enter untuk kembali ke menu...")
        elif choice == "2":
            display_data(FILE_PATH)
            input("Tekan Enter untuk kembali ke menu...")
        elif choice == "3":
            update_data_menu(FILE_PATH)
            input("Data berhasil diperbarui. Tekan Enter untuk kembali ke menu...")
        elif choice == "4":
            delete_data_menu(FILE_PATH)
            input("Data berhasil dihapus. Tekan Enter untuk kembali ke menu...")
        elif choice == "5":
            print("Terima kasih! Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
