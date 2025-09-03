def limpar_comentarios(texto):
    while "  " in texto:
        texto = texto.replace("  ", " ")

    texto = texto.replace("...", ".")
    return texto

try:
    with open("comentarios.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
except UnicodeDecodeError:
    try:
        with open("comentarios.txt", "r", encoding="latin-1") as arquivo:
            conteudo = arquivo.read()
    except Exception as erro:
        print(f"Erro ao ler o arquivo: {erro}")
        exit()

conteudo_limpo = limpar_comentarios(conteudo)

with open("comentarios_limpos.txt", "w", encoding="utf-8") as arquivo_saida:
    arquivo_saida.write(conteudo_limpo)

print("Arquivo 'comentarios_limpos.txt' criado com sucesso.")
