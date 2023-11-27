import socket

# Configurações do servidor
host = '127.0.0.1'  # Configurando para rodar localmente
port = 8081

# Cria o socket TCP
server_socket = socket.socket(
    socket.AF_INET,  # IPv4
    socket.SOCK_STREAM  # TCP | socket de stream
)

# Liga o socket ao endereço e porta especificados
server_socket.bind((host, port))

# Aguarda até 5 conexões pendentes
server_socket.listen(5)

print(f"Servidor escutando em {host}:{port}")

# Aceita a conexão do cliente
client_socket, addr = server_socket.accept()
print(f"Conexão recebida de {addr}")

# Recebe a mensagem do cliente
mensagem_recebida = client_socket.recv(1024).decode('utf-8')
print(f"Mensagem recebida do cliente: {mensagem_recebida}")

# Fecha a conexão
client_socket.close()
server_socket.close()
