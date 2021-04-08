# Função básica para limpar input de nome

def entradaDados():
    nomeSplitado = []

    nome = str(input("Digite seu nome: "))

    nomeFormatado = nome.strip().lower().split()
    for i in range(len(nomeFormatado)):

        # So aceita se o qualquer dos nomes tiver mais de 1 char e nao aceita numeros no nome
        if len(nomeFormatado[i]) >= 2 and not(any(map(str.isdigit, nomeFormatado[i]))):

            nomeSplitado.append(nomeFormatado[i].capitalize())

    nomeJoin = " ".join(nomeSplitado)
    print(nomeJoin)

def main():
    entradaDados()

main()