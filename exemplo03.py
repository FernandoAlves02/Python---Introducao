valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
print("Selecione uma opção: ")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
        resultado = valor1 + valor2
    case 2:
        resultado = valor1 - valor2
    case 3:
        resultado = valor1 * valor2
    case 4:
        resultado = valor1 / valor2
    case _:
        print("Opção inválida!")
print("Resultado: ", resultado)
