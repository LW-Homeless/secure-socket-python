import os
import socket
import ssl

from rich import print


class ClientSocketSSL:

    def __init__(self, server_name, port_number):
        self.__server_name = server_name
        self.__port_number = port_number

        self.__clean_screen()

    def connect_server(self):
        try:
            ssl_context = ssl._create_unverified_context()
            client_socket = socket.create_connection((self.__server_name, self.__port_number))
            secure_socket = ssl_context.wrap_socket(client_socket, server_hostname=self.__server_name)

            while True:
                request = input("Client > ")
                secure_socket.sendall((request + '\n').encode())

                response = secure_socket.recv(1024)
                print(f'[green]Server: {response.decode()}[/green]', end='')
        except KeyboardInterrupt:
            print(f'\n[red][X] Closed connection with the server[/red]', end='')

    def __clean_screen(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system("cls")


if __name__ == '__main__':
    server_name = input('Enter server name > ')
    port_number = input('Enter server port > ')

    clnt_socket = ClientSocketSSL(server_name, port_number)
    clnt_socket.connect_server()
