dicionario_jogadores = {}

try:
    with open("jogadores_times.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        
    for linha in linhas:
        linha = linha.strip()
        
        try:
            if ',' in linha:
                nome, time = linha.split(",", 1) 
                dicionario_jogadores[nome.strip()] = time.strip()
            else:
                
                try:
                    with open("linhas_invalidas.log", "a", encoding="utf-8") as log:
                        log.write(linha + "\n")
                except Exception as erro_log:
                    print(f"Erro ao escrever no log: {erro_log}")
        except Exception as erro_split:
            print(f"Erro ao processar linha: {linha} — {erro_split}")

except FileNotFoundError:
    print("Arquivo 'jogadores_times.txt' não encontrado.")
except Exception as erro:
    print(f"Ocorreu um erro ao ler o arquivo: {erro}")


print("Dicionário de jogadores e times:")
for jogador, time in dicionario_jogadores.items():
    print(f"{jogador} → {time}")
