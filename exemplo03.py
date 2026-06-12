while True:
    try:
        valor1 = int(input("Digite o primeiro valor: "))
        break
    except ValueError:
        print("Valor inválido! Por favor, digite um número inteiro.")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        exit(1)

while True:
    try:
        valor2 = int(input("Digite o segundo valor: "))
        break
    except ValueError:
        print("Valor inválido! Por favor, digite um número inteiro.")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        exit(1)

print("Selecione uma opção: ")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Digite a opção desejada: "))

resultado = None
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
if resultado is not None:
    print("Resultado: ", resultado)
