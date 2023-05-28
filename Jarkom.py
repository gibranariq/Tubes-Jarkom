import socket # Impor modul socket untuk komunikasi jaringan

def tcp_server():
    SERVER_HOST = "localhost"  # Menentukan host server
    SERVER_PORT = 8080  # Menentukan port server

    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Membuat objek soket
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Mengatur opsi soket

    sock_server.bind((SERVER_HOST, SERVER_PORT))  # Mengikat soket ke alamat dan port yang ditentukan

    sock_server.listen()  # Menerima koneksi masuk

    print("Server ready to serve")  # Menampilkan pesan server siap

    while True:  # Memulai loop tak terbatas
        sock_client, client_address = sock_server.accept()  # Menerima koneksi dari klien

        request = sock_client.recv(1024).decode()  # Menerima permintaan dari klien
        print("Dari client: " + request)  # Menampilkan permintaan dari klien

        response = handle_request(request)  # Menangani permintaan dan mendapatkan respons

        sock_client.send(response.encode())  # Mengirim respons kembali ke klien

        sock_client.close()  # Menutup koneksi dengan klien
    # endwhile

    sock_server.close()  # Menutup soket server



def handle_request(request):
    try:
        filename = request.split()[1][1:]  # Mendapatkan nama file dari permintaan
        with open(filename, 'r') as file:  # Membuka file untuk membaca kontennya
            message_body = file.read()  # Membaca isi file
        response_line = "HTTP/1.1 200 OK\r\n"  # Menyusun baris respons dengan kode 200 OK
        content_type = "Content-Type: text/html\r\n\r\n"  # Menyusun header respons dengan tipe konten teks/html
        response = response_line + content_type + message_body  # Menggabungkan baris respons, header, dan body
    except FileNotFoundError:
        response_line = "HTTP/1.1 404 Not Found\r\n"  # Menyusun baris respons dengan kode 404 Not Found
        content_type = "Content-Type: text/html\r\n\r\n"  # Menyusun header respons dengan tipe konten teks/html
        message_body = "<h1>404 Not Found</h1><p>File tidak tersedia pada server.</p>"  # Membuat pesan body respons
        response = response_line + content_type + message_body  # Menggabungkan baris respons, header, dan body

    return response  # Mengembalikan respons yang akan dikirim ke klien


if __name__ == "__main__":
    tcp_server() # Menjalankan server TCP saat file ini dijalankan sebagai program utama
 
