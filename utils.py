def create_node(id, name, quantity, price):
    return {
        "id": id,
        "name": name,
        "quantity": quantity,
        "price": price,
        "left": None,
        "right": None,
        "height": 1
    }

def get_height(node):
    return node["height"] if node else 0

def calculate_balance(node):
    if not node:
        return 0
    return get_height(node["left"]) - get_height(node["right"])

def rotate_right(y):
    x = y["left"]
    T2 = x["right"]

    # Rotação
    x["right"] = y
    y["left"] = T2

    # Atualizar alturas
    y["height"] = 1 + max(get_height(y["left"]), get_height(y["right"]))
    x["height"] = 1 + max(get_height(x["left"]), get_height(x["right"]))

    return x

def rotate_left(x):
    y = x["right"]
    T2 = y["left"]

    # Rotação
    y["left"] = x
    x["right"] = T2

    # Atualizar alturas
    x["height"] = 1 + max(get_height(x["left"]), get_height(x["right"]))
    y["height"] = 1 + max(get_height(y["left"]), get_height(y["right"]))

    return y
