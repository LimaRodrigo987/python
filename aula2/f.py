class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"\n✅ Depósito de R${valor:.2f} realizado!")
        else:
            print("\n❌ Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor:.2f}")
            print(f"\n✅ Saque de R${valor:.2f} realizado!")
        else:
            print("\n❌ Saldo insuficiente ou valor inválido.")

    def ver_extrato(self):
        print(f"\n📊 Extrato de {self.titular}:")
        for movimento in self.extrato:
            print(f"  → {movimento}")
        print(f"Saldo atual: R${self.saldo:.2f}")

def menu():
    print("\n" + "=" * 30)
    print("  BANCO PYTHON ".center(30, "🟦"))
    print("=" * 30)
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Extrato")
    print("0. Sair")

# Cria uma conta para teste
conta = ContaBancaria("João da Silva")

while True:
    menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        try:
            valor = float(input("Valor para depositar: R$"))
            conta.depositar(valor)
        except ValueError:
            print("❌ Digite um número válido!")

    elif opcao == "2":
        try:
            valor = float(input("Valor para sacar: R$"))
            conta.sacar(valor)
        except ValueError:
            print("❌ Digite um número válido!")

    elif opcao == "3":
        conta.ver_extrato()

    elif opcao == "0":
        print("\nObrigado por usar o Banco Python! Até logo! 🏦")
        break

    else:
        print("❌ Opção inválida! Tente novamente.")