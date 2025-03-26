import argparse
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

args = parser.parse_args()

alvo = re.sub(r"^https?://", "", args.dominio)
alvo = re.sub(r"^www\.", "", alvo)
alvo = alvo.strip("/")
wordlist = args.wordlist

try:
    resolver.resolve(alvo, "A")
    print(f"{GREEN}[+] {BOLD}Domínio {alvo} resolvido com sucesso.{RESET}")
except dns.resolver.NXDOMAIN:
    print(f"{RED}Erro: O domínio {alvo} não existe.{RESET}")
    exit(1)
except Exception as e:
    print(f"{RED}Erro ao tentar resolver o domínio: {str(e)}{RESET}")
    exit(1)

try:
    with open(wordlist, "r") as arq:
        subdominios = arq.read().splitlines()

        if not subdominios:
            print(f"{RED}Erro: A wordlist está vazia.{RESET}")
            exit(1)

        print(f"{GREEN}[+] {BOLD}Subdomínios carregados:{RESET} {CYAN}{len(subdominios)}{RESET}\n")

        for subdominio in subdominios:
            sub_alvo = f"{subdominio}.{alvo}"

            try:
                resultados = resolver.resolve(sub_alvo, "A")
                for resultado in resultados:
                    print(f"{BOLD}{sub_alvo} -> {resultado}{RESET}")
            except dns.resolver.NXDOMAIN:
                pass
            except dns.resolver.NoAnswer:
                pass
            except dns.resolver.LifetimeTimeout:
                pass
            except Exception as e:
                print(f"{RED}Erro ao tentar resolver {sub_alvo}: {str(e)}{RESET}")
                pass

except FileNotFoundError:
    print(f"{RED}Erro: O arquivo '{wordlist}' não foi encontrado.{RESET}")
    exit(1)
