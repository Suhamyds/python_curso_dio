import textwrap

def opcao():
    opcao = """\n
    ++++++++++++++++++++++++++++
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] listar contas
    [6] Novo usuario
    [0] Sair

    => """
    return input(textwrap.dedent(opcao))

def depositar(saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"O valor de R${valor:.2f} foi depositado!")
    else:
        print("Algo deu errado! :( Favor Verificar o valor de deposito, caso o erro persista entrar em contato com o gerente.)")
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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
    return saldo,   extrato

def exibir_extrato(saldo, / , *,extrato):   
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("Obrigado pela preferencia!")
        print("==========================================")

def criar_ususario(usuario):
    cpf = input("Informe o CPF (somente numero):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("usuario já cadastrado! ")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/estado)")

    usuario.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("usuario cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
         
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuario ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta,"usuario":usuario}

    print("Usuario não cadastrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta["agencia"]}
            c/c: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
    """
    print("=" * 100)
    print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0 
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    #numero_conta =1

    while True:
        tipo = opcao()

        if tipo == "1":
            valor = float(input("Informe o valor do deposito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif tipo == "2":
            valor = float(input("informe o valor de saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif tipo == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif tipo == "4":
            criar_ususario(usuarios)

        elif tipo == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                #numero_conta +=1

        elif tipo == "6":
            listar_contas(contas)

        elif tipo == "0":
            print("Obrigada por usar nosso sistema bancario !!")
            break