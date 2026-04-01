from pymongo import MongoClient

# conexão com MongoDB
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["producao"]
colecao = db["produtos"]

# limpar coleção (evita duplicação)
colecao.delete_many({})

# inserir produtos iniciais
produtos_iniciais = [
    {"_id": 1, "nome": "Produto A", "preco": 10, "lucro": 2, "categoria": "Cat1", "quantidade": 5},
    {"_id": 2, "nome": "Produto B", "preco": 20, "lucro": 4, "categoria": "Cat2", "quantidade": 10},
    {"_id": 3, "nome": "Produto C", "preco": 30, "lucro": 6, "categoria": "Cat3", "quantidade": 8},
    {"_id": 4, "nome": "Produto D", "preco": 40, "lucro": 8, "categoria": "Cat1", "quantidade": 6},
    {"_id": 5, "nome": "Produto E", "preco": 50, "lucro": 10, "categoria": "Cat2", "quantidade": 3}
]

colecao.insert_many(produtos_iniciais)

# ---------------- FUNÇÕES ----------------

def adicionar_produto():
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    lucro = float(input("Lucro: "))
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "lucro": lucro,
        "categoria": categoria,
        "quantidade": quantidade
    }

    colecao.insert_one(produto)
    print("Produto adicionado!")

def aumentar_lucro():
    porcentagem = float(input("Digite o aumento (%) do lucro: "))

    produtos = colecao.find()

    for p in produtos:
        novo_lucro = p["lucro"] * (1 + porcentagem / 100)

        colecao.update_one(
            {"_id": p["_id"]},
            {"$set": {"lucro": novo_lucro}}
        )

    print("Lucro atualizado com sucesso!")

def apagar_produto():
    nome = input("Nome do produto para apagar: ")

    resultado = colecao.delete_one({"nome": nome})

    if resultado.deleted_count > 0:
        print("Produto removido!")
    else:
        print("Produto não encontrado.")

# ---------------- MENU ----------------

while True:
    print("\n1 - Adicionar produto")
    print("2 - Aumentar lucro")
    print("3 - Apagar produto")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        aumentar_lucro()
    elif opcao == "3":
        apagar_produto()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")