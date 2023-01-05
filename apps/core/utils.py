def rn_remove_itens(lista, itens_remover):
    return list(filter(lambda item_lista: item_lista not in itens_remover, lista))