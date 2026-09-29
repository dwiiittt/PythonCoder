import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os


# =========================================================
# KONFIGURASI FILE
# =========================================================

# Mendapatkan folder tempat file Python berada
SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Lokasi birthdays.txt
BIRTHDAY_FILE = os.path.join(SCRIPT_FOLDER, "birthdays.txt")


# =========================================================
# MENGHITUNG HARI MENUJU ULANG TAHUN
# =========================================================

def get_days_until(birthday_str):
    """
    Menghitung berapa hari lagi menuju ulang tahun berikutnya.

    Format tanggal:
    DD/MM/YY
    """

    try:
        # Membaca tanggal dari birthdays.txt
        birthday = datetime.strptime(
            birthday_str,
            "%d/%m/%y"
        )

        today = datetime.now()

        # Ulang tahun menggunakan bulan dan tanggal
        # dari data, tetapi tahunnya menggunakan tahun sekarang
        next_birthday = datetime(
            today.year,
            birthday.month,
            birthday.day
        )

        # Jika ulang tahun tahun ini sudah lewat,
        # gunakan tahun depan
        if next_birthday.date() < today.date():
            next_birthday = datetime(
                today.year + 1,
                birthday.month,
                birthday.day
            )

        delta = next_birthday.date() - today.date()

        return delta.days

    except ValueError:
        return None


# =========================================================
# MEMBUAT FILE JIKA BELUM ADA
# =========================================================

def create_file_if_not_exists():

    if not os.path.exists(BIRTHDAY_FILE):

        try:
            with open(
                BIRTHDAY_FILE,
                "w",
                encoding="utf-8"
            ):
                pass

            print(
                f"File birthdays.txt dibuat di:\n"
                f"{BIRTHDAY_FILE}"
            )

        except Exception as e:

            print(
                f"Gagal membuat file:\n{e}"
            )


# =========================================================
# MEMBACA DATA BIRTHDAY
# =========================================================

def load_birthdays():

    events = []

    # Pastikan file tersedia
    create_file_if_not_exists()

    print("--------------------------------")
    print("Membaca file:")
    print(BIRTHDAY_FILE)
    print("--------------------------------")

    try:

        with open(
            BIRTHDAY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            for line in file:

                line = line.strip()

                # Lewati baris kosong
                if not line:
                    continue

                # Pastikan ada koma
                if "," not in line:
                    continue

                # Pisahkan nama dan tanggal
                name, date = line.split(",", 1)

                name = name.strip()
                date = date.strip()

                days_left = get_days_until(date)

                # Jika tanggal valid
                if days_left is not None:

                    events.append(
                        (
                            name,
                            date,
                            days_left
                        )
                    )

    except Exception as e:

        print(
            f"Terjadi kesalahan membaca file:\n{e}"
        )

    # Urutkan berdasarkan hari terdekat
    events.sort(
        key=lambda x: x[2]
    )

    return events


# =========================================================
# MENYIMPAN EVENT BARU
# =========================================================

def save_event(name, date):

    print("--------------------------------")
    print("Menyimpan event...")
    print("Nama     :", name)
    print("Tanggal  :", date)
    print("File     :", BIRTHDAY_FILE)
    print("--------------------------------")

    try:

        # Mode "a" = append
        # Data baru ditambahkan tanpa menghapus data lama
        with open(
            BIRTHDAY_FILE,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                f"{name},{date}\n"
            )

        print("Event berhasil disimpan!")

        return True

    except Exception as e:

        print(
            f"Gagal menyimpan event:\n{e}"
        )

        messagebox.showerror(
            "Error",
            f"Gagal menyimpan event:\n\n{e}"
        )

        return False


# =========================================================
# WINDOW ADD EVENT
# =========================================================

def open_add_event_window():

    global root

    # -----------------------------------------------------
    # Hancurkan Main Window
    # -----------------------------------------------------

    root.destroy()

    # -----------------------------------------------------
    # Buat Window Add Event
    # -----------------------------------------------------

    add_window = tk.Tk()

    add_window.title(
        "Add Birthday Event"
    )

    add_window.geometry(
        "500x400"
    )

    add_window.configure(
        bg="#ffe4c4"
    )

    # =====================================================
    # TITLE
    # =====================================================

    title_label = tk.Label(
        add_window,
        text="Add New Birthday Event",
        font=("Arial", 20, "bold"),
        fg="blue",
        bg="#ffe4c4"
    )

    title_label.pack(
        pady=25
    )

    # =====================================================
    # NAME LABEL
    # =====================================================

    name_label = tk.Label(
        add_window,
        text="Name:",
        font=("Arial", 12, "bold"),
        bg="#ffe4c4"
    )

    name_label.pack()

    # =====================================================
    # NAME ENTRY
    # =====================================================

    name_entry = tk.Entry(
        add_window,
        font=("Arial", 13),
        width=30
    )

    name_entry.pack(
        pady=8
    )

    # =====================================================
    # DATE LABEL
    # =====================================================

    date_label = tk.Label(
        add_window,
        text="Birthday (DD/MM/YY):",
        font=("Arial", 12, "bold"),
        bg="#ffe4c4"
    )

    date_label.pack(
        pady=(15, 0)
    )

    # =====================================================
    # DATE ENTRY
    # =====================================================

    date_entry = tk.Entry(
        add_window,
        font=("Arial", 13),
        width=30
    )

    date_entry.pack(
        pady=8
    )

    # =====================================================
    # CONTOH FORMAT
    # =====================================================

    example_label = tk.Label(
        add_window,
        text="Example: 25/12/26",
        font=("Arial", 10),
        fg="gray",
        bg="#ffe4c4"
    )

    example_label.pack()

    # =====================================================
    # SAVE FUNCTION
    # =====================================================

    def save_button():

        name = name_entry.get().strip()
        date = date_entry.get().strip()

        # -------------------------------------------------
        # Validasi nama
        # -------------------------------------------------

        if name == "":

            messagebox.showwarning(
                "Warning",
                "Please enter a name."
            )

            name_entry.focus()

            return

        # -------------------------------------------------
        # Validasi tanggal
        # -------------------------------------------------

        try:

            datetime.strptime(
                date,
                "%d/%m/%y"
            )

        except ValueError:

            messagebox.showwarning(
                "Invalid Date",
                "Please enter the date using:\n\n"
                "DD/MM/YY\n\n"
                "Example:\n"
                "25/12/26"
            )

            date_entry.focus()

            return

        # -------------------------------------------------
        # Simpan ke birthdays.txt
        # -------------------------------------------------

        success = save_event(
            name,
            date
        )

        # -------------------------------------------------
        # Jika berhasil
        # -------------------------------------------------

        if success:

            messagebox.showinfo(
                "Success",
                f"Birthday event for {name} "
                f"has been saved!"
            )

            # Tutup Add Event Window
            add_window.destroy()

            # Buka kembali Main Window
            create_main_window()

    # =====================================================
    # CANCEL FUNCTION
    # =====================================================

    def cancel_event():

        # Tutup Add Event Window
        add_window.destroy()

        # Kembali ke Main Window
        create_main_window()

    # =====================================================
    # BUTTON FRAME
    # =====================================================

    button_frame = tk.Frame(
        add_window,
        bg="#ffe4c4"
    )

    button_frame.pack(
        pady=30
    )

    # =====================================================
    # SAVE BUTTON
    # =====================================================

    save_btn = tk.Button(
        button_frame,
        text="Save",
        font=("Arial", 12, "bold"),
        bg="green",
        fg="white",
        width=12,
        padx=10,
        pady=5,
        command=save_button
    )

    save_btn.pack(
        side="left",
        padx=10
    )

    # =====================================================
    # CANCEL BUTTON
    # =====================================================

    cancel_btn = tk.Button(
        button_frame,
        text="Cancel",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        width=12,
        padx=10,
        pady=5,
        command=cancel_event
    )

    cancel_btn.pack(
        side="left",
        padx=10
    )

    # =====================================================
    # FOCUS KE NAME
    # =====================================================

    name_entry.focus()

    # =====================================================
    # JALANKAN WINDOW
    # =====================================================

    add_window.mainloop()


# =========================================================
# MAIN WINDOW
# =========================================================

def create_main_window():

    global root

    # -----------------------------------------------------
    # Buat Main Window
    # -----------------------------------------------------

    root = tk.Tk()

    root.title(
        "Family Birthday Countdown"
    )

    root.geometry(
        "650x550"
    )

    root.configure(
        bg="#ffe4c4"
    )

    # =====================================================
    # TITLE
    # =====================================================

    title_label = tk.Label(
        root,
        text="My Family Birthday Countdown",
        font=("Arial", 20, "bold underline"),
        fg="blue",
        bg="#ffe4c4"
    )

    title_label.pack(
        pady=20
    )

    # =====================================================
    # ADD EVENT BUTTON
    # =====================================================

    add_button = tk.Button(
        root,
        text="+ Add Event",
        font=("Arial", 12, "bold"),
        bg="blue",
        fg="white",
        padx=20,
        pady=7,
        command=open_add_event_window
    )

    add_button.pack(
        pady=5
    )

    # =====================================================
    # LIST FRAME
    # =====================================================

    list_frame = tk.Frame(
        root,
        bg="#ffe4c4"
    )

    list_frame.pack(
        pady=20,
        padx=50,
        fill="both",
        expand=True
    )

    # =====================================================
    # LOAD BIRTHDAY DATA
    # =====================================================

    birthday_list = load_birthdays()

    # =====================================================
    # JIKA TIDAK ADA DATA
    # =====================================================

    if not birthday_list:

        empty_label = tk.Label(
            list_frame,
            text="No birthday events found.",
            font=("Arial", 13),
            fg="gray",
            bg="#ffe4c4"
        )

        empty_label.pack(
            pady=30
        )

    # =====================================================
    # MENAMPILKAN DATA
    # =====================================================

    else:

        for i, (
            name,
            date,
            days
        ) in enumerate(birthday_list):

            # ---------------------------------------------
            # Event paling dekat = merah
            # ---------------------------------------------

            if i == 0:

                text_color = "red"

            else:

                text_color = "darkgreen"

            # ---------------------------------------------
            # Jika hari ini
            # ---------------------------------------------

            if days == 0:

                display_text = (
                    f"🎉 Today is "
                    f"{name}'s Birthday!"
                )

            # ---------------------------------------------
            # Jika masih beberapa hari lagi
            # ---------------------------------------------

            else:

                display_text = (
                    f"{name} - "
                    f"{date}\n"
                    f"It is {days} days "
                    f"until {name}'s Birthday"
                )

            # ---------------------------------------------
            # Label
            # ---------------------------------------------

            lbl = tk.Label(
                list_frame,
                text=display_text,
                font=("Arial", 13, "bold"),
                fg=text_color,
                bg="#ffe4c4",
                pady=7,
                justify="left"
            )

            lbl.pack(
                anchor="w"
            )

    # =====================================================
    # FOOTER
    # =====================================================

    now = datetime.now()

    time_info = (
        f"Date: {now.strftime('%d/%m/%Y')}\n"
        f"Time: {now.strftime('%H:%M:%S')}"
    )

    footer_label = tk.Label(
        root,
        text=time_info,
        font=("Arial", 10, "bold"),
        fg="darkred",
        bg="#ffe4c4",
        justify="right"
    )

    footer_label.pack(
        side="bottom",
        anchor="e",
        padx=20,
        pady=20
    )

    # =====================================================
    # JALANKAN MAIN WINDOW
    # =====================================================

    root.mainloop()


# =========================================================
# PROGRAM START
# =========================================================

print("========================================")
print(" FAMILY BIRTHDAY COUNTDOWN")
print("========================================")
print("Birthday file:")
print(BIRTHDAY_FILE)
print("========================================")

create_file_if_not_exists()

create_main_window()

