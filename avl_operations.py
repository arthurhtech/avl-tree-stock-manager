from utils import create_node, calculate_balance, get_height, rotate_left, rotate_right

def insert(node, id, name, quantity, price):
    if not node:
        return create_node(id, name, quantity, price)

    if id < node["id"]:
        node["left"] = insert(node["left"], id, name, quantity, price)
    elif id > node["id"]:
        node["right"] = insert(node["right"], id, name, quantity, price)
    else:
        print(f"ID {id} já existe no estoque!")
        return node

    # Atualizar altura
    node["height"] = 1 + max(get_height(node["left"]), get_height(node["right"]))

    # Balanceamento
    balance = calculate_balance(node)

    # Rotação simples à direita
    if balance > 1 and id < node["left"]["id"]:
        return rotate_right(node)

    # Rotação simples à esquerda
    if balance < -1 and id > node["right"]["id"]:
        return rotate_left(node)

    # Rotação dupla (esquerda-direita)
    if balance > 1 and id > node["left"]["id"]:
        node["left"] = rotate_left(node["left"])
        return rotate_right(node)

    # Rotação dupla (direita-esquerda)
    if balance < -1 and id < node["right"]["id"]:
        node["right"] = rotate_right(node["right"])
        return rotate_left(node)

    return node

def search(node, id):
    if not node:
        print("Item não encontrado!")
        return None

    if id == node["id"]:
        print(f"Encontrado: ID={node['id']}, Nome={node['name']}, Quantidade={node['quantity']}, Preço={node['price']}")
        return node
    elif id < node["id"]:
        return search(node["left"], id)
    else:
        return search(node["right"], id)

def in_order(node):
    if node:
        in_order(node["left"])
        print(f"ID={node['id']}, Nome={node['name']}, Quantidade={node['quantity']}, Preço={node['price']}")
        in_order(node["right"])
