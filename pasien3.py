import time
import sys
import os
from colorama import init, Fore
from tabulate import tabulate

class Patient:
    def __init__(self, name, age, gender, symptoms):
        self.name = name
        self.age = age
        self.gender = gender
        self.symptoms = symptoms

class reset():
    def deactive():
        init(autoreset=False)

    def active():
        init(autoreset=True)


def show_typing_animation(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def show_typing_animation1(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    banner = (
        "__________  _____________ ___________             ____  __.________        ____.  _____    ",
        "\______   \/   _____/    |   \______ \           |    |/ _|\_____  \      |    | /  _  \   ",
        " |       _/\_____  \|    |   /|    |  \   ______ |      <   /   |   \     |    |/  /_\  \  ",
        " |    |   \/        \    |  / |    |   \ /_____/ |    |  \ /    |    \/\__|    /    |    \ ",
        " |____|_  /_______  /______/ /_______  /         |____|__ \_______   /\________\____|__  / ",
        "        \/        \/                 \/                  \/        \/                  \/  "
    )

    for line in banner:
        show_typing_animation1(Fore.CYAN + line + "\n")
        time.sleep(0.1)

def main():
    clear_screen()
    banner()
    time.sleep(1)
    reset.active()

    print(Fore.GREEN + "Selamat datang di sistem pendaftaran pasien rumah sakit koja!")
    time.sleep(1)
    patients = []

    while True:
        print("Menu:")
        print(Fore.CYAN + "1. Daftarkan pasien baru")
        print("2. Tampilkan daftar pasien")
        print(Fore.RED + "3. Keluar")

        choice = input(Fore.YELLOW + "Masukkan pilihan (1/2/3): ")

        if choice == '1':
            clear_screen()
            print(Fore.CYAN + "== Daftarkan Pasien Baru ==")
            name = input("Nama pasien: ")
            age = int(input("Usia pasien: "))
            gender = input("Jenis kelamin pasien (L/P): ")
            symptoms = input("Gejala pasien: ")

            print(Fore.YELLOW + "Mendaftarkan pasien", end = " ")
            show_typing_animation("...")
            time.sleep(1)

            patient = Patient(name, age, gender, symptoms)
            patients.append(patient)
            print(Fore.GREEN + "\nPasien berhasil didaftarkan.")
            time.sleep(1)
            clear_screen()

        elif choice == '2':
            clear_screen()
            time.sleep(1)
            print(Fore.CYAN + "== Daftar Pasien ==")
            patient_data = []
            for idx, patient in enumerate(patients, 1):
                patient_data.append([idx, patient.name, patient.age, patient.gender, patient.symptoms])

            headers = ["No.", "Nama", "Usia", "Jenis Kelamin", "Gejala"]
            print(tabulate(patient_data, headers=headers, tablefmt="grid"))
            time.sleep(1)
            input(Fore.YELLOW + "\nTekan 'Enter' untuk kembali ke menu...")
            clear_screen()
            time.sleep(1)

        elif choice == '3':
            clear_screen()
            time.sleep(1)
            show_typing_animation("Terima kasih telah berobat di sini ^_^ \nSemoga lekas sembuh...\n")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
            time.sleep(1)
            clear_screen()

if __name__ == "__main__":
    main()
