print("###############")
print("Calculadora do Senai")
print("Digite a operaçao a realizar!")
print("1- Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print ("###############")

opcao = int(input(""))

if opcao == 1:
    num1 = float(input("Digite o primeiro numero :"))
    num2 = float(input("Digite o segundo numero :"))
    
    #executando a operação de soma
    resultado = num1 + num2
    # exibir na tela com o texto -> f'{variavel}'
    print(f'O seu resultado e :{resultado}')
          
elif  opcao == 2:
    
    num1 = float(input("Digite o primeiro numero :"))
    num2 = float(input("Digite o segundo numero :"))
    
    #executando a operação de soma
    resultado = num1 + num2
    # exibir na tela com o texto -> f'{variavel}'
    print(f'O seu resultado e :{resultado}')

    

elif  opcao ==3:
    
    num1 = float(input("Digite o primeiro numero :"))
    num2 = float(input("Digite o segundo numero :"))
    
    #executando a operação de soma
    resultado = num1 * num2

    # exibir na tela com o texto -> f'{variavel}'
    print(f'O seu resultado e :{resultado}')



elif  opcao == 4:
    
    num1 = float(input("Digite o primeiro numero :"))
    num2 = float(input("Digite o segundo numero :"))
    
    #executando a operação de soma
    resultado = num1 / num2
       # exibir na tela com o texto -> f'{variavel}'
    print(f'O seu resultado e :{resultado}')

