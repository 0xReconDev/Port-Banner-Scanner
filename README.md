# 🛡️ Port Banner Scanner 1.0

Este é um script simples em Python que escaneia algumas portas específicas de um host salva manualmente em uma lista. Essa é uma versão antiga e experimental minha, já tenho a 1.2 que possue melhores tratamentos de erros e scan em multiplas portas. Vou melhorar ainda mais no futuro...

## 🔍 O que ele faz:

- Verifica se as portas 21 (FTP), 22 (SSH), 80 (HTTP) e 443 (HTTPS) estão abertas, pode ser modificada no arquivo.
- Para portas 80 e 443, faz uma requisição **HEAD** para capturar o status HTTP.
- Essas ports podem ser alteradas na array dentro do script.
  
## 📦 Requisitos:

- Python 3.x
- Biblioteca `requests` (instale com `pip install requests`)
- Recomenda-se usar ambiente linux, mas funciona no windows mas configurações prévias seram feitas.

## 🛠️ Como usar:

```bash
python3 banner.py exemplo.com
```

### 💡 Saída esperada
[+] 21 - 220 (vsFTPd 3.0.3)

[+] 22 - SSH-2.0-OpenSSH_8.4p1 Debian-5

[+] 80 - HTTP HEAD status: 200

[+] 443 - HTTPS HEAD status: 301

