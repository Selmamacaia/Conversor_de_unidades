def contar_pares_impares_percentagem(numeros):
    pares = 0
    impares = 0
    total = len(numeros)

    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

    percentagem_pares = (pares / total) * 100
    percentagem_impares = (impares / total) * 100

    return f"Percentagem de números pares: {percentagem_pares}%, Percentagem de números ímpares: {percentagem_impares}%."

# Exemplo de uso
numeros = [6, 2, 3, 4, 5, 6]
resultado = contar_pares_impares_percentagem(numeros)

print(resultado)

