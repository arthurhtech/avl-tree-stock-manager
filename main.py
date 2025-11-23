from avl_operations import insert, search, in_order

def menu():
    root = None

    while True:
        print("\n1. Adicionar item")
        print("2. Buscar item")
        print("3. Mostrar estoque ordenado")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            id = int(input("ID: "))
            name = input("Nome: ")
            quantity = int(input("Quantidade: "))
            price = float(input("Preço: "))
            root = insert(root, id, name, quantity, price)
        elif choice == "2":
            id = int(input("ID do item a buscar: "))
            search(root, id)
        elif choice == "3":
            print("Estoque ordenado:")
            in_order(root)
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()