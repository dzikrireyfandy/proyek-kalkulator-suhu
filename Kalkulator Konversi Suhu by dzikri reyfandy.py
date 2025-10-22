# Kalkulator Konversi Suhu
# Nama  : Muhammad Dzikri Reyfandy
# NIM   : L0225056

# --- Konstanta ---
# Menyimpan nilai yang tidak berubah di satu tempat 
PETA_PILIHAN_SKALA = {
    "a": "c",
    "b": "f",
    "c": "r",
    "d": "k"
}

# Batas suhu minimum (Nol Absolut)
BATAS_SUHU = {
    "c": -273.15,
    "f": -459.67,
    "r": -218.52,
    "k": 0
}

# --- Fungsi Konversi & Validasi ---

def konversi_suhu(nilai: float, dari: str, ke: str) -> float | None:
    """Mengonversi nilai suhu dari satu skala ke skala lain."""
    dari = dari.lower()
    ke = ke.lower()

    # 1. Ubah semua ke Celcius sebagai standar tengah
    c = None
    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5/9
    elif dari == "r":
        c = nilai * 5/4
    elif dari == "k":
        c = nilai - 273.15

    # 2. Ubah dari Celcius ke skala tujuan
    if ke == "c":
        return c
    elif ke == "f":
        return (c * 9/5) + 32
    elif ke == "r":
        return c * 4/5
    elif ke == "k":
        return c + 273.15
    else:
        return None 

def cek_batas_valid(nilai: float, skala: str) -> bool:
    """Memeriksa apakah nilai suhu di atas batas minimum (Nol Absolut)."""
    return nilai >= BATAS_SUHU[skala]

# --- Fungsi untuk Input & Tampilan (User Interface) ---

def tampilkan_menu():
    """Menampilkan pilihan menu skala suhu."""
    print("\nPilih skala suhu:")
    print("A. Celcius (C)")
    print("B. Fahrenheit (F)")
    print("C. Reamur (R)")
    print("D. Kelvin (K)")
    print("-------------------------")

def dapatkan_pilihan_skala(prompt: str) -> str:
    """Meminta input pilihan skala (A/B/C/D) dan memvalidasinya."""
    while True:
        pilihan = input(prompt).lower()
        skala = PETA_PILIHAN_SKALA.get(pilihan)
        if skala:
            return skala # Mengembalikan "c", "f", "r", atau "k"
        print("Pilihan salah! Harap masukkan A, B, C, atau D.")

def dapatkan_nilai_suhu(skala_awal: str) -> float:
    """Meminta input nilai suhu dan memvalidasinya (harus angka & > batas)."""
    while True:
        try:
            nilai_str = input(f"Masukkan nilai suhu dalam {skala_awal.upper()}: ")
            nilai = float(nilai_str) 
            
            # Cek batas minimum
            if not cek_batas_valid(nilai, skala_awal):
                print(f"Suhu tidak valid. Minimum untuk {skala_awal.upper()} adalah {BATAS_SUHU[skala_awal]}.")
                continue # Ulangi loop
                
            return nilai # Kembalikan nilai jika sudah valid
            
        except ValueError:
            # Ini akan jalan jika float(nilai_str) gagal
            print("Input harus berupa angka (contoh: 50 atau 36.5). Coba lagi.")

def tanya_lanjut() -> bool:
    """Tanya ke user apakah mau lanjut atau keluar. Mengembalikan True/False."""
    while True:
        lagi = input("\nKetik 'y' untuk lanjut, 'g' untuk keluar: ").lower()
        if lagi == "y":
            print("-" * 30, "\n")
            return True # Lanjut
        if lagi == "g":
            return False # Berhenti
        print("Input salah, ketik 'y' atau 'g'.")

# --- Fungsi Utama (Titik Masuk Program) ---

def main():
    """Fungsi utama yang menjalankan alur program kalkulator."""
    print("=" * 30)
    print("KALKULATOR SUHU by Dzikri Reyfandy")
    print("=" * 30)
    
    while True:
        # 1. Tampilkan menu
        tampilkan_menu()
        
        # 2. Input Skala Awal
        skala_awal = dapatkan_pilihan_skala("Pilih suhu AWAL (A/B/C/D): ")
        
        # 3. Input Nilai
        nilai = dapatkan_nilai_suhu(skala_awal)
        
        # 4. Input Skala Tujuan
        skala_akhir = dapatkan_pilihan_skala("Pilih suhu TUJUAN (A/B/C/D): ")
        
        # 5. Proses & Tampilkan Hasil
        hasil = konversi_suhu(nilai, skala_awal, skala_akhir)
        print("\n--- HASIL KONVERSI ---")
        #:.2f artinya format angka jadi 2 desimal di belakang koma
        print(f"{nilai:.2f} {skala_awal.upper()} = {hasil:.2f} {skala_akhir.upper()}")
        print("-" * 22)
        
        # 6. Tanya Lanjut
        if not tanya_lanjut():
            break # Keluar dari loop 'while True'

    print("\nTerima kasih sudah pakai program ini.")
    print("Semoga sehat selalu dan dimudahkan segala urusan :)")


if __name__ == "__main__":
    main()