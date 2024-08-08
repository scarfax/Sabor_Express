def calcular_soma(lista_numeros):
    soma = 0
    try:
        for numero in lista_numeros:
            soma += numero
    except TypeError as e:
        print(f"Erro: {e}. Certifique-se de que todos os elementos da lista são números.")
    return soma

# Exemplo de uso
numeros = [1, 2, 3, 4, 5]
resultado = calcular_soma(numeros)
print(f"A soma dos elementos da lista é: {resultado}")