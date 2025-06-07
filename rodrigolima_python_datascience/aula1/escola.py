"""
Solicitar 4 notas para o usario
Realizar o calculo da media
Se a nota for maior que 7

Usuario aprovado

caso contrario a nota seja menor que 7
Usuário reprovado

"""
print("#############")
print("Escola Senai")
print("#############")

n1 = float(input("Digite a primeira nota : "))
n2 = float(input("Digite a segunda nota :"))
n3 = float(input("Digite a terceira nota :"))
n4 = float(input("Digite a quarta nota :"))
media =(n1+n2+n3+n4)/4

if media >=7:
    print("Voce foi aprovado")
elif media <=7:
    print("Voce foi reprovado")
    
   


  
    



