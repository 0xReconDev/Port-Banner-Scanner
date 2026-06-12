import socket
import sys
import requests

ip = sys.argv[1]
ports = [21, 22, 80, 443]

for port in ports:
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(2)
		code = sock.connect_ex((ip, port))

		if code == 0:
			try:
				requisicao_https = requests.head(f"https://{ip}/", timeout=3)
				print (f"[+] {port} - HTTPS HEAD status: {requisicao_https.status_code}.")
			except requests.RequestException as e:
				print (f"{port} - Erro na requisição HTTPS.")
				
		sock.close()
	except Exception as e:
		print (f"Erro ao conectar na porta {port}: {e}")
