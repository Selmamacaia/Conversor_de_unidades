def converter_temperatura(valor, unidade_origem, unidade_destino):
    if unidade_origem == "Celsius" and unidade_destino == "Fahrenheit":
        return valor * 9/5 + 32
    elif unidade_origem == "Fahrenheit" and unidade_destino == "Celsius":
        return (valor - 32) * 5/9
    else:
        return "Conversão não suportada"

def converter_comprimento(valor, unidade_origem, unidade_destino):
    if unidade_origem == "metros" and unidade_destino == "centimetros":
        return valor * 100
    elif unidade_origem == "centimetros" and unidade_destino == "metros":
        return valor / 100
    else:
        return "Conversão não suportada"

def converter_peso(valor, unidade_origem, unidade_destino):
    if unidade_origem == "quilogramas" and unidade_destino == "gramas":
        return valor * 1000
    elif unidade_origem == "gramas" and unidade_destino == "quilogramas":
        return valor / 1000
    else:
        return "Conversão não suportada"

tipo_conversao = input("Qual tipo de conversão você deseja fazer? (temperatura, comprimento, peso): ")
valor = float(input("Digite o valor a ser convertido: "))
unidade_origem = input("Digite a unidade de origem: ")
unidade_destino = input("Digite a unidade de destino: ")

if tipo_conversao == "temperatura":
    resultado = converter_temperatura(valor, unidade_origem, unidade_destino)
elif tipo_conversao == "comprimento":
    resultado = converter_comprimento(valor, unidade_origem, unidade_destino)
elif tipo_conversao == "peso":
    resultado = converter_peso(valor, unidade_origem, unidade_destino)
else:
    resultado = "Tipo de conversão não suportado"

print(f"Resultado da conversão: {resultado}")
