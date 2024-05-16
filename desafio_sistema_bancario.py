opcao = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(opcao)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"O valor de R${valor:.2f} foi depositado!")

        else:
            print("Algo deu errado! :( Favor Verificar o valor de deposito, caso o erro persista entrar em contato com o gerente.)")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Ops algo deu errado! Verifique o saldo.")

        elif excedeu_limite:
            print("Ops algo deu errado! Valor limite de saque excedido.")

        elif excedeu_saques:
            print("Ops algo deu errado! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("aguarde estamos processando o seu pedido de saque...")

        else:
            print("Ops algo deu errado! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("Obrigado pela preferencia!")
        print("==========================================")

    elif opcao == "0":
        print("Obrigada por usar nosso sistema!!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print("Banco Z sempre com você!")