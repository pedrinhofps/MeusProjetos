saldo = 1500
limite_saque = 500
limite_saque_diario = 0
limite_saque_diario_total = 3

while True:
    print(f"""
========= Menu =========
1. Depositar
2. Sacar
3. Extrato
4. Sair
=======================
""")
    opcao = int(input("Selecione uma opção: "))
    if opcao == 1:
        print(f"""
========= Menu =========
Saldo atual: R${saldo:.2f}
=======================
""")
        valor_deposito = float(input("Quanto quer depositar? "))
        if valor_deposito < 100:
            print("Valor insuficiente.")
        else:
            saldo += valor_deposito
            print(f"""
========= Menu =========
Valor depositado: R${valor_deposito:.2f}
Saldo atual: R${saldo:.2f}
=======================
""")
    elif opcao == 2:
        print(f"""
========= Menu =========
Saldo atual: R${saldo:.2f}
=======================
""")
        valor_saque = float(input("Qual valor você deseja sacar? "))
        if limite_saque_diario >= limite_saque_diario_total:
            print("Você atingiu o limite de saques diários.")
        elif valor_saque <= limite_saque and valor_saque <= saldo:
            saldo -= valor_saque
            limite_saque_diario += 1
            print(f"""
========= Menu =========
Valor do saque: R${valor_saque:.2f}
Saldo atual: R${saldo:.2f}
=======================
""")
        else:
            print("Valor de saque inválido.")
    elif opcao == 3:
        print("Extrato...")
        print(f"Saldo atual: R${saldo:.2f}")
    elif opcao == 4:
        print("Saindo do programa...")
        break
    else: 
        print("Opção inválida, tente novamente.")
