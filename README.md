# 🛡️ Port Banner Scanner Aprimoramento 1.2

O script em questão e uma versão aprimorada da minha primeira versão de port scan, agora ele verifica se uma lista de portas passada pelo usuário via argumentos está abertas. E retorna as informações necessárias sobre a porta. Possue melhores tratamentos de erros e mais segurança na execução.

## 🔍 Novas Funcionalidade:

- Verifica se as portas passada pelo usuário estão abertas.
- Trata erros de digitação.
- Percorre uma lista de argumentos.
- Evita excesso de tráfego na rede.
  
## 📦 Requisitos:

- Python 3.x
- Biblioteca requests (instale com pip install requests)
- Recomenda-se ambiente linux, mas windows também funciona.

## 🛠️ Como usar

```bash
python3 banner.py exemplo.com 80 443
```
### 💡 Saída esperada
[+] 80 - HTTPS HEAD status: 200.

[+] 443 - HTTPS HEAD status: 200.

- Agora ele aceita mais de uma porta, mas não quer dizer que todas estão abertas, aliás isso depende do host.

## ⚠️ Aviso

- Este script foi feito para fins educacionais e de testes autorizados.
- Não utilize em redes ou sistemas sem permissão.
- Você é o único responsável pelo uso deste código.
