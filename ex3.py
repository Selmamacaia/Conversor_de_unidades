produtos = {}


i = 0
while i<5:
    try:
        nome_produto = input('Digite o nome do produto')
        valor_produto = float(input('Digite o valor do produto'))
        produtos[nome_produto] = valor_produto
        i+=1
    except ValueError:
        print("Insira um valor válido para o produto.")
    except Exception as e:
        print("Ocorreu um erro: ", e)


for k,v in produtos.items():
    if v>50:
        print(f'{k}: {v}')