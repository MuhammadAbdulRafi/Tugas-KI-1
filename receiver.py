import socket
from des_core import decrypt

# Key yang disepakati (hardcoded, harus sama dengan sender)
SHARED_KEY = "key12345" 

def start_receiver():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 63776))
    server_socket.listen(1)
    
    print("Menunggu pesan dari Sender...")
    conn, addr = server_socket.accept()
    
    with conn:
        print(f"Terhubung dengan: {addr}")
        
        # Menerima data Ciphertext
        encrypted_data = conn.recv(4096).decode('utf-8')
        if encrypted_data:
            print("\n--- DATA DITERIMA ---")
            print(f"1. Ciphertext (Biner): {encrypted_data}")
            
            # Mendekripsi data
            try:
                decrypted_text = decrypt(encrypted_data, SHARED_KEY)
                print(f"2. Hasil Dekripsi (Plaintext): {decrypted_text}")
            except Exception as e:
                print(f"Gagal mendekripsi. Error: {e}")

if __name__ == "__main__":
    start_receiver()