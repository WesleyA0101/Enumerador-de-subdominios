import sys
import dns.resolver

resolver = dns.resolver.Resolver()

if len(sys.argv) < 3:
    print("Uso correto: python enumerador-de-subdominios.py  <dominio> <wordlist>")
    sys.exit(1)

alvo = sys.argv[1]
wordlist = sys.argv[2]

try:
    with open(wordlist, "r") as arq:
        subdominios = arq.read().splitlines()
except FileNotFoundError:
    print(f"Erro: O arquivo '{wordlist}' não foi encontrado.")
    sys.exit(1)

for subdominio in subdominios:
    try:
        sub_alvo = f"{subdominio}.{alvo}"
        resultados = resolver.resolve(sub_alvo, "A")
        for resultado in resultados:
            print(f"{sub_alvo} -> {resultado}")
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        print(f"Sem resposta para {sub_alvo}")
    except dns.resolver.LifetimeTimeout:
        print(f"Tempo limite excedido para {sub_alvo}")
    except Exception as e:
        print(f"Erro ao resolver {sub_alvo}: {e}")

