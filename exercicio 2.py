try:
    with open("frases.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        
        linhas_nao_vazias = [linha for linha in linhas if linha.strip() != '']
        print(f"Quantidade de linhas não vazias: {len(linhas_nao_vazias)}")
except FileNotFoundError:
    print("Não foi possível acessar o arquivo 'frases.txt'.")
