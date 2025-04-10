# SSL Socket en Python

Este repositorio contiene un ejemplo práctico de cómo implementar una comunicación cliente-servidor segura usando **SSL/TLS en Python**, mediante el módulo `ssl` de la biblioteca estándar.

## Estructura del proyecto

- `SocketSSL.py`: Servidor que utiliza un certificado SSL para cifrar la conexión.
- `ClientSocketSSL.py`: Cliente que se conecta al servidor usando SSL.
- `cert/`: Contiene el certificado (`cert.pem`) y la clave privada (`key.pem`) auto-firmados.

## Requisitos

- Python 3.11.3 o superior
- OpenSSL instalado para generar los certificados
- pip3 install rich==14.0.0


## Cómo generar el certificado

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
```
Guarda key.pem y cert.pem en la carpeta cert/. 

## Cómo ejecutar
- Primero inicia el servidor: python3 SocketSSL.py
- En otra terminal, inicia el cliente: python3 ClienteSocketSSL.py

Artículo completo en LinkedIn.  
[Cómo crear un socket seguro (SSL/TLS) en Python](https://www.linkedin.com/pulse/c%C3%B3mo-crear-un-socket-seguro-ssltls-en-python-meneses-castillo-buwue)