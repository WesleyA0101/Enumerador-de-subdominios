import argparse
import datetime
import re

import dns.resolver

BOLD = "\033[1m"
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
CYAN = "\033[36m"

resolver = dns.resolver.Resolver()
resolver.nameservers = ["8.8.8.8", "8.8.4.4"]

parser = argparse.ArgumentParser(description="Enumerador de subdomínios")
parser.add_argument("dominio", help="Domínio alvo")
parser.add_argument("wordlist", help="Caminho para a wordlist de subdomínios")
parser.add_argument("--log", help="Arquivo para salvar logs", default="log.txt")

args = parser.parse_args()

alvo = re.sub(r"^https?://", "", args.dominio)
alvo = re.sub(r"^www\\.", "", alvo)
alvo = alvo.strip("/")
wordlist = args.wordlist
log_file = args.log


def escrever_log(mensagem):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as log:
        log.write(f"[{timestamp}] {mensagem}\n")


try:
    resolver.resolve(alvo, "A")
    msg = f"[+] Domínio {alvo} resolvido com sucesso."
    print(f"{GREEN}{BOLD}{msg}{RESET}")
    escrever_log(msg)
except dns.resolver.NXDOMAIN:
    msg = f"Erro: O domínio {alvo} não existe."
    print(f"{RED}{msg}{RESET}")
    escrever_log(msg)
    exit(1)
except Exception as e:
    msg = f"Erro ao tentar resolver o domínio: {str(e)}"
    print(f"{RED}{msg}{RESET}")
    escrever_log(msg)
    exit(1)

try:
    with open(wordlist, "r") as arq:
        subdominios = arq.read().splitlines()

        if not subdominios:
            msg = "Erro: A wordlist está vazia."
            print(f"{RED}{msg}{RESET}")
            escrever_log(msg)
            exit(1)

        msg = f"[+] Subdomínios carregados: {len(subdominios)}"
        print(f"{GREEN}{BOLD}{msg}{RESET}\n")
        escrever_log(msg)

        for subdominio in subdominios:
            sub_alvo = f"{subdominio}.{alvo}"
            try:
                resultados = resolver.resolve(sub_alvo, "A")
                for resultado in resultados:
                    msg = f"{sub_alvo} -> {resultado}"
                    print(f"{BOLD}{msg}{RESET}")
                    escrever_log(msg)
            except dns.resolver.NXDOMAIN:
                pass
            except dns.resolver.NoAnswer:
                pass
            except dns.resolver.LifetimeTimeout:
                pass
            except Exception as e:
                msg = f"Erro ao tentar resolver {sub_alvo}: {str(e)}"
                print(f"{RED}{msg}{RESET}")
                escrever_log(msg)
except FileNotFoundError:
    msg = f"Erro: O arquivo '{wordlist}' não foi encontrado."
    print(f"{RED}{msg}{RESET}")
    escrever_log(msg)
    exit(1)
