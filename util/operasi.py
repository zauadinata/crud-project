# Fungsi untuk membaca data dari file
def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return []

# Fungsi untuk menulis data ke file
def write_data(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

# Fungsi untuk menambahkan data ke file
def append_data(file_path, data):
    with open(file_path, 'a') as file:
        file.write(f"{data}\n")

# Fungsi untuk memperbarui data di file
def update_data(file_path, old_data, new_data):
    data = read_data(file_path)
    if old_data in data:
        data[data.index(old_data)] = new_data
        write_data(file_path, data)
        return True
    return False

# Fungsi untuk menghapus data dari file
def delete_data(file_path, data_to_delete):
    data = read_data(file_path)
    if data_to_delete in data:
        data.remove(data_to_delete)
        write_data(file_path, data)
        return True
    return False
