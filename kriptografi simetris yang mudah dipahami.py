# Fungsi untuk enkripsi dan dekripsi menggunakan Caesar Cipher
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Mengatur arah pergeseran
    if mode == 'decrypt':
        shift = -shift  # Jika dekripsi, gunakan pergeseran negatif
    
    for char in text:
        # Enkripsi huruf kapital
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        # Enkripsi huruf kecil
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # Biarkan karakter non-huruf tetap sama
            
    return result

# Input dari pengguna
text = input("Masukkan teks: ")
shift = int(input("Masukkan pergeseran (shift): "))

# Pilihan mode
mode = input("Apakah Anda ingin (E)nkripsi atau (D)ekripsi? ").lower()

if mode == 'e':
    encrypted_text = caesar_cipher(text, shift, mode='encrypt')
    print("Teks terenkripsi:", encrypted_text)
elif mode == 'd':
    decrypted_text = caesar_cipher(text, shift, mode='decrypt')
    print("Teks terdekripsi:", decrypted_text)
else:
    print("Pilihan tidak valid. Silakan pilih E untuk enkripsi atau D untuk dekripsi.")
