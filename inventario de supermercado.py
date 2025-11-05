
dicionario = {
    1: {"nome": "Arroz integral 1kg", "quantidade": 22, "valor": 24.90},
    2: {"nome": "doce de leite 500g", "quantidade": 15, "valor": 8.50},
    3: {"nome": "Espaguete 500g", "quantidade": 19, "valor": 6.99},
    4: {"nome": "Óleo de Soja 900ml", "quantidade": 12, "valor": 7.99},
    5: {"nome": "Açúcar Refinado 1kg", "quantidade": 25, "valor": 5.00},
    6: {"nome": "Café Torrado 500g", "quantidade": 30, "valor": 18.90},
    7: {"nome": "Leite Integral 1L", "quantidade": 18, "valor": 4.79},
    8: {"nome": "Pão de Forma 500g", "quantidade": 20, "valor": 9.50},
    9: {"nome": "Frango Congelado 1kg", "quantidade": 14, "valor": 15.90},
    10: {"nome": "chocolate 100g", "quantidade": 10, "valor": 34.90}
}

#Usuario e senha para login
usuario_correto = "backup22"
senha_correta = "151515"


#função dos botões do menu
def visualizar_estoque():
    print("\nEstoque Atual:")
    for codigo, produto in dicionario.items():
        print(f"Cód: {codigo} | {produto['nome']} - Quantidade: {produto['quantidade']} - R$ {produto['valor']:.2f}")

def adicionar_produto():
    nome = input("Nome do novo produto: ")
    quantidade = int(input("Quantidade inicial: "))
    valor = float(input("Valor unitário: "))

    novo_codigo = max(dicionario.keys(), default=0) + 1
    dicionario[novo_codigo] = {"nome": nome, "quantidade": quantidade, "valor": valor}
    print(f"Produto '{nome}' adicionado com sucesso!")

def remover_produto():
    codigo = int(input("Digite o código do produto a remover: "))
    if codigo in dicionario:
        nome_removido = dicionario[codigo]["nome"]
        del dicionario[codigo]
        print(f"Produto '{nome_removido}' removido com sucesso!")
    else:
        print("Código não encontrado.")

#menu interativo do estoque, visualizar, adicionar, remover e sair
def menu():
    while True:
        print("\n--- Menu Estoque ---")
        print("1. Visualizar estoque atual")
        print("2. Adicionar novo item ao estoque")
        print("3. Remover um item do estoque")
        print("4. Sair")

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            visualizar_estoque()
        elif escolha == "2":
            adicionar_produto()
        elif escolha == "3":
            remover_produto()
        elif escolha == "4":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

#area de checagem do login, permitir ou negar
def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso permitido")
        menu()
    else:
        print("Acesso negado")


#inicializador do programa, executa todo o script
def main():
    login()



main()
