# 🌐 Enumerador de Subdomínios

Bem-vindo ao **Enumerador de Subdomínios**, uma ferramenta eficiente para a descoberta de subdomínios de um domínio alvo utilizando consultas DNS.

## 🚀 Funcionalidades
✅ Enumeração automática de subdomínios
✅ Resolução DNS para obtenção de endereços IP
✅ Tratamento avançado de erros
✅ Suporte a wordlists personalizadas
✅ Simplicidade e eficiência na execução

## 📌 Requisitos
Antes de executar o script, certifique-se de ter o **Python 3** instalado e instale as dependências com:

```bash
pip install -r requirements.txt
```

## 🛠️ Uso
A execução do script segue a seguinte sintaxe:

```bash
python enumerador-de-subdominios.py <dominio> <wordlist>
```

### 🔹 Parâmetros
- `<dominio>`: O domínio alvo para a enumeração.
- `<wordlist>`: Arquivo contendo a lista de subdomínios a serem testados.

### 🔹 Exemplo de uso
```bash
python enumerador-de-subdominios.py exemplo.com wordlist.txt
```

## ⚠️ Tratamento de Erros
O script conta com um sistema robusto de tratamento de erros, garantindo maior estabilidade durante a execução:
- `FileNotFoundError`: Wordlist não encontrada.
- `NXDOMAIN`: O subdomínio não existe.
- `NoAnswer`: O servidor DNS não retornou resposta.
- `LifetimeTimeout`: Tempo limite excedido na requisição DNS.
- `Exception`: Qualquer outro erro será registrado para depuração.

## 📊 Exemplo de Saída
```bash
www.exemplo.com -> 192.168.1.1
test.exemplo.com -> 192.168.1.2
Sem resposta para api.exemplo.com
Tempo limite excedido para mail.exemplo.com
```

## 📜 Licença
Este projeto é distribuído sob a licença **GNU General Public License v3.0**. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE).

## 📧 Contribuições aceitas...

