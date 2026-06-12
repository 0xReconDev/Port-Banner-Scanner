import socket
import sys
import requests


if len(sys.argv) < 3: # Verificar se o número de argumentos é menor que 3 (script.py, IP/Domínio, Porta)
	print('Uso: python script.py <IP/Domínio> <Porta>')
	sys.exit(1)

try: # Tentar obter o IP ou domínio e a porta a partir dos argumentos
	ip = sys.argv[1]
	port_user = list(map(int, sys.argv[2:])) # Permitir múltiplas portas separadas por vírgula, por exemplo: 80,443,22
except IndexError: # Verificar se o IP ou domínio foi fornecido
	print('[!] Você precisa colocar o IP ou domínio do alvo.')
	sys.exit(1)
except ValueError: # Verificar se a porta é um número inteiro
	print('[!] A porta deve ser um número inteiro, e use espaços para separar as portas. Exemplo: 80 443 22')
	sys.exit(1)

ports_lists = port_user # Converter as portas para uma lista de inteiros, permitindo intervalos como 20-25

for port in ports_lists:
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criar socket
		sock.settimeout(2) # Definitir timeout para 2 segundos
		code = sock.connect_ex((ip, port)) # Tentar conectar na porta e obter o código de resposta

		if code == 0:

			if port == 443:
				try:
					requisicao_https = requests.head(f"https://{ip}/", timeout=3) # Tentar na porta 443
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
		print (f"[!] Erro ao conectar na porta {port}: {e}")

if code != 0:
	print('[!] As demais portas não foram encontrada e o socket foi fechado.')