itens = set()  

try:
    with open("lista_a.txt", "r", encoding="utf-8") as arquivo_a:
        linhas_a = arquivo_a.readlines()
        itens.update(linha.strip() for linha in linhas_a if linha.strip())
except FileNotFoundError:
    print("Aviso: arquivo 'lista_a.txt' não encontrado.")

try:
    with open("lista_b.txt", "r", encoding="utf-8") as arquivo_b:
        linhas_b = arquivo_b.readlines()
        itens.update(linha.strip() for linha in linhas_b if linha.strip())
except FileNotFoundError:
    print("Aviso: arquivo 'lista_b.txt' não encontrado.")

itens_ordenados = sorted(itens)

with open("lista_unica.txt", "w", encoding="utf-8") as arquivo_saida:
    for item in itens_ordenados:
        arquivo_saida.write(item + "\n")

print("Arquivo 'lista_unica.txt' criado com sucesso.")
