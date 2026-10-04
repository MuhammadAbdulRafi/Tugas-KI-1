import socket
from des_core import encrypt

# Key yang disepakati (hardcoded, harus sama dengan receiver)
SHARED_KEY = "key12345"

def start_sender():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect(('localhost', 63776))
        
        print("=== APLIKASI PENGIRIM PESAN (DES) ===")
        pesan = input("Masukkan pesan rahasia: ")
        
        print("\nSedang mengenkripsi...")
        ciphertext = encrypt(pesan, SHARED_KEY)
        
        print(f"Ciphertext (Biner): {ciphertext}")
        
        # Mengirim data yang sudah dienkripsi
        client_socket.sendall(ciphertext.encode('utf-8'))
        print("\nData berhasil dikirim ke Receiver!")
        
    except ConnectionRefusedError:
        print("Gagal terhubung! Pastikan receiver.py sudah dijalankan terlebih dahulu.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_sender()