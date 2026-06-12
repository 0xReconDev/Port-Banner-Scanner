# 🛡️ Port Banner Scanner

O script em questão, tenta verificar se uma lista de portas passada pelo usuário via argumentos está abertas. E retorna as informações necessárias sobre a porta.

## 🔍 O que ele faz:

- Verifica se as portas passada pelo usuário estão abertas.
- Trata erros de digitação.
- Percorre uma lista de argumentos.
- Evita excesso de tráfego na rede.
  
## 📦 Requisitos

- Python 3.x
- Recomenda-se ambiente linux, mas windows também funciona.

## 🛠️ Como usar

```bash
python3 banner.py exemplo.com 80 443
```
### 💡 Saída esperada
[+] 80 - HTTPS HEAD status: 200.

[+] 443 - HTTPS HEAD status: 200.

## ⚠️ Aviso

- Este script foi feito para fins educacionais e de testes autorizados.
- Não utilize em redes ou sistemas sem permissão.
- Você é o único responsável pelo uso deste código.
