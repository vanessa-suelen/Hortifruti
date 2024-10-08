def cadastrar_produtos():
    produtos = []
    quantidade = int(input("Digite a quantidade de produtos a serem cadastrados: "))

    for _ in range(quantidade):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))

        
        for produto in produtos:
            if produto[0].lower() == nome.lower():  
                print("Produto já cadastrado")
                break
        else:
            
            produtos.append((nome, preco))
    
    return produtos


def buscar_precos(produtos):
    while True:
        busca = input("Digite o nome do produto para buscar o preço (ou 'Fim' para sair): ")
        
        if busca.lower() == "fim":
            break
        
        encontrado = False
        for produto in produtos:
            if produto[0].lower() == busca.lower():  
                print(f"O preço de {produto[0]} é R$ {produto[1]:.2f}")
                encontrado = True
                break
        
        if not encontrado:
            print("Produto não cadastrado")


def main():
    produtos = cadastrar_produtos()
    buscar_precos(produtos)


if __name__ == "__main__":
    main()

    
