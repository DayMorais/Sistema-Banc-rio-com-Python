menu = """

[d] Depositar
[s] Sacar
[e] Consultar Extrato
[q] Sair

=> """

saldo = 0
LIMITE = 500
extrato = ""
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual valor deseja depositar? "))

        if valor > 0:
            saldo = saldo + valor
            extrato = extrato + f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Não foi possível completar a operação. Por favor, digite um valor válido.")

    elif opcao == "s":
        valor = float(input("Qual valor deseja sacar? "))

        saldo_excedido = valor > saldo
        limite_excedido = valor > LIMITE
        quantidade_saques_excedida = quantidade_saques > 3

        if saldo_excedido:
            print("Operação inválida! Saldo Insuficiente.")

        elif limite_excedido:
            print("Operação inválida! Limite de saque excedido.")
        
        elif quantidade_saques_excedida:
            print("Operação inválida! Limite de saques diários excedido.")
        
        elif valor > 0:
            saldo = saldo - valor
            extrato = extrato + f"Saque: R$ {valor:.2f}\n"
            quantidade_saques = quantidade_saques + 1
        
        else:
            print("Não foi possível completar a operação. Por favor, digite um valor válido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Sem movimentações." if not extrato else extrato)

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Por favor selecione uma opção disponível.")