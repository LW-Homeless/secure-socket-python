import socket
import ssl


class SocketSSL:

    def __init__(self):
        self.__certfile = r''  # Path to the cert.pem.
        self.__keyfile = r''  # Path to the private key.pem.
        self.__server_socket = None
        self.__ssl_context = None

    def socket_tcp(self):
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket.bind(("0.0.0.0", 8443))
        self.__server_socket.listen(1)

    # Wrapper the TCP socket with SSL.

    def wrapper_tcp_sock_ssl(self):
        self.__ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        self.__ssl_context.load_cert_chain(certfile=self.__certfile, keyfile=self.__keyfile)

    # Accept connections SSL.

    def accept_connection_ssl(self):
        client_socket, addr = self.__server_socket.accept()
        secure_socket = self.__ssl_context.wrap_socket(client_socket, server_side=True)
        print(f"Conexión segura establecida con {addr}")

        # Receive data
        while True:
            data = secure_socket.recv(1024)
            print(f"Cliente: {data.decode()}", end="")

            # Send response
            response = input('Server: ')
            secure_socket.sendall((response + '\n').encode())
            # secure_socket.close()


if __name__ == '__main__':
    sock_ssl = SocketSSL()
    sock_ssl.socket_tcp()
    sock_ssl.wrapper_tcp_sock_ssl()
    sock_ssl.accept_connection_ssl()
