try:
    
    with open("notas.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
   
    with open("notas.txt", "w") as arquivo:
        arquivo.write("Arquivo criado.")
    
    with open("notas.txt", "r") as arquivo:
        conteudo = arquivo.read()


print(conteudo)
