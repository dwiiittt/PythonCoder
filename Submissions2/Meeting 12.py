from tkinter import Tk, messagebox, font, Label, Entry, Button
import os

# --- PENGATURAN LOKASI FILE ---
# Mengambil lokasi folder tempat script ini disimpan
BASE_DIR = os.path.dirname(__file__)
# Menggabungkan lokasi folder dengan nama file txt
FILE_PATH = os.path.join(BASE_DIR, 'm12_capital_data.txt')

def custom_askstring(title, prompt, dialog_size="450x200", bg_color="lightblue", font_size=15, font_weight="bold"):
    dialog = Tk()
    dialog.title(title)
    dialog.configure(bg=bg_color)
    dialog.geometry(dialog_size)
    
    # Membuat window muncul di tengah layar
    dialog.eval('tk::PlaceWindow . center')
    
    custom_font = font.Font(size=font_size, weight=font_weight)
    
    label = Label(dialog, text=prompt, bg=bg_color, font=custom_font, pady=10)
    label.pack()
    
    entry = Entry(dialog, font=custom_font)
    entry.pack(pady=10)
    entry.focus_set()

    # Inisialisasi hasil agar tidak error jika jendela ditutup paksa
    dialog.result = ""

    def ok():
        dialog.result = entry.get().strip()
        dialog.destroy()

    # Bind tombol Enter keyboard ke fungsi ok
    dialog.bind('<Return>', lambda event: ok())

    button = Button(dialog, text="OK", command=ok, bg="white", font=custom_font, width=10)
    button.pack(pady=10)

    dialog.wait_window()
    return dialog.result

# --- LOGIKA DATA ---
the_world = {}

def read_from_file():
    """Membaca data dari m12_capital_data.txt jika file tersebut ada"""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            for line in file:
                line = line.strip()
                if '/' in line:
                    country, city = line.split('/')
                    # Disimpan dalam huruf kecil untuk pencarian yang fleksibel
                    the_world[country.strip().lower()] = city.strip()
    else:
        print(f"Peringatan: File tidak ditemukan di {FILE_PATH}")

def write_to_file(country, city):
    """Menambahkan data baru ke dalam file tanpa menghapus data lama"""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'a') as file:
            # Menambah baris baru dengan format Negara/Ibukota
            file.write(f'\n{country}/{city}')

# --- PROGRAM UTAMA ---
# 1. Muat data dari file saat program dimulai
read_from_file()

# 2. Sembunyikan jendela utama Tkinter
main_root = Tk()
main_root.withdraw()

print('Ask the Expert - Capital Cities of the World')

while True:
    query_country = custom_askstring('Country', 'Type the name of a country:', bg_color="lightgreen")
    
    # Berhenti jika input kosong atau jendela dialog ditutup (X)
    if not query_country:
        break 
    
    # Ubah input menjadi huruf kecil agar cocok dengan database 'the_world'
    lookup_name = query_country.lower()
        
    if lookup_name in the_world:
        result = the_world[lookup_name]
        messagebox.showinfo('Answer', f'The capital city of {query_country} is {result}!')
    else:
        new_city = custom_askstring('Teach me', f'I don\'t know! What is the capital city of {query_country}?')
        if new_city:
            # Simpan ke memori (dictionary)
            the_world[lookup_name] = new_city
            # Simpan permanen ke file txt
            write_to_file(query_country, new_city)
            messagebox.showinfo('Thanks', f'I have learned that the capital of {query_country} is {new_city}!')

# Tutup aplikasi sepenuhnya
main_root.destroy()