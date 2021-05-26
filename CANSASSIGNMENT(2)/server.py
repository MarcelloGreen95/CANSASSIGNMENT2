import socket, os, threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 4466
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server data"

"""
CMD@MSg
"""


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected!")
    conn.send("OK@Welcome to the File server.".encode(FORMAT))

    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]

        if cmd == "HELP":
            send_data = "OK@"
            send_data += "LIST: List all the data on the server.\n"
            send_data += "UPLOAD <path> Upload a file.\n"
            send_data += "DELETE <filename> Delete a file from the server.\n"
            send_data += "LOGOUT: Disconnect from the server.\n"
            send_data += "HELP: List all the commands."

            conn.send(send_data.encode(FORMAT))
        elif cmd == "LOGOUT":
            break
        elif cmd == "LIST":
            pass
        elif cmd == "UPLOAD":
            pass
        elif cmd == "DELETE":
            pass

    print(f"[DISCONNECTED] {addr} disconnected!")


def main():
    print("[STARTING] Server is starting....")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening....")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    main()
