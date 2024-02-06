LIMITE_SAQUE = 500
LIMITE_DIARIO = 3
dinheiro = 100
tentativas = 0
deposito = 0
saque = 0
Operacao_realizada = 0
Saques_realizados = 0
depositos_realizados = 0

while True:
    print("Digite 1 para Saque")
    print("Digite 2 para Depósitos")
    print("Digite 3 para Extratos")
    print("Digite 4 para Sair")

    operacao = input("Selecione a operação: ")

    if operacao == "1":  # Saque
        while True:
            try:
                saque = int(input("Selecione a quantidade a ser sacada: "))
                break 
            except ValueError:
                print('Digite um número válido')

        if tentativas == LIMITE_DIARIO:
            print("Limite de saques diários atingido")

        if saque > LIMITE_SAQUE or saque > dinheiro:
            print(f"Quantidade requisitada maior que o limite de saque: {LIMITE_SAQUE} ou saldo disponível.")
        else:
            dinheiro -= saque
            print(f"Quantidade sacada: {saque}, dinheiro restante: {dinheiro}")
            tentativas += 1
            Saques_realizados += 1
            Operacao_realizada += 1

    elif operacao == "2":  # Depósito
         while True:
            try:
                deposito = int(input("Digite a quantidade a ser depositada: "))
                dinheiro += deposito
                depositos_realizados += 1
                Operacao_realizada += 1
                print(f"Quantidade depositada: {deposito}, dinheiro total: {dinheiro}")
                break 
            except ValueError:
                print('Digite um número válido')

    elif operacao == "3":  # Extrato
        if Operacao_realizada == 0 :
            print ("Não foram realizada movimentações")
        else:
            print(f"Saldo disponível: R${dinheiro}")
            print(f"quantidade depositada: R${deposito}")
            print(f"Quantidade sacada: R${saque}")
            print(f"Saques realizados: {Saques_realizados}")
            print(f"Depositos realizados: {depositos_realizados}")
    elif operacao == "4":  # Saída
        print("Adeus, volte sempre!")
        break

    else:
        print('Digite um número válido')
