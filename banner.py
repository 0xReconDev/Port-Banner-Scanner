import socket
import sys

ip = sys.argv[1]
ports = [21, 22, 80, 443]

for port in ports:
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(2)
		code = sock.connect_ex((ip, port))

		if code == 0:

			if port == 443:
				try:
					requisicao_https = requests.head(f"https://{ip}/", timeout=3)
					print (f"[+] {port} - HTTPS HEAD status: {requisicao_https.status_code}.")
				except requests.RequestException as e:
					print (f"{port} - Erro na requisição HTTPS.")
			elif port == 80:
				try:
					# Tentar na porta 80
					requisicao = requests.head(f"http://{ip}/", timeout=3)
					print (f"[+] {port} - HTTP HEAD status: {requisicao.status_code}")
				except requests.RequestException as e:
					print (f"{port} - Erro na requisição HTTP: {e}")
		sock.close()
	except Exception as e:
		print (f"Erro ao conectar na porta {port}: {e}")
