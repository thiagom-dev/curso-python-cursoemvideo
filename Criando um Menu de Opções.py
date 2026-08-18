n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

while True:

    print("=-" * 15)
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Menor")
    print("[5] Novos numeros")
    print("[6] Sair")
    print("=-" * 15)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        soma = n1 + n2
        print(f"A soma é {soma}")

    elif opcao == 2:
        multiplicar = n1 * n2
        print(f"A multiplicação é {multiplicar}")

    elif opcao == 3:
        if n1 > n2:
            print(f"O maior é {n1}")
        else:
            print(f"O maior é {n2}")

    elif opcao == 4:
        if n1 < n2:
            print(f"O menor é {n1}")
        else:
            print(f"O menor é {n2}")

    elif opcao == 5:
        print("Vamos digitar novos números!")
        n1 = int(input("Digite um novo número: "))
        n2 = int(input("Digite outro número: "))

    elif opcao == 6:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")