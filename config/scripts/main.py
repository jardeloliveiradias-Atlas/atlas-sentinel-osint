import json

print("=" * 50)
print("ATLAS SENTINEL OSINT")
print("=" * 50)

with open("config/palavras_chave.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(f"Instituição monitorada: {dados['instituicao']}")
print()

for categoria, pesquisas in dados["categorias"].items():
    print(f"Categoria: {categoria}")

    for pesquisa in pesquisas:
        print("  •", pesquisa)

    print()
