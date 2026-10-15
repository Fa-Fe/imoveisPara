import csv

dados = "data.csv"
def ler_dados(dados):
    with open(dados, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo) #Usa o cabeçalho do arquivo como chaves
        for orgao_publico in leitor:
            if orgao_publico["municipio"] == "Santa Luzia do Pará":
                for campo, valor in orgao_publico.items(): #percorre o dicionario pegando chave e valor
                    print(f"{campo}: {valor}")

ler_dados(dados)

