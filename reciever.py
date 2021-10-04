import socket
import tqdm
import os

# Built by Asad
# For any kind of help related to this , contact me on discord - Asad#2809
host = "0.0.0.0"
port = 6001
size = 4096
sep = "<SEPARATOR>"
s = socket.socket()
s.bind((host, port))
s.listen(5)
print("Built by ~ Asad \n")
print(f"[*] Listening as {host}:{port}")
client_socket, address = s.accept()
print(f"[+] {address} is connected.")
received = client_socket.recv(size).decode()
filename, file_size = received.split(sep)
filename = os.path.basename(filename)
file_size = int(file_size)
progress = tqdm.tqdm(range(file_size), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(size)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))

client_socket.close()
s.close()

# Built by Asad
# For any kind of help related to this , contact me on discord - Asad#2809
