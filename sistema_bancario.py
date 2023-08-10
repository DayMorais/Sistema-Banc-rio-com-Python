def menu():
    menu = """\n
    ================MENU=================
    [d]\tDepositar
    [s]\tSacar
    [e]\tConsultar Extrato
    [nc]\tAbrir Nova Conta
    [lc]\tListar Contas
    [nu]\tCriar Novo usuário
    [q]\tSair
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo = saldo + valor
        extrato = extrato + f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado!")
    else:
        print("\n Não foi possível completar a operação. Por favor, digite um valor válido.")
    
    return saldo, extrato

def sacar(*,saldo, valor, extrato, LIMITE, quantidade_saques, LIMITE_SAQUES):
    saldo_excedido = valor > saldo
    limite_excedido = valor > LIMITE
    quantidade_saques_excedida = quantidade_saques > LIMITE_SAQUES
    
    if saldo_excedido:
            print("\nOperação inválida! Saldo Insuficiente.")
    elif limite_excedido:
            print("\nOperação inválida! Limite de saque excedido.")
        
    elif quantidade_saques_excedida:
            print("\nOperação inválida! Limite de saques diários excedido.")
        
    elif valor > 0:
            saldo = saldo - valor
            extrato = extrato + f"Saque:\tR$ {valor:.2f}\n"
            quantidade_saques = quantidade_saques + 1
            print("\n Saque realizado!")
    else:
            print("\nNão foi possível completar a operação. Por favor, digite um valor válido.")
    
    return saldo, extrato

def consultar_extrato(saldo, /, *, extrato):
     print("\n================ EXTRATO ================")
     print("Sem movimentações." if not extrato else extrato)
     print(f"\nSaldo:\tR$ {saldo:.2f}")
     print("=========================================")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n CPF já cadastrado")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite seu endereço (logadouro, nº, bairro - cidade/estado): ")
    
    usuarios.append({"Nome": nome, "Data de nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco})
    
    print("Usuário cadastrado!")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, conta, usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Conta cadastrada com sucesso!")
        return {"Agência": agencia, "Conta corrente": conta, "Usuário": usuario}
    
    print("\n Não foi possível realizar a operação. Usuário não cadastrado")
    
def listar_contas(contas):
    for conta in contas:
        dados_conta = f"""\n
        Agência:\t{conta['agencia']}
        C/C:\t{conta['conta']}
        Titular:\t{conta['usuario']['nome']}
    """
    print("=" * 100)
    print(dados_conta)
    
def main():
    saldo = 0
    LIMITE = 500
    extrato = ""
    quantidade_saques = 0
    LIMITE_SAQUES = 3
    usuarios: []
    contas: []
    AGENCIA: "0001"
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Qual valor deseja depositar? "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Qual valor deseja sacar? "))
            
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITE, número_saques=quantidade_saques, limite_saques=LIMITE_SAQUES)
            
        elif opcao == "e":
            consultar_extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, conta, usuarios, contas)
            
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break
        
        else:
            print("Opção inválida. Por favor selecione uma opção disponível.")