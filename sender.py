import socket
import tqdm
import os

# Built by Asad
# For any kind of help related to this , contact me on discord - Asad#2809
sep = "<SEPARATOR>"
size = 1024 * 4  # 4KB
host = input("Enter the Ip of the machine of which you want to send the files to: ")
port = 6001
filename = input("enter the file name with its extension: ")


def send_file(filename, host, port):
    file_size = os.path.getsize(filename)
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    s.send(f"{filename}{sep}{file_size}".encode())
    progress = tqdm.tqdm(range(file_size), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(size)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            progress.update(len(bytes_read))

    s.close()


send_file(filename, host, port)

# Built by Asad
# For any kind of help related to this , contact me on discord - Asad#2809
