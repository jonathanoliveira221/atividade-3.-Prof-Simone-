import string

try:
    with open("texto.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        
        conteudo = conteudo.lower()
        
        for pontuacao in string.punctuation:
            conteudo = conteudo.replace(pontuacao, "")
        
        palavras = conteudo.split()
        
        palavras_distintas = set(palavras)
        
        print(f"Quantidade de palavras distintas: {len(palavras_distintas)}")

except FileNotFoundError:
    print("Arquivo texto.txt não encontrado.")
