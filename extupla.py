
Produto = tuple

def valor_total_estoque(produto):
    _, preco, quantidade = produto
    return preco * quantidade

def produto_disponivel(produto):
    _, _, quantidade = produto
    return quantidade > 0

def informacoes_produto(produto):
    nome, preco, quantidade = produto
    return f"Nome do Produto: {nome}, Preço: R${preco, 'R$'} , Quantidade em estoque: {quantidade}"
   

produto = ("Notebook", 2000.00, 10)

print(informacoes_produto(produto))

print("Valor total em estoque é de:", valor_total_estoque(produto), 'R$')


print("Produto disponível?" , "Sim" if produto_disponivel(produto) else "Não")
