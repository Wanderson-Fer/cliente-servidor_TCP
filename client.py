import socket

# Configurações do cliente
host = '127.0.0.1'  # Configurando para rodar localmente
port = 8081

# Cria o socket TCP
client_socket = socket.socket(
    socket.AF_INET,  # IPv4
    socket.SOCK_STREAM  # TCP | socket de stream
)

# Conecta ao servidor
client_socket.connect((host, port))

# Envia uma mensagem ao servidor
msg = "Hello World!\nOlá, servidor!"
client_socket.send(msg.encode('utf-8'))

# Fecha a conexão
client_socket.close()
